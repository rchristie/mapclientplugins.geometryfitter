"""
MAP Client Plugin Step
"""
import json

from PySide6 import QtGui, QtCore, QtWidgets

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.geometryfitter.configuredialog import ConfigureDialog
from mapclientplugins.geometryfitter.model.geometryfittermodel import GeometryFitterModel
from mapclientplugins.geometryfitter.view.geometryfitterwidget import GeometryFitterWidget


class GeometryFitterStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(GeometryFitterStep, self).__init__('Geometry Fitter', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Fitting'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/geometryfitter/images/fitting.png')
        # Ports:
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#exf_file_location')])
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#exf_file_location')])
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#exf_file_location')])
        self.addPort([('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#file_location'),
                      ('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                       'http://physiomeproject.org/workflow/1.0/rdf-schema#json_file_location')])
        # Port data:
        self._port0_inputZincModelFile = None  # input exf_file_location
        self._port1_inputZincDataFile = None  # input exf_file_location
        self._port2_outputZincModelFile = None  # output exf_file_location
        self._port3_outputJsonSettingsFilename = None  # output json_file_location
        # Config:
        self._config = {'identifier': '', 'reset': False, 'auto-fit': False}
        self._model = None
        self._view = None

    def _create_model(self):
        """
        Ensure self._model is constructed if not already existing.
        """
        if not self._model:
            self._model = GeometryFitterModel(self._port0_inputZincModelFile, self._port1_inputZincDataFile,
                                              self._location, self._config['identifier'], self._config['reset'])

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
        try:
            self._create_model()
            self._model.load()
            self._config['reset'] = False
            if self._config['auto-fit']:
                self._model.done()
                self._my_done_execution()
            else:
                self._view = GeometryFitterWidget(self._model)
                self._view.registerDoneExecution(self._my_done_execution)
                self._setCurrentWidget(self._view)
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def _my_done_execution(self):
        self._port2_outputZincModelFile = self._model.getOutputModelFileName()  # exf_file_location
        self._port3_outputJsonSettingsFilename = self._model.getJsonSettingsFilename()  # json_file_location
        self._view = None
        self._model = None
        self._doneExecution()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.

        :param index: Index of the port to return.
        :param dataIn: The data to set for the port at the given index.
        """
        if index == 0:
            self._port0_inputZincModelFile = dataIn  # exf_file_location
        elif index == 1:
            self._port1_inputZincDataFile = dataIn  # exf_file_location

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        if index == 2:
            return self._port2_outputZincModelFile  # exf_file_location
        if index == 3:
            return self._port3_outputJsonSettingsFilename  # json_file_location
        return None

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()

    def getAdditionalConfigFiles(self):
        self._create_model()
        return [self._model.getJsonSettingsFilename(), self._model.getJsonDisplaySettingsFilename()]
