import csv
import math
import numpy as np
import matplotlib.pyplot as plt

filename = '---.csv'  # ÇÝÞCSVt@C

time = []
a1_values = []
a2_values = []
a3_values = []
dangerous_events = []

# CSVt@CðJ¢ÄÇÝÝ
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    
    # esðÇÝÝAlÌvZðs¤
    for i, row in enumerate(csvreader):
        ax = float(row[0])
        ay = float(row[1])
        az = float(row[2])

# vZ®ª
        A = math.sqrt(ax**2 + ay**2 + az**2)
        g = 9.81
        a1 = math.sqrt(max(A**2 - g**2, 0))
        a2 = ay
        a3 = math.sqrt(ax**2 + az**2)

# èlÌè`
    aggressive_turn_threshold = 0.73 * g  # UIÈ^]ÌùñÁ¬èl
    emergency_turn_threshold = 0.74 * g   # Ù}ùñèl
    uturn_aggressive_threshold = 0.91 * g # UIÈ^]ÌU^[èl
    non_aggressive_turn_threshold = 0.3 * g # ñUIÈ^]Ìùñèl
    uturn_non_aggressive_threshold = 0.56 * g # ñUIÈ^]ÌU^[èl
    a_brake_threshold = 0.48 * g  # }Á¬E}¸¬èl

# èlÌvZª
    if a3 > aggressive_turn_threshold:
        dangerous_events.append((i, 'UIÈùñ', a3))
    elif a3 > emergency_turn_threshold:
        dangerous_events.append((i, 'Ù}ùñ', a3))
    elif a3 > non_aggressive_turn_threshold:
        dangerous_events.append((i, 'ñUIÈùñ', a3))

    if a3 > uturn_aggressive_threshold:
        dangerous_events.append((i, 'UIÈU^[', a3))
    elif a3 > uturn_non_aggressive_threshold:
        dangerous_events.append((i, 'ñUIÈU^[', a3))

    if abs(a2) > a_brake_threshold:
        if a2 > 0:
            dangerous_events.append((i, '}Á¬', a2))
        else:
            dangerous_events.append((i, '}¸¬', a2))

    time.append(i)
    a1_values.append(a1)
    a2_values.append(a2)
    a3_values.append(a3)

    print("m³ê½ë¯^]:")
    for event in dangerous_events:
        print(f": {event[0]} - Cxg: {event[1]} - l: {event[2]:.2f} m/s^2")

    # Á¬x²Évbg
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