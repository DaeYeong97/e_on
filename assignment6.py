import math # 수학적 모듈 math 선언

def NOC(n): # Number Of Case 함수 선언
    r = 0
    result = 0 #초기값 세팅
    while True: #무한루프
        result += math.factorial(n) // (math.factorial(r) * math.factorial(n-r)) # nCr조합 함수에서 nC0 + n-1C1 + n-2C2 ...까지 더한다.
        r += 1 # r 을 1씩 더한다.
        n -= 1 # n을 1씩 뺀다.
        if n < r: #r이 n보다 커지기 전까지 더하고, 커지면 함수 무한루프 탈출
          break
    return result

a = int(input("숫자를 입력하세요: "))
print(NOC(a)) #함수 대입
