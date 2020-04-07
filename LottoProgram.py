import random, string

cn = "y"

print("로또 번호 자동 생성 프로그램 시작")
print("-------------------------------------------")
print("게임수를 입력하세요. 숫자만 입력 가능합니다. :")

while( cn == "Y" or cn == "y" ):

    num = input("숫자입력 :")

    if( num.isdigit() == True ) :

        print("-------------------------------------------")

        for i in range(0, int(num)):
            lotto = random.sample(range(1,46), 6)
            lotto.sort()
            print(lotto)
    else:
        print("숫자를 입력하세요.")
        continue

    print("-------------------------------------------")
    print("로또 번호 자동 생성 완료")
    print("-------------------------------------------")
    cn = input("다시 하시겠습니까(Y/N)? :")
    
    while(cn != "y" and cn != "Y" and cn != "n" and cn != "N"):
        print("y나 n만 입력하세요.")
        print("-------------------------------------------")
        cn = input("다시 하시겠습니까(Y/N)? :")

print("-------------------------------------------")
print("로또 번호 자동 생성 프로그램 종료")
print("Enter 를 누르면 프로그램이 꺼집니다.")
input(":")