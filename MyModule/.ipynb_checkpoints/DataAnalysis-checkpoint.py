import pandas as pd
import glob
from chardet.universaldetector import UniversalDetector
import matplotlib.pyplot as plt
import japanize_matplotlib
import shutil
import os
import openpyxl
from openpyxl import Workbook
from openpyxl.chart import ScatterChart, Reference, Series

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

#データフレーム内の列をヒストグラムを保存する。
def df_graph_hist(path,df_data):
　#path:グラフを保存するフォルダ
　#df_data:計算するdataframe
  #文字列データを除く
  df_data.select_dtypes(exclude=object)
  #すべての列でヒストグラムをグラフ化し、画像を保存する。
  for colum_name,item in df_data.iteritems():
    graph_hist(path+'\\'+colum_name+'.png',item,bins_number=10,title=colum_name,xlabel='x',ylabel='y')

#エクセルファイルで散布図を作成する。
def excel_graph_scatter(path,WSName,column_x,column_y_min,column_y_num,row_min,row_max,title):
  #ワークブックを開く
  wb = openpyxl.load_workbook(path)
  #ScatterChartオブジェクトを作成
  chart = ScatterChart()
  #グラフのX軸の範囲を設定する為に、Referenceオブジェクト作る
  x_values = Reference(wb[WSName], min_col = column_x, min_row = row_min, max_row = row_max)
  #データの書き込み
  for i in range(0, column_y_num):
    min_col = i + column_y_min
    #データの範囲(Y軸)をReferenceで選択
    values = Reference(wb[WSName], min_col = min_col, min_row = row_min, max_row = row_max)
    #Seriesオブジェクトを作成
    series = Series(values, x_values, title=i)
    #線を消す
    series.graphicalProperties.line.noFill = True
    #マーカーを表示する
    series.marker.symbol = 'circle'
    #散布図として定義したchartへデータを指定したseries変数を渡す
    chart.series.append(series)
  #B2セルにグラフを表示
  wb[WSName].add_chart(chart,"B2")
  #Fileを保存
  wb.save(path)