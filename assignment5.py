a = list(map(int,input("숫자를 입력해주세요: ").split())) #입력하는 숫자를 받아 배열로 만듦
def ARRAY(X): #함수 선언
    b = list(map(int,input("첫번째, 마지막, 몇번째: ").split())) #제시 구간과 정렬했을때 찾고 싶은 숫자를 따로 배열로 만듦
    X = X[b[0]-1:b[1]] #리스트 요소 특성상 0부터 세기 때문에 -1을 하고 끝에는 미만으로 세기때문에 그대로 씀.
    X.sort() #오름차순 정렬
    return X[b[2]-1] #몇번째 숫자를 찾는지 반환한다.
print(ARRAY(a)) #함수 ARRAY에 입력한 숫자들을 출력
