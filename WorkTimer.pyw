import sys, os
if sys.executable.endswith("pythonw.exe"):
  sys.stdout = open(os.devnull, "w")
  sys.stderr = open(os.path.join(os.getenv("TEMP"), "stderr-"+os.path.basename(sys.argv[0])), "w")

import time
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty

class WorkTimerGrid(GridLayout):
    mainLabel = ObjectProperty(None)
    

    def start(self):
        if self.mainLabel.text == "Press Start":
            with open("Work_logs.txt","a+") as file:
                self.mainLabel.text = "Starting time : "+ str(time.asctime())
                file.write("Start:{0}\n".format(str(time.asctime())))
        
    def stop(self):
        if self.mainLabel.text != "Press Start":
            with open("Work_logs.txt","a+") as file:
                self.mainLabel.text = "Press Start"
                file.write("Stop:{0}\n".format(str(time.asctime())))
        
class WorkTimerApp(App):
    def build(self):
        return WorkTimerGrid()

    def stop(self, *largs):
        f = open("Work_logs.txt","r")
        lines = f.read().splitlines()
        last_line = lines[-1]
        f.close()

        if last_line[0:4] != "Stop":
            f = open("Work_logs.txt","a")
            f.write("Stop:{0}\n".format(str(time.asctime())))
            f.close()
                
if __name__ == '__main__':
    WorkTimerApp().run()