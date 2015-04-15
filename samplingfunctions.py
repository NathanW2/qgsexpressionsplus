"""
QGIS expression functions for sampling raster and vector layers.
"""

import qgis.core
import qgis.gui
import qgis.utils


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
        iface = qgis.utils.iface
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


# TODO - deal with coordinate transformations
@qgis.core.qgsfunction(args="auto", group='Custom')
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

    map_layer_registry = qgis.core.QgsMapLayerRegistry.instance()
    qgs_layers = map_layer_registry.mapLayersByName(layer_name)
    sampled_value = None
    if any(qgs_layers):
        qgs_layer = qgs_layers[-1]
        if qgs_layer.type() != qgis.core.QgsMapLayer.VectorLayer:
            raise Exception("Layer {} is not a vector".format(layer_name))
        elif qgs_layer.geometryType() != qgis.core.QGis.Polygon:
            raise Exception("Layer {} is not a polygon".format(layer_name))
        geom = feature.geometry()
        centroid_geom = geom.centroid()
        # implement the actual sampling of the value
    else:
        raise Exception("Could not find layer {}".format(layer_name))
    return sampled_value
