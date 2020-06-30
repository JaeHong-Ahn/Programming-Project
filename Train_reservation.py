import Train_sample
import copy
import sys

class Train_reservation:

    def __init__(self):
        self.trainData = Train_sample.TrainDB()
        self.trainUserData_checkYes = list()
        self.menu()
        self.inputTimeData = None

    def menu(self):
        print("""
        1) 빠른시간 기차 검색 및 예매
        2) 전체 기차 리스트 출력
        3) 나의 예매 현황 출력 및 예매 취소
        4) 프로그램 종료
        """)

        num = int(input())


        if num == 1:
            self.findTrain()
            self.menu()
        elif num == 2:
            self.showingTrainData()
            self.menu()
        elif num == 3:
            self.showingUserData()
        elif num == 4:
            sys.exit()
            
        else:
            print("1~4 사이의 값을 입력하여 주세요")
            self.menu()

    def findTrain(self):
        self.inputTime = input("탑승시간을 입력해주세요 ex. 0800 : ") #탑승시간 입력
        self.inputStart = input("출발지를 입력해주세요 ex.서울 : ") #출발지 입력
        self.inputNext = input("도착지를 입력해주세요 ex. 부산 : ") #도착지 입력
        self.inputSort = input("열차 종류를 입력해주세요 ex. KTX : ") # 열차 종류 입력

        copyData = copy.deepcopy(self.trainData.trainTable)
        for i in range(len(copyData)):
            if copyData[i][1] != self.inputStart:
                copyData[i] = [0, 0, 0, 0, 0]
            if copyData[i][2] != self.inputNext:
                copyData[i] = [0, 0, 0, 0, 0]
            if copyData[i][3] != self.inputSort:
                copyData[i] = [0, 0, 0, 0, 0]

        self.userFindDataIndex = self.searchTimeTrain(copyData)
        checkYes = int(input("예매하시겠습니까? 1. 예  2. 아니요 (그 외의 숫자를 입력하시면 메뉴로 돌아갑니다.): "))
        if checkYes == 1:
            if self.trainData.trainTable[self.userFindDataIndex][4] != 0:
                self.trainData.trainTable[self.userFindDataIndex][4] = self.trainData.trainTable[self.userFindDataIndex][4] - 1       
                self.trainUserData_checkYes.append(self.trainData.trainTable[self.userFindDataIndex]) #예매 정보를 저장하는 별도의 리스트 생성
                print("\n 입력하신 탑승시간 중 가장 근접한 시간의 기차가 예매되었습니다. \n")
            else:
                print("예약할 수 없습니다. \n")
                self.menu()
        elif checkYes == 2:
            print("예매를 하지 않으셨습니다. 메뉴로 돌아갑니다. \n")
            self.menu()
        else :
            print("메뉴로 돌아갑니다. \n")
            self.menu()

    def searchTimeTrain(self,copyData):
        copyData = copy.deepcopy(self.trainData.trainTable)
        for i in range(len(copyData)):
           copyData[i][0] = int(copyData[i][0][0]) * 60 + int(copyData[i][0][1])
        
        self.inputTime_calc = (int(self.inputTime[0]) *10 + int(self.inputTime[1])) * 60 + int(self.inputTime[2]) * 10 + int(self.inputTime[3])
        
        compareIndex = []
        for i in range(len(copyData)):
            compareIndex.append(abs(self.inputTime_calc - copyData[i][0]))

        findIndex = compareIndex.index(min(compareIndex))

        return findIndex

    def showingTrainData(self):
        for i in range(len(self.trainData.trainTable)):
            print(self.trainData.trainTable[i])

    def showingUserData(self):
        for i in range(len(self.trainUserData_checkYes)) :
            print(self.trainUserData_checkYes[i])

        if self.trainUserData_checkYes == None:
            print("예약된 상품이 없습니다. 메뉴로 돌아갑니다.")
            print("\n")
            self.menu()

        elif self.trainUserData_checkYes == []:
            print("예약된 상품이 없습니다. 메뉴로 돌아갑니다.")
            print("\n")
            self.menu()

        else :
            while True :
                checkCancel = int(input("1. 예매 내역 확인 2. 예매 취소하기 3. 메뉴로 돌아가기 "))

                if checkCancel == 1:
                    print(self.trainUserData_checkYes)

                elif checkCancel == 2:
                    for i in range (len(self.trainUserData_checkYes)):
                        print(i, '. ', self.trainUserData_checkYes[i])
                    checkPop = int(input("몇 번을 삭제하시겠습니까? : "))
                    self.trainUserData_checkYes[checkPop][4] = self.trainUserData_checkYes[checkPop][4] + 1
                    self.trainUserData_checkYes.pop(checkPop)
                    print("예약이 취소되었습니다. \n")

                    self.menu()

                elif checkCancel == 3:
                    print("예약이 취소되었습니다.")
                    self.menu()
                
                else :
                    print("1, 2, 3의 숫자 중에 입력해주시기 바랍니다.")

train_program = Train_reservation()

#고생많으셨습니다..