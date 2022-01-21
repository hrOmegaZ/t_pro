'''Write an interactive program that asks the user what information they would like to analyze, whether they want for the entire year or an individual month.
Display the output on a line graph.
- address the user by name throughout the program
- data category choices must include:  Tmax, Tmin, wind speed, humidity, rain totals
- the graph should use labels for axes, a different color line for each station, and a legend to map the colors to the stations'''

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

name = input('Name: ')
month = input('year or month: ')
while month != 'year' and month != 'month':
    print('Try again.')
    month = input('year or month (lowercase): ')
if month == 'month':
    i_month = input('Which month would you like to see (month name): ')
    if i_month not in months:
        print('Try again')
        i_month = input('Which month would you like to see (month name): ')
    else:
        pass
else:
    pass
category = input('Choose from- TMAX, TMIN, wind speed, humidity, rain totals: ')
while category != "TMAX" and category != 'TMIN' and category != 'wind speed' and category != 'humidity' and category != 'rain totals':
    print('Try again')
    category = input('Choose from- TMAX, TMIN, wind speed, humidity, rain totals: ')

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
            if month == 'month':
                if row['MONTH'] == months.index('January'):
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
            else:
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

if category == 'TMAX':
    x = []
    for lel in range(len(ALTUm)):
        x.append(lel)
    y = ALTUm
    x1 = []
    for lel in range(len(BEAVm)):
        x1.append(lel)
    y1 = BEAVm
    x2 = []
    for lel in range(len(NRMNm)):
        x2.append(lel)
    y2 = NRMNm
    x3 = []
    for lel in range(len(TISHm)):
        x3.append(lel)
    y3 = TISHm
    x4 = []
    for lel in range(len(TULNm)):
        x4.append(lel)
    y4 = TULNm

    plt.plot(x, y, label='ALTU')
    plt.plot(x1,y1, label='BEAV')
    plt.plot(x2,y2, label='NRMN')
    plt.plot(x3,y3, label='TISH')
    plt.plot(x4,y4, label='TULN')

    leg = plt.legend(loc='lower center')
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.title("Weather Channel's Maximums")

    plt.show()

elif category == 'TMIN':
    x = []
    for lel in range(len(ALTU)):
        x.append(lel)
    y = ALTU
    x1 = []
    for lel in range(len(BEAV)):
        x1.append(lel)
    y1 = BEAV
    x2 = []
    for lel in range(len(NRMN)):
        x2.append(lel)
    y2 = NRMN
    x3 = []
    for lel in range(len(TISH)):
        x3.append(lel)
    y3 = TISH
    x4 = []
    for lel in range(len(TULN)):
        x4.append(lel)
    y4 = TULN

    plt.plot(x, y, label='ALTU')
    plt.plot(x1,y1, label='BEAV')
    plt.plot(x2,y2, label='NRMN')
    plt.plot(x3,y3, label='TISH')
    plt.plot(x4,y4, label='TULN')

    leg = plt.legend(loc='lower center')
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.title("Weather Channel's Minimums")

    plt.show()

elif category == 'wind speed':
    x = []
    for lel in range(len(ALTUWSmx)):
        x.append(lel)
    y = ALTUWSmx
    x1 = []
    for lel in range(len(BEAVWSmx)):
        x1.append(lel)
    y1 = BEAVWSmx
    x2 = []
    for lel in range(len(NRMNWSmx)):
        x2.append(lel)
    y2 = NRMNWSmx
    x3 = []
    for lel in range(len(TISHWSmx)):
        x3.append(lel)
    y3 = TISHWSmx
    x4 = []
    for lel in range(len(TULNWSmx)):
        x4.append(lel)
    y4 = TULNWSmx

    x5 = []
    for lel in range(len(ALTUWSmn)):
        x5.append(lel)
    y5 = ALTUWSmn
    x6 = []
    for lel in range(len(BEAVWSmn)):
        x6.append(lel)
    y6 = BEAVWSmn
    x7 = []
    for lel in range(len(NRMNWSmn)):
        x7.append(lel)
    y7 = NRMNWSmn
    x8 = []
    for lel in range(len(TISHWSmn)):
        x8.append(lel)
    y8 = TISHWSmn
    x9 = []
    for lel in range(len(TULNWSmn)):
        x9.append(lel)
    y9 = TULNWSmn

    plt.plot(x, y, label='ALTUmx')
    plt.plot(x1,y1, label='BEAVmx')
    plt.plot(x2,y2, label='NRMNmx')
    plt.plot(x3,y3, label='TISHmx')
    plt.plot(x4,y4, label='TULNmx')

    plt.plot(x5, y5, label='ALTUmn')
    plt.plot(x6,x6, label='BEAVmn')
    plt.plot(x7,y7, label='NRMNmn')
    plt.plot(x8,y8, label='TISHmn')
    plt.plot(x9,y9, label='TULNmn')

    leg = plt.legend(loc='lower center')
    plt.xlabel("Day")
    plt.ylabel("Wind Speed")
    plt.title("Weather Channel's Wind Speed Max and Mins")

    plt.show()

elif category == 'humidity':
    x = []
    for lel in range(len(ALTUh)):
        x.append(lel)
    y = ALTUh
    x1 = []
    for lel in range(len(BEAVh)):
        x1.append(lel)
    y1 = BEAVh
    x2 = []
    for lel in range(len(NRMNh)):
        x2.append(lel)
    y2 = NRMNh
    x3 = []
    for lel in range(len(TISHh)):
        x3.append(lel)
    y3 = TISHh
    x4 = []
    for lel in range(len(TULNh)):
        x4.append(lel)
    y4 = TULNh

    plt.plot(x, y, label='ALTU')
    plt.plot(x1,y1, label='BEAV')
    plt.plot(x2,y2, label='NRMN')
    plt.plot(x3,y3, label='TISH')
    plt.plot(x4,y4, label='TULN')

    leg = plt.legend(loc='lower center')
    plt.xlabel("Day")
    plt.ylabel("Humidity")
    plt.title("Weather Channel's Humidity")

    plt.show()

elif category == 'rain totals':
    x = []
    for lel in range(len(ALTUr)):
        x.append(lel)
    y = ALTUr
    x1 = []
    for lel in range(len(BEAVr)):
        x1.append(lel)
    y1 = BEAVr
    x2 = []
    for lel in range(len(NRMNr)):
        x2.append(lel)
    y2 = NRMNr
    x3 = []
    for lel in range(len(TISHr)):
        x3.append(lel)
    y3 = TISHr
    x4 = []
    for lel in range(len(TULNr)):
        x4.append(lel)
    y4 = TULNr

    plt.plot(x, y, label='ALTU')
    plt.plot(x1,y1, label='BEAV')
    plt.plot(x2,y2, label='NRMN')
    plt.plot(x3,y3, label='TISH')
    plt.plot(x4,y4, label='TULN')

    leg = plt.legend(loc='lower center')
    plt.xlabel("Day")
    plt.ylabel("Rain Totals")
    plt.title("Weather Channel's Rain Totals")

    plt.show()