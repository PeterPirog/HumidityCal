import pyvisa

class Instrument:
    def __init__(self, VISA_address):
        self.VISA_address=VISA_address
        self.resource_manager=pyvisa.ResourceManager()
        self.instrument=self.resource_manager.open_resource(self.VISA_address)

class Multimeter(Instrument):
    def __init__(self,VISA_address):
        super.__init__(VISA_address)



mul=Multimeter(VISA_address='GPIB0::21::INSTR')

print(mul.instrument.query("*IDN?"))