'''
Created on May 23, 2015

@author: hsorby
'''
import numpy as np

from PySide2 import QtCore, QtWidgets

from mapclientplugins.hearttransformstep.view.ui_hearttransformwidget import Ui_HeartTransformWidget
from mapclientplugins.hearttransformstep.scene.master import HeartTransformScene
from mapclientplugins.hearttransformstep.definitions import BASE_PART, APEX_PART,\
    RV_PART

class HeartTransformWidget(QtWidgets.QWidget):
    '''
    classdocs
    '''


    def __init__(self, model, parent=None):
        '''
        Constructor
        '''
        super(HeartTransformWidget, self).__init__(parent)
        self._ui = Ui_HeartTransformWidget()
        self._ui.setupUi(self)
        self._ui.widgetZinc.setContext(model.getContext())
        self._ui.widgetZinc.setModel(model)
        self._callback = None
        self._master_model = model
        self._master_scene = HeartTransformScene(model)
        
        self._makeConnections()

    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        self._ui.pushButtonViewAll.clicked.connect(self._viewAllButtonClicked)
        self._ui.pushButtonHideAll.clicked.connect(self._hideAllButtonClicked)
        self._ui.listWidget.itemChanged.connect(self._itemChanged)
        self._ui.comboBoxMode.currentIndexChanged.connect(self._modeChanged)
        self._ui.spinBoxPointSize.valueChanged.connect(self._pointSizeChanged)
        self._ui.pushButtonLoad.clicked.connect(self._loadButtonClicked)
        self._ui.pushButtonSave.clicked.connect(self._saveButtonClicked)
        
        self._master_model.registerActiveModeListener(self._activeModeChanged)
        self._ui.widgetZinc.graphicsInitialized.connect(self._graphicsInitialized)
        
    def _graphicsInitialized(self):
        sceneviewer = self._ui.widgetZinc.getSceneviewer()
        scenepicker = self._ui.widgetZinc.getScenepicker()
        if sceneviewer is not None and scenepicker is not None:
            scene = self._master_scene.getScene()
            sceneviewer.setScene(scene)
            scenepicker.setScene(scene)
            sceneviewer.viewAll()
            
    def _loadButtonClicked(self):
        self._master_model.load()
    
    def _saveButtonClicked(self):
        self._master_model.save()
                
    def _pointSizeChanged(self, value):
        self._master_scene.setNodeGraphicsSize(value)
        
    def _modeChanged(self, value):
        ct = self._ui.comboBoxMode.currentText()
        mode = BASE_PART
        if ct == 'Base':
            mode = BASE_PART
        elif ct == 'Apex':
            mode = APEX_PART
        elif ct == 'RV':
            mode = RV_PART
        self._master_model.setBlockSignals(True)
        self._master_model.setActiveMode(mode)
        self._master_model.setBlockSignals(False)
        
    def _activeModeChanged(self, mode):
        self._ui.comboBoxMode.blockSignals(True)
        if mode == APEX_PART:
            self._ui.comboBoxMode.setCurrentIndex(0)
        elif mode == BASE_PART:
            self._ui.comboBoxMode.setCurrentIndex(1)
        elif mode == RV_PART:
            self._ui.comboBoxMode.setCurrentIndex(2)
        self._ui.comboBoxMode.blockSignals(False)
        
    def _itemChanged(self, item):
        region = item.text()
        self._master_model.setImageRegionVisibility(region, item.checkState() == QtCore.Qt.Checked)
                
    def _viewAllButtonClicked(self):
        self._master_model.beginHierarchicalChange()
        self._ui.widgetZinc.viewAll()
        for index in range(self._ui.listWidget.count()):
            item = self._ui.listWidget.item(index)
            item.setCheckState(QtCore.Qt.Checked)
        self._master_model.endHierarchicalChange()

    def _hideAllButtonClicked(self):
        self._master_model.beginHierarchicalChange()
        for index in range(self._ui.listWidget.count()):
            item = self._ui.listWidget.item(index)
            item.setCheckState(QtCore.Qt.Unchecked)
        self._master_model.endHierarchicalChange()

    def _setupUi(self):
        self._ui.listWidget.clear()
        region_names = self._master_model.getImageRegionNames()
        
        for region_name in region_names:
            item = QtWidgets.QListWidgetItem(self._ui.listWidget)
            item.setText(region_name)
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | item.flags())
            item.setCheckState(QtCore.Qt.Checked)
        
    def clear(self):
        self._master_model.clear()
        self._master_scene.clear()

    def initialise(self):
        self._master_model.initialise()
        self._master_scene.initialise()
        self._setupUi()
        self._graphicsInitialized()
        
    def setImageData(self, axis, image_data):
        self._master_model.setImageData(axis, image_data)
    
    def registerDoneExecution(self, callback):
        self._callback = callback
        
    def _doneButtonClicked(self):
        self._callback()
        
    def getAffineTransformation(self):
        t = self._master_model.getOrigin()
        R = self._master_model.getTransformationMatrix()
        print(t)
        print(R)
        return AffineTransformation(R, t)
        
        
class AffineTransformation(object):
    
    transformType = 'rigid'
    
    def __init__(self, R, t):
        self._R = R
        self._t = t
        
    def getRotationMatrix(self):
        return self._R
    
    def getTranslationVector(self):
        return self._t
    
    def getT(self):
        return np.array(self._t)
    
    def getP(self):
        return np.array(self._R)
    
    def __str__(self):
        r = str(self._R)
        t = str(self._t)
        
        string = 'mx: {0}\nt: {1}'.format(r, t)
        return string
    