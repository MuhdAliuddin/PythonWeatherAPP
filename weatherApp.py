'''

    PARADIGM PROJECT (PYTHON WEATHER APP)

    Muhammad Aliuddin b. Refakaei A161177
    
'''

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

from Wheater_API import WeatherAPI


class weatherApp(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi('weatherGUI.ui', self)

        self.setStyleSheet('QMainWindow{background-color: #B7C3F3}')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.buttonTemp.clicked.connect(self.get_temp)
        self.buttonWeather.clicked.connect(self.get_weather)
        
    #return temperature results function
    def get_temp(self):

        city = self.locationEdit.text()

        weatherResults = WeatherAPI.weather_key(city)
        (current_temp, min_temp, max_temp, humid_level) = WeatherAPI.temp_results(weatherResults)

        self.textBrowser.append('\nCurrent Temperature : ' + str(current_temp) + '°')
        self.textBrowser.append('Minimum Temperature : ' + str(min_temp) + '°')
        self.textBrowser.append('Maximum Temperature : ' + str(max_temp) + '°')
        self.textBrowser.append('Humidity Level : ' + str(humid_level) + '% ')



    #return weather results function
    def get_weather(self):

        city = self.locationEdit.text()

        weatherResults = WeatherAPI.weather_key(city)
        (weather_current, weather_desc) = WeatherAPI.weather_results(weatherResults)

        self.textBrowser.append('\nCurrent weather in ' + city + ' : ' + weather_current.upper())
        self.textBrowser.append('Weather description in ' + city + ' : ' + weather_desc.upper())

        
        
    # Exception hook
    sys._excepthook = sys.excepthook

    def application_exception_hook(exctype, value, traceback):

        '''
        Error exception handling
        '''
        
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = application_exception_hook

    
app = QApplication(sys.argv)
widget = weatherApp()
widget.show()
sys.exit(app.exec_())
