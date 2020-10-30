# -*- coding: utf-8 -*-
# from src import randomClass

# test = randomClass.StockPridict()


# import sys
# import pathlib
# # base.pyのあるディレクトリの絶対パスを取得
# current_dir = pathlib.Path(__file__).resolve().parent
# # モジュールのあるパスを追加
# sys.path.append(str(current_dir) + '/../')

# # モジュールのインポート
# import ..src.randomClass
# # test = randomClass.StockPridict()


# 上の階層を見る方法
import sys
sys.path.append('../')
from src.randomClass import StockPridict

if __name__ == '__main__':
    test = StockPridict()
    print(type(str(test.result)))
    print(str(test.result))
    print('トレーニングデータに対する正解率： %.2f' % test.result)