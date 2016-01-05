import imp
import sys

ok = imp.load_source('ok','../../lib/ok/ok.py')

import constants

class OpalKelly:
	
    def __init__(self):
	self.xem = ok.okCFrontPanel()
	self.pll = ok.PLL22393()
	self.activationFlag = False

    def openDevice(self):
        errormsg = self.xem.OpenBySerial("")
        if (self.xem.NoError == errormsg):
            self.activationFlag = True
        return errormsg

    def configurePLL(self):
        if (self.activationFlag):
            self.xem.GetPLL22393Configuration(self.pll)
            self.pll.SetReference(48.0)
            self.pll.SetPLLParameters(0, 400, 48, True)
            self.pll.SetOutputSource(0, ok.PLL22393.ClkSrc_PLL0_0)
            self.pll.SetOutputDivider(0, 4)
            self.pll.SetOutputEnable(0, True)
            self.xem.SetPLL22393Configuration(self.pll)
            return self.pll.GetPLLFrequency(0)
        else :
            pass

    def loadFile(self, filename):
        if (self.activationFlag):
            output = self.xem.ConfigureFPGA(filename)
        else :
            pass

    def setWireIn(self,addr,data):
        self.xem.SetWireInValue(addr,data)
    
    def updateWireIns(self):
        self.xem.updateWireIns()

    def activateTriggerIn(self,addr,bit):
        self.xem.ActivateTriggerIn(addr,bit)

    def tryConfiguration(self):
        self.xem.SetWireInValue(constants.OK_ADDR_COMMAND, constants.OK_STORE_1)
        self.xem.SetWireInValue(constants.OK_ADDR_DATA, 0x55)
        self.xem.UpdateWireIns()

        self.xem.ActivateTriggerIn(constants.OK_ADDR_TRIGGER, constants.OK_DATA_TRIGGER)

        self.xem.SetWireInValue(0x00,0x02)
        self.xem.SetWireInValue(0x01,0x00)
        self.xem.UpdateWireIns()

        self.xem.ActivateTriggerIn(0x40,0x00)

    def tryDisplay1(self):
        self.xem.SetWireInValue(0x00,0x03)
        self.xem.SetWireInValue(0x01,0x01)
        self.xem.UpdateWireIns()
        self.xem.ActivateTriggerIn(0x40,0x00)
    
    def tryDisplay2(self):
        self.xem.SetWireInValue(0x00,0x03)
        self.xem.SetWireInValue(0x01,0x02)
        self.xem.UpdateWireIns()
        self.xem.ActivateTriggerIn(0x40,0x00)

