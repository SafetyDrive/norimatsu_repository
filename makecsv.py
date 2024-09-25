import csv
import serial
import time

if __name__ == "__main__":
    ser = serial.Serial("COM4", 9600, timeout=1)

    # CSVファイルを開いて書き込み
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # ヘッダーを書き込む（例：センサー値1, センサー値2, センサー値3, 時刻）
        writer.writerow(['Sensor Value 1', 'Sensor Value 2', 'Sensor Value 3', 'Timestamp'])
        
        # データを連続して取得
        try:
            while True:
                if ser.in_waiting:  # データがシリアルポートに到着しているか確認
                    line = ser.readline().decode('utf-8').strip()  # シリアルデータを読み込む
                    values = line.split(' ')  # データを分割
                    if len(values) == 3:  # データが3つの数字で構成されていることを確認
                        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')  # 現在の時刻を取得
                        print(f"{timestamp}: {values}")  # コンソールに出力（任意）
                        
                        # CSVファイルにデータを書き込む
                        writer.writerow([values[0], values[1], values[2], timestamp])
        except Exception as e:
            print(f"エラーが発生しました: {e}")
        finally:
            # プログラム終了時にシリアルポートを閉じる
            print("データ収集を終了します")
            ser.close()
