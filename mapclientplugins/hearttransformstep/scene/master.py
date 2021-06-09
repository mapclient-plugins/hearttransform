'''
Created on May 23, 2015

@author: hsorby
'''
from mapclientplugins.hearttransformstep.scene.image import ImageScene
from mapclientplugins.hearttransformstep.scene.transform import TransformScene


class HeartTransformScene(object):
    '''
    classdocs
    '''

    def __init__(self, model):
        '''
        Constructor
        '''
        self._master_model = model
        self._image_scene = ImageScene(model.getImageModel())
        self._transform_scene = TransformScene(model.getTransformModel())

    def initialise(self):
        self._image_scene.initialise()
        self._transform_scene.initialise()

    def clear(self):
        self._image_scene.clear()
        self._transform_scene.clear()

    def setNodeGraphicsSize(self, value):
        self._transform_scene.setGraphicsSize(value)

    def getScene(self):
        return self._master_model.getRegion().getScene()
