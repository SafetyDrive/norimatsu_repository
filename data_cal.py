import csv
import math
import statistics  # ���ς��v�Z���邽�߂̃��C�u����


filename = '---.csv'  # �ǂݍ���CSV�t�@�C��

# ���ʂ��i�[���邽�߂̃��X�g
results = []

# CSV�t�@�C�����J���ēǂݍ���
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    
    # �e�s��ǂݍ��݁A���l�̌v�Z���s��
    for row in csvreader:
        # ��Ƃ��āA�e�s��2�ڂ̒l���g�� (�K�v�ɉ����ăC���f�b�N�X��ύX)
        value = float(row[1])  # ���l�f�[�^�����o����float�^�ɕϊ�
        
        # ����̎��ɑ���i�����ł͗�Ƃ��� x^2 + 2x + 1�j
        result = value**2 + 2 * value + 1
        
        # ���ʂ����X�g�ɒǉ�
        results.append(result)

# ���ς��v�Z
average_result = statistics.mean(results)

# ���ʂ�\��
print("�v�Z���ʂ̕���:", average_result)
