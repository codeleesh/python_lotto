import random, string

cn = "y"

print("BR♡PD♥SH")
print("로또 번호 자동 생성 프로그램 시작")
print("-------------------------------------------")
print("게임수를 입력하세요. 숫자만 입력 가능합니다. :")

while( cn == "Y" or cn == "y" ):
    print("-------------------------------------------")
    print("변수 초기화")
    lotto = None
    num = input("숫자입력 :")

    if( num.isdigit() == True ) :

        print("-------------------------------------------")
        print("랜덤으로 뽑은 Lotto 숫자")
        for i in range(0, int(num)):
            lotto = random.sample(range(1,46), 6)
            lotto.sort()
            print(lotto)
            lotto = None

        # choiceLotto = list(set(choiceLotto))
        # print("랜덤으로 뽑힌 Lotto 숫자 중에서 다시 랜덤으로 뽑은 숫자")
        # for i in range(0, int(num)):
        #     newLotto = random.sample(choiceLotto, 6)
        #     newLotto.sort()
        #     print(newLotto)
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
print("BR♡PD♥SH")
input(":")