import json
import pandas as pd
import requests
import math
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def resp_to_packets(resp_text):
    ''' Convert file to list of packets.'''
    packet = ''
    for line in resp_text.split('\n'):
        if line.startswith('}{'):
            packet += '}'
            yield json.loads(packet)
            packet = '{'
        else:
            packet += line + '\n'
    yield json.loads(packet)
    
def packet_to_df(packet):
    ''' Convert packet to data frame.'''
    df = list()
    for key, values in packet.items():
        t = (pd.json_normalize(values)
              .explode('co2')
              .explode('occupancy')
              .explode('temperature')
              .assign(room=key)
             )
        df.append(t)
    return pd.concat(df, ignore_index=True)

dtypes = {'co2': float, 'occupancy': int, 'temperature': float, 
          'time': 'datetime64', 'room': str}
url = 'https://gist.githubusercontent.com/tzelaya21/9b90dd07a3bdf49322f5b8019db73c96/raw/148ad3419d1520a478d3f0d7b66213ff7d84d76f/data.json'
r = requests.get(url)
assert r.ok

packets = (packet for packet in resp_to_packets(r.text))
dfs     = (packet_to_df(packet) for packet in packets)
df      = pd.concat(dfs, ignore_index=True).astype(dtype=dtypes)

lab1 = df.loc[df['room'] == 'lab1']
class1 = df.loc[df['room'] == 'class1']
office = df.loc[df['room'] == 'office']

lab1 = lab1.reset_index(drop=True)
class1 = class1.reset_index(drop=True)
office = office.reset_index(drop=True)

stand_dev = math.sqrt(lab1.var()['temperature'])
mini = int(round((lab1.mean()['temperature'] - 2*stand_dev)))
maxi = int(round((lab1.mean()['temperature'] + 2*stand_dev)))

check = []
for i in range (len(lab1)):
    if lab1.loc[i, 'temperature'] < maxi and lab1.loc[i, 'temperature'] > mini:
        check.append(lab1.loc[i, 'temperature'])
    else:
        check.append(np.nan)

lab1['filtered'] = pd.DataFrame(check, columns = ['Valid'])

bad_n = lab1['filtered'].isnull().sum()
bad_per = round((bad_n/len(lab1))*100, 2)
print("Percentage of bad data points: " + str(bad_per) +"%")

print("New median is " + str(lab1.median()['filtered']))
print("New variance is " + str(lab1.var()['filtered']))