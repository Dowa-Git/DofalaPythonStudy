# int Ÿ���� ���� ����
# NumberZero��� �̸��� ������ ����� ���⿡ ���� 0�� �־��ּ���.
NumberZero = 0

# float Ÿ���� ���� ����
# FloatSix��� �̸��� ������ ����� ���⿡ �Ǽ� 6.0�� �־��ּ���.
FloatSix = 6.0 

# char Ÿ���� ���� ����
# CharA��� �̸��� ������ ����� ���⿡ ���� A�� �־��ּ���.
CharA = 'A'

# bool Ÿ���� ���� ����
# IsTrue��� �̸��� ������ ����� ���⿡ True ���� �־��ּ���.
IsTrue = True


# �Է� �ޱ�
# Input���� = �Է±�('�Է� ���� �� ǥ�� �� ����')
Input = input('input the number : ')
# ���(Input����)
print(Input)


# For �ݺ���
# �ݺ� [0����5����]:
for i in range(0,5):
#   ��±�('a')
    print('a')


#  While �ݺ��� 
# Condition ���� = ��
Condition = True
# �ݺ� [Condition ������ ���� ����]
while Condition:
#    ��±�('*')
    print('*')
    
#### �� While �� ���ô� ���� �ݺ��̹Ƿ� �Ʒ� while �� ���ø� �׽�Ʈ �Ͻ÷��� ���� ������ �ּ� ó��(#) Ȥ�� ����� �׽�Ʈ ���ּ���.


# While �ݺ��� ����
# CurrentInput ���� = -1
CurrentInput = ''
# �ݺ� [CurrentInput ������ 0�� �ƴ� ����]
while CurrentInput != '0':
    # CurrentInput ���� = �Է±�('���ڸ� �Է����ּ���. (0�� �Է��ϸ� ����ϴ�.')
    CurrentInput = input('input the word (for break input 0) : ')
    # ���('���� �Էµ� �ܾ�� ->')
    print('Current Input word is -> ')
    # ���(CurrentInput ����)
    print(CurrentInput)
    