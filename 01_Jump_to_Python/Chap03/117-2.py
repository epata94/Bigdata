# coding: cp949
money = int(input("�󸶸� ������ �ֽ��ϱ�? "))
card = input("ī�带 �����ϰ� �ֽ��ϱ�? (y/n) : ")
if card == 'y':     card = True
else:               card = False

if money >= 3000:
    print("��Ű��ó �ؽ� �м� ������ �м��մϴ�.")
    print("�м��� �Ϸᰡ �Ǿ����ϴ�.")
    print("�ؽø� Ÿ�� ����")
elif card == True:
    print("�ؽø� Ÿ�� ����")
else:
    print("�ɾ��")

