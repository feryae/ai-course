from typing import List
import math
import numpy as np # learn more: https://python.org/pypi/numpy
import pandas as pd # learn more: https://python.org/pypi/pandas
from io import StringIO
import random

def shannon_entropy(p1: float, p2: float) -> float:
  # TODO: your Shannon Entropy function here
  entropyRet = (-p1*math.log(p1,2)) - (p2*math.log(p2,2)) 
  return entropyRet

def information_gain(_ent_buy: float,
    p_low: float, _ent_buy_low: float, 
    p_med: float, _ent_buy_med: float,
    p_high: float, _ent_buy_high: float) -> float:
  # TODO: your Information Gain function here
  infoGain = _ent_buy - (p_low*_ent_buy_low) - (p_med*_ent_buy_med) - (p_high*_ent_buy_high)
  return infoGain

lines = []
while True:
  line = input()
  lines.append(line)
  if not line.strip():
    break
csv = "\n".join(lines)

df = pd.read_csv(StringIO(csv))
#print(df)


len_all = len(df)
len_buy_deal = len(df[(df.buy == 'Deal')])
len_buy_away = len(df[(df.buy == 'Away')])

ent_buy = shannon_entropy(len_buy_deal/len_all,len_buy_away/len_all)
print('%.04f' % ent_buy)
len_low = len(df[(df.price == 'Low' )])
len_med = len(df[(df.price == 'Med' )])
len_high = len(df[(df.price == 'High' )])

len_deal_low = len(df[(df.price == 'Low' ) & (df.buy == 'Deal' )])
len_away_low = len(df[(df.price == 'Low' ) & (df.buy == 'Away' )])
ent_buy_low = shannon_entropy(len_deal_low/len_low,len_away_low/len_low)
# print('len_deal_low=', len_deal_low, len_deal_low / len_low)
# print('len_away_low=', len_away_low, len_away_low / len_low)
print('%.04f' % ent_buy_low)

len_deal_med = len(df[(df.price == 'Med' ) & (df.buy == 'Deal' )])
len_away_med = len(df[(df.price == 'Med' ) & (df.buy == 'Away' )])
ent_buy_med = shannon_entropy(len_deal_med/len_med,len_away_med/len_med)
print('%.04f' % ent_buy_med)

len_deal_high = len(df[(df.price == 'High' ) & (df.buy == 'Deal' )])
len_away_high = len(df[(df.price == 'High' ) & (df.buy == 'Away' )])
ent_buy_high = shannon_entropy(len_deal_high/len_high,len_away_high/len_high)
print('%.04f' % ent_buy_high)

ig_price = information_gain(ent_buy, len_low/len_all, ent_buy_low , len_med/len_all, ent_buy_med, len_high/len_all, ent_buy_high)
print('%.04f' % ig_price)
