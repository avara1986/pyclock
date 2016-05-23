# encoding: utf-8
import os
import datetime
from time import sleep

if __name__ == '__main__':
  while True:
      os.system('clear')
      print datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
      sleep(1)
