# 載入套件
from talib.abstract import *
import sys,Function

# 資料參數 (可自行調整)
SDate = sys.argv[1] # 資料起始日
EDate = sys.argv[2] # 資料結束日
Prod = sys.argv[3]  # 商品代碼
Kind = sys.argv[4]  # 商品種類
Cycle = sys.argv[5] # K棒週期

# 取得K棒資料
KBar = Function.GetKBar(SDate,EDate,Prod,Kind,Cycle)

# 計算技術指標
flag = False
Data = CDLGAPSIDESIDEWHITE(KBar)
for i in range(0,len(Data)):
    signal = Data[i]
    if signal != 0: 
        print( KBar.index[i],signal )
        flag = True

if flag == False:
    print('期間內無觸發此型態訊號')
