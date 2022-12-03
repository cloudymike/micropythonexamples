import machine
import esp32


class internaltempreader:

    def __init__(self, unit='C'):

        self.unit = unit



    # Assume there is just one sensor
    def get_temp(self):
        F=esp32.raw_temperature()
        if self.unit == 'F':
            temp = F
        else:
            temp = (F-32)*5/9
        return(temp)

    # For a full list of sensors get all
    def get_temp_list(self):
        tempdict = {}
        tempdict['internal'] = self.get_temp
        return(tempdict)
