import os
from selenium import webdriver
from pathlib import Path

class Firefox():

    def __init__(self):
      self.path = Path(__file__).parent.absolute()



    def FireFoxBrowser(self):
        print(self.path)
        return webdriver.Firefox(executable_path=str(self.path) + "/geckodriver")
