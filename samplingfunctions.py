"""
QGIS expression functions for sampling raster and vector layers.
"""

import qgis.core
import qgis.gui
from qgis.utils import iface


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

    sampled_value = None
    qgs_layer = _get_layer(layer_name, qgis.core.QgsMapLayer.RasterLayer)
    if qgs_layer is not None:
        own_crs = _get_own_crs()
        dst_crs = qgs_layer.crs()
        centroid = feature.geometry().centroid().asPoint()
        point = _reproject_point(own_crs, dst_crs, centroid)
        provider = qgs_layer.dataProvider()
        sampled_values = provider.identify(
            point, qgis.core.QgsRaster.IdentifyFormatValue)
        if sampled_values.isValid():
            sampled_value = sampled_values.results().get(band_index)
    else:
        raise Exception("Could not find layer {}".format(layer_name))
    return sampled_value


@qgis.core.qgsfunction(args="auto", group='Expressions +', register=False)
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
        bbox = feature.geometry().centroid().boundingBox()
        own_crs = _get_own_crs()
        reprojected_bbox = _reproject_bbox(own_crs, qgs_layer.crs(), bbox)
        feature_request = qgis.core.QgsFeatureRequest()
        feature_request.setFilterRect(reprojected_bbox)
        for dst_feat in qgs_layer.getFeatures(feature_request):
            sampled_value = dst_feat.attributes()[attr_idx]
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

def _reproject_point(input_crs, output_crs, point):
    transformer = None
    if input_crs != output_crs:
        src = qgis.core.QgsCoordinateReferenceSystem(input_crs)
        dst = qgis.core.QgsCoordinateReferenceSystem(output_crs)
        transformer = qgis.core.QgsCoordinateTransform(src, dst)
    if transformer is None:
        projected = point
    else:
        projected = transformer.transform(point)
    return projected

def _get_own_crs():
    own_layer = iface.mapCanvas().currentLayer()
    return own_layer.crs()

def _reproject_bbox(src_crs, dst_crs, bbox):
    new_pts = []
    for pt in (qgis.core.QgsPoint(bbox.xMinimum(), bbox.yMinimum()),
               qgis.core.QgsPoint(bbox.xMaximum(), bbox.yMaximum())):
        new_pts.append(_reproject_point(src_crs, dst_crs, pt))
    new_bbox = qgis.core.QgsRectangle(*new_pts)
    return new_bbox
