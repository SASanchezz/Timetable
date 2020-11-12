from itertools import chain
import math
import numpy as np
import pandas as pd

df = pd.read_excel('data.xlsx')
#print(type(df[df['Week'].isnull()]['Week'][64]))
for i in range(0, len(df['Week'])):
    if type(df['Week'][i]) != float:
        try:
            df['Week'][i] = int(df['Week'][i])
        except ValueError:
            df['Week'][i] = df['Week'][i].split(',')

    df['Group'][i] = str(df['Group'][i])

    if type(df['Day'][i]) == str:
        day = df['Day'][i]
    if type(df['Day'][i]) == float:
        df['Day'][i] = day

    if type(df['Time'][i]) == str:
        time = df['Time'][i]
    if type(df['Time'][i]) == float:
        df['Time'][i] = time

for i in range(0, len(df['Week'])):
    if type(df['Week'][i]) != float and type(df['Week'][i]) != int:
        for j in range (0, len(df['Week'][i])):
            row = []
            if "-" in df['Week'][i][j]:
                df['Week'][i][j] = df['Week'][i][j].split('-')
                for k in range (int(df['Week'][i][j][0]), int(df['Week'][i][j][1])+1):
                    row.append(k)
                df['Week'][i][j] = row
        if isinstance(df['Week'][i][0], list) or isinstance(df['Week'][i][1], list):
            df['Week'][i] = list(chain.from_iterable(df['Week'][i]))
        df['Week'][i] = list(map(int, df['Week'][i]))
    if type(df['Week'][i]) == int:
        df['Week'][i] = [df['Week'][i]]



    #print(df.iloc[i][])




    #print(df['Time'][i])

    #print (len(df['Week']))

