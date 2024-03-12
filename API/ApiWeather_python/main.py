import sys
from datetime import datetime
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtUiTools import QUiLoader
import string
import requests
import json
import datetime




class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.btn_search.clicked.connect(self.search)

        
        

    def search(self):
        city = self.ui.search_box.text()
        url = f"https://api.weatherbit.io/v2.0/forecast/daily?&city={city}&key=2effe1f9f06e40cc8ef77eb5be376022"
         
        response = requests.get(url)
        data = json.loads(response.text)
        
        self.ui.lbl_namecity.setText(str(data["city_name"]))
        self.ui.lbl_nowtemp.setText(str(data["data"][0]["temp"])+"°C")
        self.ui.lbl_description.setText(str(data["data"][0]['weather']['description']))
        self.ui.lbl_temp2.setText(str(data["data"][1]["temp"])+"°C")
        self.ui.lbl_temp3.setText(str(data["data"][2]["temp"])+"°C")
        self.ui.lbl_temp4.setText(str(data["data"][3]["temp"])+"°C")
        self.ui.lbl_windspd.setText("wind:"+str(+data["data"][0]["wind_spd"])+"km/h")
        self.ui.lbl_windspd1.setText(str(data["data"][1]["wind_spd"])+"km/h")
        self.ui.lbl_windspd2.setText(str(data["data"][2]["wind_spd"])+"km/h")
        self.ui.lbl_windspd3.setText(str(data["data"][3]["wind_spd"])+"km/h")
        today = datetime.date.today()
        day1 = today + datetime.timedelta(days=1)
        day1 = day1.strftime("%A")
        day2 = today + datetime.timedelta(days=2)
        day2 = day2.strftime("%A")
        day3 = today + datetime.timedelta(days=3)
        day3 = day3.strftime("%A")
        self.ui.lbl_day1.setText(day1)
        self.ui.lbl_day2.setText(day2)
        self.ui.lbl_day3.setText(day3)

       
        weather = data["data"][0]["weather"]["description"]
        print(weather)

        if "few clouds" in weather: 
            img = "icon\partlycloudy.png"
        elif "Mix snow/rain" in weather: 
            img = "icon\mix snow_rain.png"
        elif "rain" in weather: 
            img = "icon\rain.png"
        elif "snow" in weather: 
            img = "icon\snow.png"
        elif "sun" in weather: 
            img = "icon\sun.png"
        elif "Clear" in weather: 
            img = "icon\clouds.png"
        elif "rainfall" in weather: 
            img = "icon\rainfall.png"
        elif "storm" in weather: 
            img = "icon\storm.png"
        elif "Light shower rain" in weather: 
            img = "icon\raincloud.png"
        else : img = "icon\clouds.png"
        
        pixmap = QPixmap(img)
        self.ui.lbl_tempnow.setPixmap(pixmap)




        


if __name__ == "__main__":
    app = QApplication([])
    window = mainwindow()
    sys.exit(app.exec_())
