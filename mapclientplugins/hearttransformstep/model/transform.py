'''
Created on May 23, 2015

@author: hsorby
'''
from cmlibs.zinc.field import Field
from cmlibs.zinc.status import OK
from cmlibs.utils.zinc.field import create_field_coordinates

from mapclientplugins.hearttransformstep.definitions import SELECTION_PART, \
    APEX_PART, BASE_PART, DEPENDENT_PART, RV_PART
import json


class TransformModel(object):
    '''
    classdocs
    '''

    def __init__(self, context):
        '''
        Constructor
        '''
        self._context = context
        self._parts = [SELECTION_PART, APEX_PART, BASE_PART, RV_PART, DEPENDENT_PART]
        self.clear()

    def clear(self):
        self._active_mode_listener = None
        self._show_origin_listener = None
        self._block_signals = False
        self._axes_field = None
        self._switch_field = None
        self._coordinate_field = None
        self._fields = {}
        for part in self._parts:
            self._fields[part] = {}
            self._fields[part]['nodeset_group'] = None
            self._fields[part]['group'] = None

        self._region = None

    #         if hasattr(self, '_region'):
    #             fieldmodule = self._region.getFieldmodule()
    #             nodeset = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
    #             nodeset.destroyAllNodes()
    #             scene = self._region.getScene()
    #             scene.removeAllGraphics()
    #             it = fieldmodule.createFielditerator()
    #             field = it.next()
    #             while field.isValid():
    #                 if field.isManaged():
    #                     field.setManaged(False)
    #                     # must reset iterator
    #                     it = fieldmodule.createFielditerator()
    #                 field = it.next()
    #
    #             self._active_group = None
    #             self._coordinate_field = None
    # #             self._selection_group = None
    # #             self._selection_group_field = None
    #             self._context.getDefaultRegion().removeChild(self._region)
    #             self._region = None

    def initialise(self, region):
        self._setupRegion(region)
        self._active_group = self._fields[APEX_PART]['nodeset_group']

    def serialise(self):
        data = {BASE_PART: [], APEX_PART: [], RV_PART: []}
        fieldmodule = self._region.getFieldmodule()
        nodeset = fieldmodule.findNodesetByName('nodes')
        it = nodeset.createNodeiterator()
        node = it.next()
        while node.isValid():
            pos = self.getNodeLocation(node)
            for part in [APEX_PART, BASE_PART, RV_PART]:
                if self._fields[part]['nodeset_group'].containsNode(node):
                    data[part] = pos
                    break

            node = it.next()
        return json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialise(self, string):
        data = json.loads(string)
        self._region.beginChange()
        self.setBlockSignals(True)
        active_group = self._active_group
        for part in [BASE_PART, APEX_PART, RV_PART]:
            self.setActiveMode(part)
            pos = data[part]
            if pos:
                if self.doesActiveModeHaveNode():
                    node = self.getActiveModeNode()
                else:
                    node = self.createNode()
                self.setNodeLocation(node, pos)
                self.assignToActiveMode(node)

        mode = self.getMode(active_group)
        self.setActiveMode(mode)
        self.setBlockSignals(False)
        self._region.endChange()

    def getMode(self, group):
        for part in self._parts:
            if self._fields[part]['nodeset_group'] == group:
                return part

    def getContext(self):
        return self._context

    def getRegion(self):
        return self._region

    def getCoordinateField(self):
        return self._coordinate_field

    def setBlockSignals(self, state):
        self._block_signals = state

    def setActiveMode(self, mode):
        self._active_group = self._fields[mode]['nodeset_group']
        if not self._block_signals:
            self._active_mode_listener(mode)

    def assignToActiveMode(self, node):
        if self._fields[SELECTION_PART]['nodeset_group'].containsNode(node):
            self._fields[SELECTION_PART]['nodeset_group'].removeNode(node)
        self._active_group.addNode(node)

    def setSelected(self, node):
        for part in self._parts:
            if self._fields[part]['nodeset_group'].containsNode(node):
                self._fields[part]['nodeset_group'].removeNode(node)
        self._fields[SELECTION_PART]['nodeset_group'].addNode(node)

    def doesActiveModeHaveNode(self):
        nodeset = self._active_group
        it = nodeset.createNodeiterator()
        node = it.next()
        return node.isValid()

    def getActiveModeNode(self):
        nodeset = self._active_group
        it = nodeset.createNodeiterator()
        node = it.next()
        return node

    def getNodeMode(self, node):
        for part in self._parts:
            if self._fields[part]['nodeset_group'].containsNode(node):
                return part

        return None

    def registerActiveModeListener(self, listener):
        self._active_mode_listener = listener

    def registerShowOriginListener(self, listener):
        self._show_origin_listener = listener

    def getNodeLocation(self, node):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        fieldmodule.beginChange()
        fieldcache.setNode(node)
        result, location = self._coordinate_field.evaluateReal(fieldcache, 3)
        fieldmodule.endChange()

        if result == OK:
            return location

        return None

    def setNodeLocation(self, node, location):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        fieldmodule.beginChange()
        fieldcache.setNode(node)
        self._coordinate_field.assignReal(fieldcache, location)
        # Update the axis location as well
        mode = self.getMode(self._active_group)
        self._fields[mode]['coord'].assignReal(fieldcache, location)
        fieldmodule.endChange()

    def createNode(self):
        '''
        Create a node with the models coordinate field.
        '''
        fieldmodule = self._region.getFieldmodule()
        fieldmodule.beginChange()

        nodeset = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
        template = nodeset.createNodetemplate()
        template.defineField(self._coordinate_field)

        scene = self._region.getScene()
        selection_field = scene.getSelectionField()
        if not selection_field.isValid():
            scene.setSelectionField(self._fields[SELECTION_PART]['group'])

        self._fields[SELECTION_PART]['group'].clear()

        node = nodeset.createNode(-1, template)
        self._fields[SELECTION_PART]['nodeset_group'].addNode(node)

        fieldmodule.endChange()

        return node

    def getGroupField(self, group):
        return self._fields[group]['group']

    def getOriginField(self):
        return self._origin_field

    def getOrigin(self):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        result, location = self._origin_field.evaluateReal(fieldcache, 3)

        if result == OK:
            return location

        return None

    def getAxesField(self):
        return self._axes_field

    def getAxes(self):
        fieldmodule = self._region.getFieldmodule()
        fieldcache = fieldmodule.createFieldcache()
        result, axes = self._axes_field.evaluateReal(fieldcache, 9)

        if result == OK:
            return axes

        return None

    def _setupRegion(self, region):
        self._region = region.createChild('surfaces')  # self._context.getDefaultRegion().createChild('surfaces')
        fieldmodule = self._region.getFieldmodule()
        nodeset = fieldmodule.findNodesetByName('nodes')
        self._coordinate_field = create_field_coordinates(fieldmodule, managed=True)

        base_field = fieldmodule.createFieldConstant([1.0, 0.0, 0.0])
        apex_field = fieldmodule.createFieldConstant([0.0, 1.0, 0.0])
        rv_field = fieldmodule.createFieldConstant([0.0, 0.0, 1.0])
        const_3 = fieldmodule.createFieldConstant(3.0)

        dir_x_field = apex_field - base_field
        temp2 = fieldmodule.createFieldDivide(dir_x_field, const_3)
        self._origin_field = base_field + temp2

        p1 = fieldmodule.createFieldDotProduct(base_field, dir_x_field)
        p2 = fieldmodule.createFieldDotProduct(rv_field, dir_x_field)
        p3 = fieldmodule.createFieldDotProduct(dir_x_field, dir_x_field)

        perp_t = fieldmodule.createFieldDivide((p1 - p2), p3)  # put missing minus sign in next equation
        lr_perp = base_field - perp_t * dir_x_field  # minus sign from equation above appears here
        dir_y_field = rv_field - lr_perp

        temp4 = apex_field - rv_field
        mag = fieldmodule.createFieldMagnitude(temp4)
        tol = fieldmodule.createFieldConstant(0.00001)
        self._switch_field = fieldmodule.createFieldGreaterThan(mag, tol)

        dir_z_field = fieldmodule.createFieldCrossProduct(dir_x_field, dir_y_field)

        dir_x_norm_field = fieldmodule.createFieldNormalise(dir_x_field)
        dir_y_norm_field = fieldmodule.createFieldNormalise(dir_y_field)
        dir_z_norm_field = fieldmodule.createFieldNormalise(dir_z_field)
        self._axes_field = fieldmodule.createFieldConcatenate([dir_x_norm_field, dir_y_norm_field, dir_z_norm_field])

        self._fields[BASE_PART]['coord'] = base_field
        self._fields[APEX_PART]['coord'] = apex_field
        self._fields[RV_PART]['coord'] = rv_field
        for part in self._parts:
            self._fields[part]['group'] = fieldmodule.createFieldGroup()
            self._fields[part]['nodeset_group'] = self._fields[part]['group'].createNodesetGroup(nodeset)
