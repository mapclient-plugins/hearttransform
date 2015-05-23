
'''
MAP Client Plugin Step
'''
import os

import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.hearttransformstep.configuredialog import ConfigureDialog
from mapclientplugins.hearttransformstep.definitions import LONG_AXIS,\
    SHORT_AXIS
from mapclientplugins.hearttransformstep.model.master import HeartTransformModel
from mapclientplugins.hearttransformstep.view.hearttransformwidget import HeartTransformWidget

class AffineTransformation(object):
    pass

class HeartTransformStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(HeartTransformStep, self).__init__('Heart Transform', location)
        self._configured = False # A step cannot be executed until it has been configured.
        self._category = 'Transform'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#images'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#images'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#affinetransform'))
        self._config = {}
        self._config['identifier'] = ''
        self._image_data = {}
        self._image_data[LONG_AXIS] = None
        self._image_data[SHORT_AXIS] = None
        self._view = None


    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        if self._view is None:
            model = HeartTransformModel()
            model.setLocation(os.path.join(self._location, self._config['identifier']))
            self._view = HeartTransformWidget(model)
            self._view.registerDoneExecution(self._doneExecution)

        if self._image_data[LONG_AXIS] is not None:
            self._view.setImageData(LONG_AXIS, self._image_data[LONG_AXIS])
        if self._image_data[SHORT_AXIS] is not None:
            self._view.setImageData(SHORT_AXIS, self._image_data[SHORT_AXIS])
        self._view.initialise()
        
        self._setCurrentWidget(self._view)

    def setPortData(self, index, dataIn):
        '''
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        '''
        if index == 0:
            self._image_data[LONG_AXIS] = dataIn # http://physiomeproject.org/workflow/1.0/rdf-schema#images
        else:
            self._image_data[SHORT_AXIS] = dataIn # http://physiomeproject.org/workflow/1.0/rdf-schema#images

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        # http://physiomeproject.org/workflow/1.0/rdf-schema#affinetransform
        return self._view.getAffineTransformation()

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog()
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)
        
        if dlg.exec_():
            self._config = dlg.getConfig()
        
        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()


