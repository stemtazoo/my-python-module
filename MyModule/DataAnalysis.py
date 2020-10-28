import pandas as pd
import glob
from chardet.universaldetector import UniversalDetector
import matplotlib.pyplot as plt
import shutil
import os

# 2つの変数の和を計算する自作関数
def my_sum(x,y):
    z = x + y
    return z

# 2つの変数の差を計算する自作関数
def my_dif(x,y):
    z = x - y
    return z

# 2つの変数の商を計算する自作関数
def my_waru(x,y):
    z=x/y
    return z

# 2つの変数の積を計算する自作関数
def my_kakeru(x,y):
    z=x*y
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

#フォルダ内にある複数のCSVファイルの内容をdataframeに入れて返す。
def readcsvfiles(filepath):
  csv_files = glob.glob(filepath+'*.csv')
  list = []
  for file in csv_files:
    list.append(pd.read_csv(file))

  df = pd.concat(list)
  return df

#ヒストグラムを作成して、グラフを保存する。
def graph_hist(path,data,bins_number=10,title='hist',xlabel='x',ylabel='y'):
  # 画像準備
  fig = plt.figure()
  # ヒストグラムを出力
  plt.hist(data,bins=bins_number)
  # グラフの指定
  plt.title(title)
  # x軸のラベル
  plt.xlabel(xlabel)
  # y軸のラベル
  plt.ylabel(ylabel)
  # グラフをファイルに保存する
  fig.savefig(path)

#散布図を作成して、グラフに保存する。
def graph_scatterplot(path,data_x,data_y,title='scatterplot',xlabel='x',ylabel='y'):
  # 画像準備
  fig = plt.figure()
  # 散布図を出力
  plt.scatter(data_x,data_y)
  # グラフの指定
  plt.title(title)
  # x軸のラベル
  plt.xlabel(xlabel)
  # y軸のラベル
  plt.ylabel(ylabel)
  # グラフをファイルに保存する
  fig.savefig(path)

#フォルダ内を空にする。
def create_folder(path):
  if os.path.isdir(path):
    #ディレクトリの削除
    shutil.rmtree(path)
  #フォルダの作成
  os.mkdir(path)
