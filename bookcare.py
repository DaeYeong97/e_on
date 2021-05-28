def addbook1():
    book = input("도서명, 저자, 출판연도, 장르 순서대로 입력세요: ") #책 입력
    f = open("C:/Python_Cd/input.txt","a") #파일 오픈(사라지지않고 쓰기 위해서 a)
    f.write("\n"+ book) #입력받은 책 저장
    print("도서추가 완료했습니다.\n")
    f.close()
def searchbook1():
        import glob 
        import re #모듈 선언
        
        search_book = input("검색할 단어를 입력하세요: ")
        booklog1 = re.compile(search_book) #검색할 단어를 booklog1의 저장
        for i in glob.glob(r"C:/Python_Cd/input.txt"):
            with open(i, "r") as f:
                 for x, y in enumerate(f.readlines(),1):
                    Target_book = booklog1.findall(y) #찾는 도서나 연도 찾아 변수에 저장
                    if Target_book: #있으면
                        print("관련 도서목록 : %s" %y) #출력
def databook1():
    with open("C:/Python_Cd/input.txt","r") as f:
        book_num = int(input("1. 도서명\n2. 저자\n3. 출판연도\n4. 출판사명\n5. 장르\n"))
        while True:
            X_1 = f.readline()
            if not X_1:
                break
            looking_B = X_1.split(" ")
            if book_num == 1:
                print(looking_B[0])
            elif book_num ==  2:
                print(looking_B[1])
            elif book_num == 3:
                print(looking_B[2])
            elif book_num == 4:
                print(looking_B[3])
            elif book_num == 5:
                print(looking_B[4])
    searchbook1()
                    
            
                      
def revisebook1():
    new_text = " "
    target = input("수정하고 싶은 부분을 적어주세요: ")
    newword = input("변경하고 싶은 단어를 넣어주세요: ")
    with open("C:/Python_Cd/input.txt","r") as f:
        lines = f.readlines() #lines에 전체 파일 목록 저장 
        for i, l in enumerate(lines):# 해당 도서명을 번호로 나열
            new_string = l.strip().replace(target, newword) #대체
            if new_string: #해당 단어가 존재하면
                new_text += new_string + "\n" #대체
            else: # 아니면
                new_text += "\n" #반환
    with open("C:/Python_Cd/input.txt","w") as f:
        f.write(new_text)
    print("수정되었습니다. \n")
def deletebook1():
    with open("C:/Python_Cd/input.txt","r") as infile:
        lines = infile.readlines() #전체 도서목록을 변수에 저장
    f = open("C:/Python_Cd/input.txt","r")
    li_num = 1
    line = f.readline()
    while line:
        print("%d. %s" %(li_num,line))
        line = f.readline()
        li_num += 1 #해당 도서목록을 번호대로 출력
    f.close
    cancel_num = int(input("삭제할 번호를 입력하세요: "))
    with open("C:/Python_Cd/input.txt","w") as outfile:
        for i, line in enumerate(lines):
            if i != cancel_num-1: #파일 번호와 일치하지 않은 것만 출력
                outfile.write(line) #번호가 일치하는건 삭제 후 출력
    print("삭제되었습니다. \n")
def showbook1():
    f = open("C:/Python_Cd/input.txt","r")
    x = f.read()
    print(x)
    f.close()

        



    

