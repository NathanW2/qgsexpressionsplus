"""
QGIS expression functions for sampling raster and vector layers.
"""

import qgis.core
import qgis.gui
from qgis.utils import QgsMessageLog as logger, iface


@qgis.core.qgsfunction(args="auto", group="Expressions +", register=False)
def sample_raster(layer_name, band_index, feature, parent):
    """
    Sample a raster layer

    <h4>Syntax</h4>
    <p>sample_raster(<i>layer_name</i>, <i>band_index</i>)</p>
    <h4>Arguments</h4>
    <p>
      <i>layer_name</i> &rarr; name of the raster layer to sample<br>
      <i>band_index</i> &rarr; index of the band to sample, starting from 1<br>
    </p>
    """

    map_layer_registry = qgis.core.QgsMapLayerRegistry.instance()
    qgs_layers = map_layer_registry.mapLayersByName(layer_name)
    sampled_value = None
    if any(qgs_layers):
        qgs_layer = qgs_layers[-1]
        if qgs_layer.type() != qgis.core.QgsMapLayer.RasterLayer:
            raise Exception("Layer {} is not a raster".format(layer_name))
        own_layer = iface.mapCanvas().currentLayer()
        src_crs = own_layer.crs()
        dst_crs = qgs_layer.crs()
        provider = qgs_layer.dataProvider()
        geom = feature.geometry()
        centroid_geom = geom.centroid()
        if src_crs == dst_crs:
            pt = centroid_geom.asPoint()
        else:
            src = qgis.core.QgsCoordinateReferenceSystem(src_crs)
            dst = qgis.core.QgsCoordinateReferenceSystem(dst_crs)
            transformer = qgis.core.QgsCoordinateTransform(src, dst)
            pt = transformer.transform(centroid_geom.asPoint())
        sampled_values = provider.identify(
            pt, qgis.core.QgsRaster.IdentifyFormatValue)
        if sampled_values.isValid():
            sampled_value = sampled_values.results().get(band_index)
    else:
        raise Exception("Could not find layer {}".format(layer_name))
    return sampled_value


#FIXME - There is some error with the reprojection of the bounding box
@qgis.core.qgsfunction(args="auto", group='Expressions +')
def sample_polygon(layer_name, attribute, feature, parent):
    """
    Sample a polygon layer

    <h4>Syntax</h4>
    <p>sample_polygon(<i>layer_name</i>, <i>attribute</i>)</p>
    <h4>Arguments</h4>
    <p>
      <i>layer_name</i> &rarr; name of the polygon layer to sample<br>
      <i>attribute</i> &rarr; name of the attribute to sample<br>
    </p>
    """

    sampled_value = None
    qgs_layer = _get_layer(layer_name, qgis.core.QgsMapLayer.VectorLayer,
                           geom_type=qgis.core.QGis.Polygon)
    if qgs_layer is not None:
        attr_idx = qgs_layer.fieldNameIndex(attribute)
        bbox = feature.geometry().boundingBox()
        logger.logMessage("bbox: {}".format(bbox.asWktPolygon(),
                          level=logger.INFO))
        own_crs = _get_own_crs()
        reprojected_bbox = _reproject_bbox(own_crs, qgs_layer.crs(), bbox)
        logger.logMessage("reprojected_bbox: {}".format(
            reprojected_bbox.asWktPolygon(), level=logger.INFO))
        feature_request = qgis.core.QgsFeatureRequest()
        feature_request.setFilterRect(reprojected_bbox)
        samples = []
        for dst_feat in qgs_layer.getFeatures(feature_request):
            samples.append(dst_feat.attributes()[attr_idx])
            sampled_value = dst_feat.attributes()[attr_idx]
        logger.logMessage("feat: {}".format(feature), level=logger.INFO)
        logger.logMessage("samples: {}".format(samples), level=logger.INFO)
        logger.logMessage("********************", level=logger.INFO)
    else:
        raise Exception("Could not find layer {}".format(layer_name))
    return sampled_value

def _get_layer(layer_name, layer_type, geom_type=None):
    map_layer_registry = qgis.core.QgsMapLayerRegistry.instance()
    qgs_layers = map_layer_registry.mapLayersByName(layer_name)
    result = None
    if any(qgs_layers):
        qgs_layer = qgs_layers[-1]
        if qgs_layer.type() != layer_type:
            raise Exception("Layer {} has incorrect type".format(layer_name))
        elif geom_type is not None and qgs_layer.geometryType() != geom_type:
            raise Exception("Layer {} has incorrect geometry".format(layer_name))
        result = qgs_layer
    return result

def _reproject_points(input_crs, output_crs, *points):
    transformer = None
    if input_crs != output_crs:
        src = qgis.core.QgsCoordinateReferenceSystem(input_crs)
        dst = qgis.core.QgsCoordinateReferenceSystem(output_crs)
        transformer = qgis.core.QgsCoordinateTransform(src, dst)
    projected = []
    for pt in points:
        if transformer is None:
            projected = pt
        else:
            projected = transformer.transform(pt)
    return projected

def _get_own_crs():
    own_layer = iface.mapCanvas().currentLayer()
    return own_layer.crs()

def _reproject_bbox(src_crs, dst_crs, bbox):
    for pt in (qgis.core.QgsPoint(bbox.xMinimum(), bbox.yMinimum()),
               qgis.core.QgsPoint(bbox.xMaximum(), bbox.yMaximum())):
        reprojected = _reproject_points(src_crs, dst_crs, pt)
    new_bbox = qgis.core.QgsRectangle(*reprojected)
    return new_bbox
