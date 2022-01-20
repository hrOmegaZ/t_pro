'''Write an interactive program that asks the user what information they would like to analyze, whether they want for the entire year or an individual month.
Display the output on a line graph.
- address the user by name throughout the program
- data category choices must include:  Tmax, Tmin, wind speed, humidity, rain totals
- the graph should use labels for axes, a different color line for each station, and a legend to map the colors to the stations'''

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ALTUm = []
BEAVm = []
NRMNm = []
TISHm = []
TULNm = []

ALTUWSmx = []
ALTUWSmn = []

BEAVWSmx = []
BEAVWSmn = []

NRMNWSmx = []
NRMNWSmn = []

TISHWSmx = []
TISHWSmn = []

TULNWSmx = []
TULNWSmn = []

ALTUh = []
BEAVh = []
NRMNh = []
TISHh = []
TULNh = []

ALTUr = []
BEAVr = []
NRMNr = []
TISHr = []
TULNr = []

ALTU = []
BEAV = []
NRMN = []
TISH = []
TULN = []

channel = ['ALTU','BEAV','NRMN','TISH','TULN']

with open("2016VizData.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        for x in range(len(channel)):
            #Temp Max and Min
            if float(row['TMAX']) > 200 or float(row['TMAX']) < -200:
                pass
            else:
                if row['STID'] == channel[x]:
                    if x == 0:
                        ALTUm.append((float(row["TMAX"])))
                    elif x == 1:
                        BEAVm.append((float(row["TMAX"])))
                    elif x == 2:
                        NRMNm.append((float(row["TMAX"])))
                    elif x == 3:
                        TISHm.append((float(row["TMAX"])))
                    else:
                        TULNm.append((float(row["TMAX"])))
            if float(row['TMIN']) > 200 or float(row['TMIN']) < -200:
                pass
            else:
                if row['STID'] == channel[x]:
                    if x == 0:
                        ALTU.append((float(row["TMIN"])))
                    elif x == 1:
                        BEAV.append((float(row["TMIN"])))
                    elif x == 2:
                        NRMN.append((float(row["TMIN"])))
                    elif x == 3:
                        TISH.append((float(row["TMIN"])))
                    elif x == 4:
                        TULN.append((float(row["TMIN"])))
            # Wind Speed Max and Min
            if float(row['WSMX']) > 200 or float(row['WSMX']) < -200:
                pass
            else:
                if row['STID'] == channel[x]:
                    if x == 0:
                        ALTUWSmx.append((float(row["WSMX"])))
                    elif x == 1:
                        BEAVWSmx.append((float(row["WSMX"])))
                    elif x == 2:
                        NRMNWSmx.append((float(row["WSMX"])))
                    elif x == 3:
                        TISHWSmx.append((float(row["WSMX"])))
                    elif x == 4:
                        TULNWSmx.append((float(row["WSMX"])))
            if float(row['WSMN']) > 200 or float(row['WSMN']) < -200:
                pass
            else:
                if row['STID'] == channel[x]:
                    if x == 0:
                        ALTUWSmn.append((float(row["WSMN"])))
                    elif x == 1:
                        BEAVWSmn.append((float(row["WSMN"])))
                    elif x == 2:
                        NRMNWSmn.append((float(row["WSMN"])))
                    elif x == 3:
                        TISHWSmn.append((float(row["WSMN"])))
                    elif x == 4:
                        TULNWSmn.append((float(row["WSMN"])))
            # Humidity
            if float(row['HAVG']) > 200 or float(row['HAVG']) < -200:
                pass
            else:
                if row['STID'] == channel[x]:
                    if x == 0:
                        ALTUh.append((float(row["HAVG"])))
                    elif x == 1:
                        BEAVh.append((float(row["HAVG"])))
                    elif x == 2:
                        NRMNh.append((float(row["HAVG"])))
                    elif x == 3:
                        TISHh.append((float(row["HAVG"])))
                    elif x == 4:
                        TULNh.append((float(row["HAVG"])))
            # Rain 
            if float(row['RAIN']) > 200 or float(row['RAIN']) < -200:
                pass
            else:
                if row['STID'] == channel[x]:
                    if x == 0:
                        ALTUr.append((float(row["RAIN"])))
                    elif x == 1:
                        BEAVr.append((float(row["RAIN"])))
                    elif x == 2:
                        NRMNr.append((float(row["RAIN"])))
                    elif x == 3:
                        TISHr.append((float(row["RAIN"])))
                    elif x == 4:
                        TULNr.append((float(row["RAIN"])))

name = input('Name: ')
