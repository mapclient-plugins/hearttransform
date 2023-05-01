'''
Created on May 23, 2015

@author: hsorby
'''
from cmlibs.zinc.field import Field
from cmlibs.zinc.glyph import Glyph
from mapclientplugins.hearttransformstep.definitions import SELECTION_PART, \
    BASE_PART, APEX_PART, RV_PART


class TransformScene(object):
    '''
    classdocs
    '''

    def __init__(self, model):
        '''
        Constructor
        '''
        self._model = model
        self.clear()

    def clear(self):
        self._selection_graphics = None
        self._base_graphics = None
        self._apex_graphics = None
        self._rv_graphics = None
        self._coordinate_graphics = None

    def initialise(self):
        self._setupVisualisation()

    def setGraphicsSize(self, size):
        region = self._model.getRegion()
        scene = region.getScene()
        scene.beginChange()
        attributes = self._selection_graphics.getGraphicspointattributes()
        attributes.setBaseSize(size)
        attributes = self._base_graphics.getGraphicspointattributes()
        attributes.setBaseSize(size)
        attributes = self._apex_graphics.getGraphicspointattributes()
        attributes.setBaseSize(size)
        attributes = self._rv_graphics.getGraphicspointattributes()
        attributes.setBaseSize(size)
        attributes = self._coordinate_graphics.getGraphicspointattributes()
        attributes.setBaseSize(size)
        scene.endChange()

    def _setupVisualisation(self):
        coordinate_field = self._model.getCoordinateField()
        region = self._model.getRegion()
        scene = region.getScene()
        materialmodule = scene.getMaterialmodule()
        yellow = materialmodule.findMaterialByName('yellow')
        red = materialmodule.findMaterialByName('red')
        green = materialmodule.findMaterialByName('green')
        orange = materialmodule.findMaterialByName('orange')
        self._selection_graphics = self._createGraphics(scene, coordinate_field, yellow, SELECTION_PART,
                                                        gen_text_field=False)
        self._base_graphics = self._createGraphics(scene, coordinate_field, red, BASE_PART)
        self._apex_graphics = self._createGraphics(scene, coordinate_field, green, APEX_PART)
        self._rv_graphics = self._createGraphics(scene, coordinate_field, orange, RV_PART)
        self._createPointGraphics()

    def _createPointGraphics(self):
        region = self._model.getRegion()
        scene = region.getScene()
        materialmodule = scene.getMaterialmodule()
        brown = materialmodule.findMaterialByName('brown')
        origin_field = self._model.getOriginField()
        axes_field = self._model.getAxesField()
        scene.beginChange()
        # Create a surface graphic and set it's coordinate field
        # to the finite element coordinate field.
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_POINT)
        graphic.setCoordinateField(origin_field)
        graphic.setMaterial(brown)
        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_SOLID_XYZ)
        attributes.setBaseSize(1.0)
        attributes.setScaleFactors([10.0, 10.0, 10.0])
        #         attributes.setLabelField(origin_field)
        attributes.setOrientationScaleField(axes_field)
        #         surface = scene.createGraphicsSurfaces()
        #         surface.setCoordinateField(finite_element_field)
        scene.endChange()
        self._coordinate_graphics = graphic

    def _createGraphics(self, scene, finite_element_field, material, part, gen_text_field=True):
        subgroup_field = self._model.getGroupField(part)
        scene.beginChange()
        # Create a surface graphic and set it's coordinate field
        # to the finite element coordinate field.
        graphic = scene.createGraphicsPoints()
        graphic.setFieldDomainType(Field.DOMAIN_TYPE_NODES)
        graphic.setCoordinateField(finite_element_field)
        graphic.setMaterial(material)
        graphic.setSelectedMaterial(material)
        graphic.setSubgroupField(subgroup_field)
        attributes = graphic.getGraphicspointattributes()
        attributes.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
        attributes.setBaseSize([1.0])
        if gen_text_field:
            attributes.setLabelText(1, part)
            attributes.setLabelOffset(1.0)
        scene.endChange()

        return graphic
