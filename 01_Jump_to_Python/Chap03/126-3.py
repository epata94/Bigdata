# coding: cp949
coffee_number = 10

print("<SW 아키텍처 커피자판기 Ver1.0>")
menu="""
<Menu>
1. 커피구매
2. 커피잔량확인
3. 프로그램 종료
메뉴를 선택하세요: """

while True:
    print(menu,end='')
    choice = int(input())

    if choice == 1:
        money = int(input("\n금액을 입력하세요: "))
        if money == 300:
            print("커피를 줍니다.")
            coffee_number = coffee_number-1
        elif money > 300:
            print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
            coffee_number = coffee_number-1
        elif money < 300 and money > 0:
            print("금액이 %d 모자랍니다." % (300-money))
            print("돈을 다시 돌려주고 커피를 주지 않습니다")
    elif choice == 2:
        print("남은 커피의 양은 %d개입니다.\n" % coffee_number)
    elif choice == 3:
        break

    if not coffee_number:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
