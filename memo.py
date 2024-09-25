import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# グラフを作成
fig, ax = plt.subplots(figsize=(10, 6))

# 初期化
a1_list = []
a2_list = []
a3_list = []

line1, = ax.plot([], [], label='a1 (Lateral Acceleration)')
line2, = ax.plot([], [], label='a2 (Vertical Acceleration)')
line3, = ax.plot([], [], label='a3 (Longitudinal Acceleration)')

ax.set_xlabel('Time [t]')
ax.set_ylabel('Acceleration [m/s^2]')
ax.set_title('Acceleration vs Time')
ax.legend()
ax.grid(True)

def init():
    ax.set_xlim(0, 10)  # 初期のx軸の範囲
    ax.set_ylim(-10, 10)  # 初期のy軸の範囲
    return line1, line2, line3

def update(frame):
    # ここで ax, ay, az のデータを取得する
    # 例: ax, ay, az = get_acceleration_data()
    # 仮のデータを使用
    ax_data = frame * 0.1
    ay_data = frame * 0.2
    az_data = frame * 0.3

    a1_list.append(ax_data)
    a2_list.append(ay_data)
    a3_list.append(az_data)

    line1.set_data(range(len(a1_list)), a1_list)
    line2.set_data(range(len(a2_list)), a2_list)
    line3.set_data(range(len(a3_list)), a3_list)

    ax.set_xlim(0, len(a1_list))  # x軸の範囲を更新
    ax.set_ylim(min(min(a1_list), min(a2_list), min(a3_list)), max(max(a1_list), max(a2_list), max(a3_list)))  # y軸の範囲を更新

    return line1, line2, line3

ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)

def on_key(event):
    if event.key == 'q':
        plt.close(event.canvas.figure)

fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()