def bubble_sort(x): #bubble_sort 함수
    for i in range(0,len(x)-1,1): #입력받은 수 길이-1(0부터 세기때문), 1씩 증가
        for j in range(0,len(x)-1,1):#입력받은 수 길이-1, 1씩증가
            if x[j] > x[j+1]: #(입력기준) 왼쪽 숫자가 크면
                x[j], x[j+1] = x[j+1], x[j] # 스위치
    return x #반환값

a = list(map(int,input("숫자를 입력해주세요").split())) #띄어쓰기로 숫자 구분, 입력한 수를 정수값으로 바꾸어주는 map함수 이용
print(bubble_sort(a)) #입력한 수를 함수에 입력