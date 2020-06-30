class TrainDB:
    def __init__(self):
        open_trainlist = open(r"C:\Users\HOME\Desktop\Taken\TrainList.txt", 'r')
        contents = open_trainlist.readlines()
        contents = contents[1:]

        self.trainTable = list()
        for c in contents:
            c = c.replace('->', '')
            line = c.split()
            line[-1] = int(line[-1])
            line[0] = line[0].split(':')
            self.trainTable.append(line)

# class compare_train_user:
#     def __init__(self):
#         # self.table = list()
#         # for c in contents:
#         #     c = c.replace('->', '')
#         #     line = c.split()
#         #     line[-1] = int(line[-1])
#         #     line[0] = line[0].split(':')
#         #     line[0] = int(line[0][0])*60 + int(line[0][1])
#         #     table.append(line)
#         self.DB = 3

#     def compare_everything(self):
#         time = input("탑승시간을 입력해주세요(ex. 0830) : ")
#         start = str(input("희망 출발지를 입력해주세요(ex. 서울) : "))       
#         last = str(input("희망 도착지를 입력해주세요(ex. 부산) : "))
#         sort = str(input("희망하는 열차 종류를 입력해주세요(ex. KTX) : "))

#         # time = list(time)
#         minus = []
#         user_time = int(time[0:2]) * 60 + int(time[2:4])
#         for i in range(20):
#             minus.append(abs(user_time -table[i][0]))
#             # if minus > 0 :
#             #     return minus
#             # else:
#             #     return minus * (-1)

#             #minus = sorted(minus)

#             if table[i][1] == start and table[i][2] == last and table[i][3] == sort :

#                 table[i][0] = str(table[i][0]//60) + ":" + str(table[i][0]%60) 
#                 if len(table[i][0]) < 5:
#                     table[i][0] = "0"+table[i][0]
#                 print(table[i])
#             else :
#                 pass
#         return table
            
# a = compare_train_user()
# a.compare_everything()