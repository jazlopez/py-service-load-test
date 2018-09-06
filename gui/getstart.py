import PySimpleGUI as sg
import time


for i in range(1, 10):

    sg.EasyProgressMeter("Test Results Meter", i+1, 10, "Test Results Meter")

    time.sleep(i)