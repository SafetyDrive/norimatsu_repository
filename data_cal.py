import csv
import math
import statistics  # 平均を計算するためのライブラリ


filename = '---.csv'  # 読み込むCSVファイル

results = []

# CSVファイルを開いて読み込み
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    
    # 各行を読み込み、数値の計算を行う
    for row in csvreader:


        
        # 結果をリストに追加
        results.append(result)

# 平均を計算
average_result = statistics.mean(results)

# 結果を表示
print("計算結果の平均:", average_result)
