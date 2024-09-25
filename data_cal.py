import csv
import math
import os
import numpy as np
import matplotlib.pyplot as plt

filename = '2024-09-17_exmple1.csv'  # 読み込むCSVファイル

time = []
a1_values = []
a2_values = []
a3_values = []
dangerous_events = []

# CSVファイルを開いて読み込み
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    
    # 各行を読み込み、数値の計算を行う
    for i, row in enumerate(csvreader):
        ax = float(row[0])
        ay = float(row[1])
        az = float(row[2])

# 計算式部分
        A = math.sqrt(ax**2 + ay**2 + az**2)
        g = 9.81
        a1 = math.sqrt(max(A**2 - g**2, 0))
        a2 = ay
        a3 = math.sqrt(ax**2 + az**2)

# 閾値の定義
    aggressive_turn_threshold = 0.73 * g  # 攻撃的な運転の旋回加速閾値
    emergency_turn_threshold = 0.74 * g   # 緊急旋回閾値
    uturn_aggressive_threshold = 0.91 * g # 攻撃的な運転のUターン閾値
    non_aggressive_turn_threshold = 0.3 * g # 非攻撃的な運転の旋回閾値
    uturn_non_aggressive_threshold = 0.56 * g # 非攻撃的な運転のUターン閾値
    a_brake_threshold = 0.48 * g  # 急加速・急減速閾値

# 閾値の計算部分
    if a3 > aggressive_turn_threshold:
        dangerous_events.append((i, '攻撃的な旋回', a3))
    elif a3 > emergency_turn_threshold:
        dangerous_events.append((i, '緊急旋回', a3))
    elif a3 > non_aggressive_turn_threshold:
        dangerous_events.append((i, '非攻撃的な旋回', a3))

    if a3 > uturn_aggressive_threshold:
        dangerous_events.append((i, '攻撃的なUターン', a3))
    elif a3 > uturn_non_aggressive_threshold:
        dangerous_events.append((i, '非攻撃的なUターン', a3))

    if abs(a2) > a_brake_threshold:
        if a2 > 0:
            dangerous_events.append((i, '急加速', a2))
        else:
            dangerous_events.append((i, '急減速', a2))

    time.append(i)
    a1_values.append(a1)
    a2_values.append(a2)
    a3_values.append(a3)

    print("検知された危険運転:")
    for event in dangerous_events:
        print(f"時刻: {event[0]} - イベント: {event[1]} - 値: {event[2]:.2f} m/s^2")

    # 時刻加速度軸にプロット
    plt.figure(figsize=(10, 6))

    plt.plot(time, a1_values, label='a1 (Lateral Acceleration)')
    plt.plot(time, a2_values, label='a2 (Vertical Acceleration)')
    plt.plot(time, a3_values, label='a3 (Longitudinal Acceleration)')

    plt.xlabel('Time [t]')
    plt.ylabel('Acceleration [m/s^2]')
    plt.title('Acceleration vs Time')
    plt.legend()
    plt.grid(True)

    plt.show()