'''
Created on May 23, 2015

@author: hsorby
'''
from opencmiss.zinc.context import Context
from mapclientplugins.hearttransformstep.model.transform import TransformModel
from mapclientplugins.hearttransformstep.model.image import ImageModel
import os

class HeartTransformModel(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._context = Context('hearttransform')
        self.defineStandardMaterials()
        self.defineStandardGlyphs()
        self._location = None
        self._region = None
        self._image_model = ImageModel(self._context)
        self._transform_model = TransformModel(self._context)
        
    def clear(self):
        self._image_model.clear()
        self._transform_model.clear()
        self._region = None
    
    def initialise(self):
        self._region = self._context.createRegion()
        self._image_model.initialise(self._region)
        self._transform_model.initialise(self._region)
        
    def setLocation(self, location):
        self._location = location
        
    def getRegion(self):
        return self._region
    
    def getContext(self):
        return self._context
    
    def getImageModel(self):
        return self._image_model
    
    def getTransformModel(self):
        return self._transform_model
    
    def getOrigin(self):
        return self._transform_model.getOrigin()
        
    def getTransformationMatrix(self):
        vector = self._transform_model.getAxes()
        mx = [vector[0:3], vector[3:6], vector[6:9]]
        return mx

    def save(self):
        if not os.path.exists(self._location):
            os.mkdir(self._location)
            
        string = self._transform_model.serialise()
        with open(os.path.join(self._location, 'nodes.json'), 'w') as f:
            f.write(string)
    
    def load(self):
        if os.path.exists(os.path.join(self._location, 'nodes.json')):
            with open(os.path.join(self._location, 'nodes.json')) as f:
                string = f.read()
                self._transform_model.deserialise(string)
                                  
    def getImageRegionNames(self):
        return self._image_model.getRegionNames()
        
    def setImageData(self, axis, image_data):
        self._image_model.setImageData(axis, image_data)
        
    def setImageRegionVisibility(self, region_name, state):
        self._image_model.setRegionVisibility(region_name, state)

    def getImagePlane(self, region):
        return self._image_model.getPlane(region)
    
    def setActiveMode(self, mode):
        self._transform_model.setActiveMode(mode)
    
    def setBlockSignals(self, state):
        self._transform_model.setBlockSignals(state)
        
    def registerActiveModeListener(self, listener):
        self._transform_model.registerActiveModeListener(listener)
        
    def beginHierarchicalChange(self):
        region = self._context.getDefaultRegion()
        region.beginHierarchicalChange()

    def endHierarchicalChange(self):
        region = self._context.getDefaultRegion()
        region.endHierarchicalChange()
    
    def defineStandardGlyphs(self):
        '''
        Helper method to define the standard glyphs
        '''
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()

    def defineStandardMaterials(self):
        '''
        Helper method to define the standard materials.
        '''
        material_module = self._context.getMaterialmodule()
        material_module.defineStandardMaterials()

        