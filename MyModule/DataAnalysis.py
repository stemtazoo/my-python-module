import pandas as pd
import glob
from chardet.universaldetector import UniversalDetector

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