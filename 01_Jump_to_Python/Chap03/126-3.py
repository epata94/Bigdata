# coding: cp949
coffee_number = 10

print("<SW ��Ű��ó Ŀ�����Ǳ� Ver1.0>")
menu="""
<Menu>
1. Ŀ�Ǳ���
2. Ŀ���ܷ�Ȯ��
3. ���α׷� ����
�޴��� �����ϼ���: """

while True:
    print(menu,end='')
    choice = int(input())

    if choice == 1:
        money = int(input("\n�ݾ��� �Է��ϼ���: "))
        if money == 300:
            print("Ŀ�Ǹ� �ݴϴ�.")
            coffee_number = coffee_number-1
        elif money > 300:
            print("�Ž����� %d�� �ְ� Ŀ�Ǹ� �ݴϴ�." % (money -300))
            coffee_number = coffee_number-1
        elif money < 300 and money > 0:
            print("�ݾ��� %d ���ڶ��ϴ�." % (300-money))
            print("���� �ٽ� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�")
    elif choice == 2:
        print("���� Ŀ���� ���� %d���Դϴ�.\n" % coffee_number)
    elif choice == 3:
        break

    if not coffee_number:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break
