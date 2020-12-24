import pyvisa as visa

class Instrument():
    def __init__(self, VISA_address,model=None,serial=None,
                 command_reset='*RST',
                 command_idn='*IDN?',
                 command_meas='MEAS?',*args):

        self.model=model
        self.serial=serial
        self.command_reset=command_reset
        self.command_idn=command_idn
        self.command_meas=command_meas

        self.VISA_address=VISA_address
        self.rm=visa.ResourceManager()
        print(f'Instruments: {self.rm.list_resources()}')
        self.inst=self.rm.open_resource(self.VISA_address)

    def reset(self):
        self.inst.write(self.command_reset)

    def idn(self,*args):
        self.identifier=self.inst.query(self.command_idn)
        return self.identifier

    def send_command(self,cmd):
        self.inst.write(cmd)

    def send_query(self,cmd,*args):
        response=self.inst.query(cmd,*args)#query_ascii_values(cmd)
        try:
            response=float(response)
        except:
            response=str(response)
        return response

    def meas(self,*args):
        self.measured_value=self.send_query(cmd=self.command_meas,*args)
        return self.measured_value

class Multimeter(Instrument):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


mul=Multimeter(VISA_address='GPIB0::21::INSTR')
#mul.reset()
#print(mul.idn())
#mul.send_command('*RST')

print(mul.send_query('*idn?'))
print(mul.send_query('MEAS?'))
#print(mul.meas())


""""""
#rm = visa.ResourceManager()
#rm.list_resources()
#('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::14::INSTR')
#my_instrument = rm.open_resource('GPIB0::21::INSTR')
#print(my_instrument.query('*IDN?'))