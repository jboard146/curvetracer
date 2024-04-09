import pyvisa

class Powersupply:

    def __init__(self, port):
           
        self.connected = False
        self.port = port
        self.resource = None
        self.info = []
        self.mfr = ''
        self.name = ''
        self.sn = ''
        self.ver = ''
        self.options = []
        self.instrument = None
        
        
    def connect(self):
        # Connect to .so or .dll for visa communications
        # ASSumens that there is the NI visa driver or linux equivelent installed
        self.resource = pyvisa.ResourceManager()
        print(self.resource)
        
        # Open our Port
        # Tested only with TCP/IP Connection
        self.instrument = self.resource.open_resource(self.port)
        self.connected = True
        
        # Make Sure we have \n as the RW termination
        self.instrument.read_termination = '\n'
        self.instrument.write_termination = '\n'
        
        # Get info about our Rigol DP832
        self.getInfo()
        self.getOptions()
        
    def disconnect(self):
        self.instrument.close()
        self.connected = False
        
    def status(self):
        pass
    
    def getInfo(self):
        x = self.instrument.query('*IDN?').strip()
        self.info = x.split(',')
        self.mfr = self.info[0]
        self.name = self.info[1]
        self.sn = self.info[2]
        self.ver = self.info[3]
    
    def getOptions(self):
        y = self.instrument.query('*OPT?').strip()
        self.options = y.split(',')
        
    def setVoltage(self, channel, voltage):
        # ':INST CH1' /*Select CH1*/
        # ':VOLT 12' /*Set the voltage of CH1 to 12V*/
        cmd1 = ':INST CH' + str(channel)
        print("Select Channel CMD: ", cmd1)
        err1 = self.instrument.write(cmd1)
        print("Error Code:", err1)
        cmd2 = ':VOLT ' + str(voltage)
        print("Set Voltage CMD", cmd2)
        err2 = self.instrument.write(cmd2)
        print("Error Code:", err2)
        
    
    def setCurrent(self,channel, current):
        # You can pass > 3 decmial places, but all you get is 3
        # ':INST CH1' /*Select CH1*/
        # ':CURR 5' /*Set the current of CH1 to 5A*/
        cmd1 = ':INST CH' + str(channel)
        print("Select Channel CMD: ", cmd1)
        err1 = self.instrument.write(cmd1)
        print("Error Code:", err1)
        cmd2 = ':CURR ' + str(current)
        print("Set Voltage CMD", cmd2)
        err2 = self.instrument.write(cmd2) 
        print("Error Code:", err2)
    
    def getMode(self, channel):
        cmd = ':OUTP:MODE? CH' + str(channel)
        mode = self.instrument.query(cmd).strip()
        if channel == 1:
            self.ch1mode = mode
        elif channel == 2:
            self.ch2mode = mode
        elif channel == 3:
            self.ch3mode = mode
    
    def measure(self, channel):
        #Voltage and Current return 4 decmial places ex 1.2345
        
        # ':MEAS:ALL? CH1'
        cmd = ':MEAS:ALL? CH' + str(channel)
        print(cmd)
        #err = self.instrument.write(cmd)
        vals = self.instrument.query(cmd).strip()
        val = vals.split(',')
        print(vals)
        print(val)
        if channel == 1:
            self.ch1voltage = float(val[0])
            self.ch1current = float(val[1])
            self.ch1power = float(val[2])
        elif channel == 2:
            self.ch2voltage = float(val[0])
            self.ch2current = float(val[1])
            self.ch2power = float(val[2])
        elif channel == 3:
            self.ch3voltage = float(val[0])
            self.ch3current = float(val[1])
            self.ch3power = float(val[2])
        
        
    def outputEnable(self, channel):
        if self.connected == True:
            # ':OUTP CH1, ON'
            # Very important to have a space after the comma
            cmd = ':OUTP CH' + str(channel) + ', ON'
            print(cmd)
            err = self.instrument.write(cmd)
            cmd2 = ':OUTP? CH' + str(channel)
            err2 = self.instrument.query(cmd2).strip()
            print("Output? ", err2)   
        else: 
            return(1)
        
    def outputDisable(self, channel):
        if self.connected == True:
            # ':OUTP CH1, OFF'
            # Very important to have a space after the comma
            cmd = ':OUTP CH' + str(channel) + ', OFF'
            print(cmd)
            err = self.instrument.write(cmd)
            cmd2 = ':OUTP? CH' + str(channel)
            err2 = self.instrument.query(cmd2).strip()
            print("Output? ", err2)  
        else: 
            return(1)
        
    def getI(self):
        pass
    
    
