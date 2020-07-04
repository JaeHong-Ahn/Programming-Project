import os
import sys

# try:
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'input.txt')
Bookdata = open(my_file, 'r')
Book_line = Bookdata.readlines()
Check_Books = list()

for i in range(len(Book_line)):
    Check_Book = Book_line[i].split()

    Check_Books += Check_Book

Bookdata.close()
# except:
#     pass

class WelcomLibrary:
    def __init__(self,Book_line):
        self.Book_User = None #사용자가 직접 입력한 내용
        self.Book = None
        self.AddBook_Content = list()
        self.Plus_Book = []
        self.Plus_Book.append(Check_Books)
        self.menu()

    def menu(self):
        num = int(input("""
        1. 도서추가(도서명, 저자, 출판연도, 출판사명, 장르 입력)
        2. 도서 검색
        3. 도서 정보 수정
        4. 도서 삭제
        5. 현재 총 도서 목록 출력
        6. 저장
        7. 프로그램 나가기
        """))

        if num == 1:
            self.AddBook()
        elif num == 2:
            self.SearchBook()
        elif num == 3:
            self.RetouchBook()
        elif num == 4:
            self.KillBook()
        elif num == 5:
            self.ListBook()
        elif num == 6:
            self.StoreBook()
        elif num == 7:
            sys.exit()

        # elif num == 8:

        else :
            print("1~7의 숫자만 입력해주십시오")
            self.menu()

    def AddBook(self):#도서 추가(도서명, 저자, 출판연도, 출판사명, 장르 입력) #Clear
        print("""도서 추가를 선택하셨습니다.
        기억이 안나신다면 '미상'으로 적어주세요""")
        self.AddBook_name = input("도서명 : ")
        self.AddBook_writer = input("저자 : ")
        self.AddBook_year = input("출판연도 : ")
        self.AddBook_company = input("출판사명 : ")
        self.AddBook_genre = input("장르 : ") 
        self.AddBook_Content = self.AddBook_name.split() + self.AddBook_writer.split() + self.AddBook_year.split() + self.AddBook_company.split() + self.AddBook_genre.split()

        self.Plus_Book.append(self.AddBook_Content)

        print("입력하신 도서가 추가되었습니다.")

        self.menu()

    def SearchBook(self):#도서 검색(도서명, 저자, 출판연도, 출판사명, 장르 각각 검색 가능) #Clear
        print("\n 도서검색을 선택하셨습니다. ")
        print("""검색할 부분을 골라주세요
        1. 도서명
        2. 저자
        3. 출판연도
        4. 출판사명
        5. 장르      
        
        그 외의 숫자를 입력하시면 메뉴로 돌아갑니다.
        """)
        SearchBook_selectMenu = int(input())

        if SearchBook_selectMenu == 1: #도서명 검색
            print("\n 도서명 검색을 선택하셨습니다. 도서명을 입력해주세요 : ")
            SearchBook_selectMenu_name = input()
            for i in range (len(self.Plus_Book)):
                if self.Plus_Book[i][0] == SearchBook_selectMenu_name :
                    print(self.Plus_Book[i])
                    print("\n메뉴로 돌아갑니다. ")
                    self.menu()
                    
                else :
                    print("해당내용으로 입력된 도서가 없습니다. ") 
                    print("\n 메뉴로 돌아갑니다. ")                  
                    self.menu()

        elif SearchBook_selectMenu == 2:# 저자 검색
            print("\n 저자 검색을 선택하셨습니다. 저자명을 입력해주세요 : ")
            SearchBook_selectMenu_writer = input()
            for i in range (len(self.Plus_Book)):
                if self.Plus_Book[i][1] == SearchBook_selectMenu_writer :
                    print(self.Plus_Book[i])
                    print("\n메뉴로 돌아갑니다. ")
                    self.menu()

                else :
                    print("해당내용으로 입력된 도서가 없습니다. ") 
                    print("\n 메뉴로 돌아갑니다. ")                  
                    self.menu() 

        elif SearchBook_selectMenu == 3: #출판연도 검색
            print("\n 출판연도 검색을 선택하셨습니다. 출판연도를 입력해주세요 :")
            SearchBook_selectMenu_year = input()
            for i in range (len(self.Plus_Book)):
                if self.Plus_Book[i][2] == SearchBook_selectMenu_year :
                    print(self.Plus_Book[i])
                    print("\n메뉴로 돌아갑니다. ")
                    self.menu()

                else :
                    print("해당내용으로 입력된 도서가 없습니다. ") 
                    print("\n 메뉴로 돌아갑니다. ")                  
                    self.menu()          

        elif SearchBook_selectMenu == 4: #출판사명 검색
            print("\n 출판사 검색을 선택하셨습니다. 출판사를 입력해주세요 :")
            SearchBook_selectMenu_company = input()
            for i in range (len(self.Plus_Book)):
                if self.Plus_Book[i][3] == SearchBook_selectMenu_company :
                    print(self.Plus_Book[i])
                    print("\n메뉴로 돌아갑니다. ")
                    self.menu()
                    
                else :
                    print("해당내용으로 입력된 도서가 없습니다. ") 
                    print("\n 메뉴로 돌아갑니다. ")                  
                    self.menu()

        elif SearchBook_selectMenu == 5: # 장르 검색
            print("\n 장르 검색을 선택하셨습니다. 장르명을 입력해주세요 :")
            SearchBook_selectMenu_genre = input()
            for i in range (len(self.Plus_Book)):
                if self.Plus_Book[i][4] == SearchBook_selectMenu_genre :
                    print(self.Plus_Book[i])
                    print("\n메뉴로 돌아갑니다. ")
                    self.menu()
                    
                else :
                    print("해당내용으로 입력된 도서가 없습니다. ") 
                    print("\n 메뉴로 돌아갑니다. ")                  
                    self.menu()      

        else :#메뉴로 돌아가기
            print("\n 메뉴로 돌아갑니다. ")
            self.menu()

    def RetouchBook(self):#도서 정보 수정 - 수정할 도서명을 입력 받아 입력할 부분을 5가지로 분할하여 고른 뒤 수정 vs 해당 도서명의 내용을 입력받은 내용으로 덮어쓰기
        for i in range(len(self.Plus_Book)):
            print(i, '. ', self.Plus_Book[i])
        
        RetouchBook_input = int(input("\n수정할 도서의 번호를 입력해주세요 : " ))

        print("""
        수정할 파트 선택
        1. 도서명
        2. 저자
        3. 출판연도
        4. 출판사명
        5. 장르

        메뉴로 돌아가고 싶다면 그 외의 숫자를 입력해주세요 
        """)
        RetouchBook_inputs = int(input())

        if RetouchBook_inputs == 1:
            RetouchBook_bookname = input("도서명 수정 : ")
            self.Plus_Book[RetouchBook_input][0] = RetouchBook_bookname
            print("도서명이 {0}으로 수정되었습니다. ".format(RetouchBook_bookname))
            print("\n 메뉴로 돌아갑니다. \n")
            self.menu()

        elif RetouchBook_inputs == 2:
            RetouchBook_bookwriter = input("저자 수정 : ")
            self.Plus_Book[RetouchBook_input][1] = RetouchBook_bookwriter
            print("저자가 {0}으로 수정되었습니다. ".format(RetouchBook_bookwriter))
            print("\n 메뉴로 돌아갑니다. \n")
            self.menu()

        elif RetouchBook_inputs == 3:
            RetouchBook_bookyear = input("출판연도 수정 : ")
            self.Plus_Book[RetouchBook_input][2] = RetouchBook_bookyear
            print("출판연도가 {0}으로 수정되었습니다. ".format(RetouchBook_bookyear))
            print("\n 메뉴로 돌아갑니다. \n")
            self.menu()

        elif RetouchBook_inputs == 4:
            RetouchBook_bookcompany = input("출판사명 수정 : ")
            self.Plus_Book[RetouchBook_input][3] = RetouchBook_bookcompany
            print("출판사명이 {0}으로 수정되었습니다. ".format(RetouchBook_bookcompany))
            print("\n 메뉴로 돌아갑니다. \n")
            self.menu()

        elif RetouchBook_inputs == 5:
            RetouchBook_bookgenre = input("장르 수정 : ")
            self.Plus_Book[RetouchBook_input][4] = RetouchBook_bookgenre
            print("장르가 {0}으로 수정되었습니다. ".format(RetouchBook_bookgenre))
            print("\n 메뉴로 돌아갑니다. \n")
            self.menu()

        else :
            print("\n 메뉴로 돌아갑니다 .\n ")
            self.menu()

    def KillBook(self):#도서 삭제 - 총도서 목록을 출력한 뒤에 책 이름을 입력 받아 리스트의 내용과 비교후 삭제, 해당 도서명이 없을 경우 예외처리
        for i in range(len(self.Plus_Book)):
            print(i, '. ', self.Plus_Book[i])
        
        if self.Plus_Book != [] :
            num = int(input("\n 삭제할 도서의 번호를 입력해주세요 : "))
            self.Plus_Book.remove(self.Plus_Book[num])
            print("해당 도서가 삭제되었습니다. ")
            print("\n 메뉴로 돌아갑니다. ")
            self.menu()
        else :
            print("삭제할 도서가 없습니다.")
            print("\n 메뉴로 돌아갑니다. ")
            self.menu()

    def ListBook(self):#현재 총 도서 목록 출력
        if self.Plus_Book == []:
            print("현재 저장되어 있는 도서가 없습니다. ")
            self.menu()
        else :
            for i in range(len(self.Plus_Book)):
                print(self.Plus_Book[i])

            print("\n도서를 출력했습니다. 메뉴로 돌아갑니다.")
            self.menu()

    def StoreBook(self):#현재 내용 저장
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        self.StoreBook_final = open(my_file, 'r+')
        Userinput = str(input("작업 내용을 저장하시겠습니까? (y/n) : "))
        if Userinput == 'y':
            for i in range(len(self.Plus_Book)):
                self.StoreBook_final.writelines(" ".join(self.Plus_Book[i]))
                self.StoreBook_final.write("")
                print("저장되었습니다.")
                
            self.menu()
        elif Userinput == 'n':
            print("메뉴로 돌아갑니다.")
            return self.menu()
        else:
            print("y 또는 n 중에 하나의 값만 입력하세요.")
            return self.StoreBook()

        # StoreBook_return()
        # def StoreBook_return(self):
        #     StoreBook_input = int(input("\n 저장을 원하시면 1을, 저장 없이 메뉴로 돌아가시려면 2를 입력해주세요 : "))

        #     if StoreBook_input == 1:
        #         for i in range(len(self.Plus_Book)):
        #             StoreBook_final.writelines(" ".join(self.Plus_Book[i]))
        #             StoreBook_final.write("\n")
                
        #         print("저장이 완료되었습니다. 메뉴로 돌아갑니다. ")
                
        #         self.menu()
        #     elif StoreBook_input == 2:
        #         self.menu()
        #     else :
        #         return self.StorBook_return() #재귀함수!

        self.StoreBook_final.close()

Library_Program = WelcomLibrary(Book_line)