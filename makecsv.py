import csv
import serial
import time

if __name__ == "__main__":
    ser = serial.Serial("COM4", 9600, timeout=1)

    # CSV�t�@�C�����J���ď�������
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # �w�b�_�[���������ށi��F�Z���T�[�l1, �Z���T�[�l2, �Z���T�[�l3, �����j
        writer.writerow(['Sensor Value 1', 'Sensor Value 2', 'Sensor Value 3', 'Timestamp'])
        
        # �f�[�^��A�����Ď擾
        try:
            while True:
                if ser.in_waiting:  # �f�[�^���V���A���|�[�g�ɓ������Ă��邩�m�F
                    line = ser.readline().decode('utf-8').strip()  # �V���A���f�[�^��ǂݍ���
                    values = line.split(' ')  # �f�[�^�𕪊�
                    if len(values) == 3:  # �f�[�^��3�̐����ō\������Ă��邱�Ƃ��m�F
                        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')  # ���݂̎������擾
                        print(f"{timestamp}: {values}")  # �R���\�[���ɏo�́i�C�Ӂj
                        
                        # CSV�t�@�C���Ƀf�[�^����������
                        writer.writerow([values[0], values[1], values[2], timestamp])
        except Exception as e:
            print(f"�G���[���������܂���: {e}")
        finally:
            # �v���O�����I�����ɃV���A���|�[�g�����
            print("�f�[�^���W���I�����܂�")
            ser.close()
