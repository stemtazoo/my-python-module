import pandas as pd
from chardet.universaldetector import UniversalDetector

# 2つの変数の和を計算する自作関数
def my_sum(x,y):
    z = x + y
    return z

# 2つの変数の差を計算する自作関数
def my_dif(x,y):
    z = x - y
    return z

def my_waru(x,y):
    z=x/y
    return z

#CSVファイルの内容をdataframeに入れて返す。
#filepath:ファイルパス
#hederCol:ヘッダー行
def readcsv(filepath,headerCol):
    detector = UniversalDetector()
    with open(filepath, mode='rb') as f:
        for binary in f:
            detector.feed(binary)
            if detector.done:
                break
    detector.close()
    df=pd.read_csv(filepath, header=headerCol,encoding=detector.result['encoding'])
    return df
