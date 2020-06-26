""" 1.현재 queue의 가장 앞에 있는 문서의 우선순위를 확인한다.
2. 나머지 문서들 중 현재 문서보다 우선순위가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 queue의 가장 두에 재배치한다.
그렇지 않다면 바로 인쇄를 한다.
3. 모든 작업은 1~9까지의 우선순위를 가진다.(9가 우선순위가 제일 높음)
4. 모든 작업은 프린터 소요시간이 1분이라고 하자

1. 작업 수/작업 번호를 입력받는다
2. 작업의 우선순위를 입력받는다.
3. 입력받은 작업 번호를 9부터 1까지 내림차순으로 정렬한다.
4. 출력으로 나오는 프린터 소요시간은 내림차순한 뒤 해당 작업의 위치까지의 시간 +1분이다 """

print("입력")

num = int(input("작업수/ 작업 번호 : "))
print_num = int(input())

priority = list(map(int, input("작업 우선순위 : ").split()))

d = sorted(priority)
d.reverse()

time = 0

for i in range(num):
    if priority[print_num] == d[i]:
        print("출력 : {}분".format(time+1))
        break
    else :
        time = time + 1

# 1번 코드 설명
# 원래 문제풀이 방식은 순차적으로 우선순위를 확인한뒤
# 우선순위가 해당 리스트 안에서 max가 아니면 뒤로 보내는
# 형식으로 했었다면, 이번 방식은 받은 우선순위를 오름차순으로 정렬한뒤
# 이를 reverse하여 큰 숫자부터 작은 숫자순으로 나열시킴.
# 그 다음 우선순위와 작업번호를 연관지어 출력함.

print("입력")
num = int(input("작업 수 : "))
print_num = int(input("작업 번호 : "))
priority = list(map(int,input("우선순위 : ").split()))

d = list(range(len(priority)))
d[print_num] = "print"
time = 0

while True :
    if priority[0] == max(priority):
        time = time + 1
        if d[0] == "print":
            print(time, "분")
            break
        else :
            priority.pop(0)
            d.pop(0)
    else:
        priority.append(priority.pop(0))
        d.append(d.pop(0))

# 2번코드 설명
# 작업 수, 작업 번호를 입력받고 우선순위를 입력받는다.
# list(map())을 통해 원래 우선순위 리스트는 그대로 두고, 
# 순차대로 우선순위를 비교하는데, 해당 숫자가 리스트에서 max가 아니면
# pop을 통해 빼고, pop으로 뺀 것을 리스트의 맨 뒷부분에 append하는 방식이다.
# 이렇게 하면 예제대로 1 1 9 1 1 1을 입력받았을때, 0번째의 1의 출력시간이
# 5분이 나올수 있게 된다.