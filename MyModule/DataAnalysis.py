import pandas as pd
import glob
from chardet.universaldetector import UniversalDetector
import matplotlib.pyplot as plt

# 2�̕ϐ��̘a���v�Z���鎩��֐�
def my_sum(x,y):
    z = x + y
    return z

# 2�̕ϐ��̍����v�Z���鎩��֐�
def my_dif(x,y):
    z = x - y
    return z

# 2�̕ϐ��̏����v�Z���鎩��֐�
def my_waru(x,y):
    z=x/y
    return z

# 2�̕ϐ��̐ς��v�Z���鎩��֐�
def my_kakeru(x,y):
    z=x*y
    return z

#CSV�t�@�C���̓��e��dataframe�ɓ���ĕԂ��B
#filepath:�t�@�C���p�X
#hederCol:�w�b�_�[�s
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

#�t�H���_���ɂ��镡����CSV�t�@�C���̓��e��dataframe�ɓ���ĕԂ��B
def readcsvfiles(filepath):
  csv_files = glob.glob(filepath+'*.csv')
  list = []
  for file in csv_files:
    list.append(pd.read_csv(file))

  df = pd.concat(list)
  return df

#�q�X�g�O�������쐬���āA�O���t��ۑ�����B
def graph_hist(data,bins_number=10,title,xlabel='x',ylabel='y',path):
  # �摜����
  fig = plt.figure()
  # �q�X�g�O�������o��
  plt.hist(data,bins=bins_number)
  # �O���t�̎w��
  plt.title(title)
  # x���̃��x��
  plt.xlabel(xlabel)
  # y���̃��x��
  plt.ylabel(ylabel)
  # �O���t���t�@�C���ɕۑ�����
  fig.savefig(path)

#�U�z�}���쐬���āA�O���t�ɕۑ�����B
def graph_scatterplot(data_x,data_y,title,xlabel='x',ylabel='y',path)
  # �摜����
  fig = plt.figure()
  # �U�z�}���o��
  .scatter(data_x,data_y)
  # �O���t�̎w��
  plt.title(title)
  # x���̃��x��
  plt.xlabel(xlabel)
  # y���̃��x��
  plt.ylabel(ylabel)
  # �O���t���t�@�C���ɕۑ�����
  fig.savefig(path)