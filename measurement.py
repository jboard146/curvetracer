class Measurement:
    def __init__(self):
        
        self.min=0
        self.max=10
        self.curveStep=.010 #in mV
        self.points=10
        self.traces=5
        self.R1 = 100
        self.R2 = 10000
            
        self.deviceTypeList = ['Diode','NPN','PNP','N-FET','P-FET']
        self.measureTypeList = []
        self.deviceType = ''
    
    def getDeviceTypeList(self):
        return self.deviceTypeList

    def getMeasureTypeList(self):
        return self.measureTypeList
            
    def setType(self, myTraceType):
        self.deviceType = myTraceType
        match myTraceType:
            case 'Diode':
                self.measureTypeList = ['I/V-mA', 'I/V-uA']
            case 'NPN' | 'PNP':
                self.measureTypeList = ['Ic/Vce(Ib)','Vce/Ic(Ib)', 'Ic/Vce(Vbe)', 'Ic/Vce', 'Ic/Vbe', 'Vbe/Ic', 'Ib/Vbe', 'Ic/Ib']
            case 'N-FET' | 'P-FET':
                self.measureTypeList = ['Id/Vds', 'Id/Vgs', 'Vds/Vgs(Vd)']