print("입력")
print_num = int(input("작업할 문서의 개수를 입력하세요 : "))
print_sequence = int(input("출력하고 싶은 작업을 입력하세요 : "))
print_rank = list(map(int,input("우선순위를 입력하세요 ").split()))

print_fast = list(range(len(print_rank)))
print_fast[print_sequence] = "print"
printing_time = 0

while True :
    if print_rank[0] == max(print_rank):
        printing_time = printing_time + 1
        if print_fast[0] == "print":
            print(printing_time, "분")
            break
        else :
            print_rank.pop(0)
            print_fast.pop(0)
    else:
        print_rank.append(print_rank.pop(0))
        print_fast.append(print_fast.pop(0))