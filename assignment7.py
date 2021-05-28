class Library: # 도서관리 클래스
    def __init__(self):
        pass
    def add_book(self): #책 입력함수
        bookcare.addbook1()
    def search_book(self): #책 검사함수
        bookcare.searchbook1()
    def data_book(self): #책 개별검사 함수
        bookcare.databook1() 
    def revise_book(self): #책 수정함수
        bookcare.revisebook1() 
    def delete_book(self): #책 삭제함수
        bookcare.deletebook1()
    def show_book(self): #전체 책 출력함수
        bookcare.showbook1()
    def out(self): #프로그램 종료함수
        print("프로그램 종료")


import bookcare #bookcare 파일 import
while True: 
    n = Library() #객체
    print("1. 도서 추가 \n2. 도서 검색 \n3. 개별 검색 \n4. 도서 정보 수정 \n5. 도서 삭제 \n6. 도서 목록 출력  \n7. 프로그램 나가기")
    number = int(input("번호를 선택하세요: " ))
    if number == 1:
        n.add_book()
    elif(number == 2):
        n.search_book()
    elif(number == 3):
        n.data_book()
    elif(number == 4):
        n.revise_book()
    elif(number == 5):
        n.delete_book()
    elif(number == 6):
        n.show_book()
    elif(number == 7):
        break
n.out() 
       
