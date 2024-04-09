def tester(psu):
    psu = Powersupply(PSU_PORT)
    psu.connect()
    print(psu.info)
    print(psu.options)
    

    psu.setCurrent(1, 1.123567)
    psu.setVoltage(1, 12.345678)
    psu.outputEnable(1)
    psu.measure(1)

    psu.outputDisable(1)

    print(psu.ch1voltage)
    print(psu.ch1current)
    print(psu.ch1power)

    psu.disconnect()