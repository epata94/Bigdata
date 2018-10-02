num1=1
num2=0
print("업무1")
# f = open('나있는파일','r')
try:
    result=num1/num2
    f = open('나있는파일','r')
    print("업무2")
except:
    print("""
[알림]
프로그램 수행중 오류발생하였습니다.
코드를 확인하세요.
""")

print("프로그램 정상 종료")
