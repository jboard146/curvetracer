import time
import argparse
#import numpy as np
#import pyvisa
from powersupply import Powersupply
from measurement import Measurement

PSU_PORT = 'TCPIP0::192.168.1.152::INSTR'
run_tester = False



def curvetrace(m):
    print()
    print("Rb/Rg/R1: ", m.R1)
    print("Re/Rc/R2: ", m.R2)
    print("Min: ", m.min)
    print("Max: ", m.max)
    print("V between curves: ", m.curveStep)
    print("Points to record: ", m.points)
    print("Num of Traces: ", m.traces)
    print()
    
    
    # Make Sure we can connect to DP832
    try: 
        psu = Powersupply(PSU_PORT)
        psu.connect()
        print(psu.info)
    except:
        print("Cant Connect to Powersupply!")
        return
        
    
    # Make Sure Channels are OFF
        psu.outputDisable(1)
        psu.outputDisable(2)
    # Set Voltage and Current to 0
        psu.setCurrent(1, 0)
        psu.setVoltage(1, 0)
        psu.setCurrent(2, 0)
        psu.setVoltage(2, 0)
    
    # Loop to step through each trace
    t=0 
    loopStepV=m.min
    for t in range(m.traces):
        print()
        print("Trace: ", t)
        loopStepV = loopStepV + m.curveStep
        print("Step Voltage: ", loopStepV)
        if loopStepV <= m.max:
                   
            # Loop to record each trace
            p=0
            for p in range(m.points):
                print("Point: ", p)
            
        
        else:
            print("Max Voltage Reached")
            
            
if __name__ == "__main__":
    #argparser()
    myMeasure = Measurement()
    print(myMeasure.getDeviceTypeList())
    myMeasure.setType('NPN')
    print(myMeasure.getMeasureTypeList())
    curvetrace(myMeasure)