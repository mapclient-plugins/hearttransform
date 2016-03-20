'''
Created on May 23, 2015

@author: hsorby
'''
from mapclientplugins.hearttransformstep.definitions import IMAGE_PLANE_GRAPHIC_NAME,\
    ELEMENT_OUTLINE_GRAPHIC_NAME
from opencmiss.zinc.field import Field
# from opencmiss.zinc.glyph import Glyph

class ImageScene(object):
    '''
    classdocs
    '''


    def __init__(self, model):
        '''
        Constructor
        '''
        '''
        Constructor
        '''
        self._model = model
        self.clear()
        
    def initialise(self):
        self._setupVisualisation()
        
    def clear(self):
        self._outline = {}
        self._image = None

    def _createTextureSurface(self, region, coordinate_field):
        scene = region.getScene()

        fm = region.getFieldmodule()
        xi = fm.findFieldByName('xi')
        scene.beginChange()
        # Create a surface graphic and set it's coordinate field
        # to the finite element coordinate field.
        graphic = scene.createGraphicsSurfaces()
        graphic.setCoordinateField(coordinate_field)
        graphic.setTextureCoordinateField(xi)
#         iso_graphic.setIsoscalarField(iso_scalar_field)
#         iso_graphic.setListIsovalues(0.0)
        graphic.setName(IMAGE_PLANE_GRAPHIC_NAME)

        scene.endChange()

        return graphic

    def _createOutline(self, region, finite_element_field):
        scene = region.getScene()

        scene.beginChange()
        # Create a surface graphic and set it's coordinate field
        # to the finite element coordinate field.
        outline = scene.createGraphicsLines()
        outline.setCoordinateField(finite_element_field)
        outline.setName(ELEMENT_OUTLINE_GRAPHIC_NAME)
        scene.endChange()

        return outline

    def _setupVisualisation(self):
        images = self._model.getImages()
        for image in images:
            name = image.getName()
            region = image.getRegion()
            coordinate_field = image.getCoordinateField()
            material = image.getMaterial()
            self._outline[name] = self._createOutline(region, coordinate_field)
            self._image = self._createTextureSurface(region, coordinate_field)
            self._image.setMaterial(material)
