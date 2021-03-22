def SUMF(numbers):
    result = 0 #result 초깃값 설정
    for i in numbers: #for문을 이용
        result += i #리스트 내 요소들을 더하여 result값에 저장
    return result #합산한 값을 반환

a = list(map(int, input("숫자를 입력하세요.(예시. 10,20이면 10 20) : ").split())) #띄어쓰기를 통해 입력받은 수들을 리스트로 만들어 a에 저장한다.
print("입력한 숫자의 합은 %d입니다." %SUMF(a)) # SUMF함수를 호출
