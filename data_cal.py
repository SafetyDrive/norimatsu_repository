import csv
import math
import statistics  # 平均を計算するためのライブラリ


filename = '---.csv'  # 読み込むCSVファイル

# 結果を格納するためのリスト
results = []

# CSVファイルを開いて読み込み
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    
    # 各行を読み込み、数値の計算を行う
    for row in csvreader:
        # 例として、各行の2つ目の値を使う (必要に応じてインデックスを変更)
        value = float(row[1])  # 数値データを取り出してfloat型に変換
        
        # 特定の式に代入（ここでは例として x^2 + 2x + 1）
        result = value**2 + 2 * value + 1
        
        # 結果をリストに追加
        results.append(result)

# 平均を計算
average_result = statistics.mean(results)

# 結果を表示
print("計算結果の平均:", average_result)
