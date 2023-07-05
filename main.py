from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random
from openpyxl import load_workbook


r = requests.get('https://fbx.freightos.com/api/ticker')
soup = bs(r.content, 'html.parser')
text = str(soup)


fbx_holder = ""
price_holder = ""
a = 1
point = 0

fbx_list = []
prices_list = []


print(len(text))

for i in range(len(text)):
    fbx_holder = ""
    if text[i] + text[i+1] + text[i+2] == "FBX":
        point = i+2
        while text[point] != '"':
            fbx_holder += text[point]
            point += 1

        fbx_list.append("FB" + fbx_holder)

    price_holder = ""
    if text[i] + text[i+1] + text[i+2] + text[i+3] + text[i+4] == 'lue":':
        point = i+5
        while text[point] != '.':
            price_holder += text[point]
            point += 1
    prices_list.append(price_holder)



    if i >= 1315:
        break

print(fbx_list)

prices_list = list(filter(None, prices_list))
prices_list = list(map(float, prices_list))

def multiply(a):
    return a * 0.001

def zaokr(r):
    return round(r, 3)


prices_list = list(map(multiply, prices_list))

prices_list[2] = prices_list[2]*1000
prices_list[4] = prices_list[4]*1000
prices_list[6] = prices_list[6]*1000
prices_list[9] = prices_list[9]*1000

prices_list = list(map(zaokr, prices_list))


print(prices_list)
#key_list
fbx_constant_list = fbx_list

main_dict = dict(zip(fbx_constant_list, prices_list))
print(main_dict)

df = pd.DataFrame(data=main_dict, index=['Prices in $'])
df = (df.T)
#print(df)

df.to_excel('test.xlsx')

#TODO :: Przekonwertować zapis wartości słownika jako listy z stringów
#TODO ::