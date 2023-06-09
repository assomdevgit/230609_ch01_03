# 리스트와 튜플
## 리스트 : 1개 이상의 연속된ㄴ 값들의 묶음
# 30개의 숫자를 저장(1-30)
# 리스트(list) : 목록 --> 값을 일렬로 (순서가 있게) 늘어놓은 형태
'''
* 변수에 값을 저장할 때 [](대괄호)로 묶어주면 리스트가 됨.
* 리스트 = [값1, 값2, ... ]
'''
fruits = ['apple', 'banana', 'cherry']
print(fruits)
numbers = [10, 40, 27]
print(numbers)

# 리스트에는 여러 가지 자료를 저장
teacher = ["김강사", 180, 70.9, True] # 리스트 내용 --> 다 같은 타입이 되도록 제한
print(teacher)
print(type(teacher))

# 빈 리스트 만들기
'''
* 빈 리스트를 만들 때는 [] 만 사용하거나, list()를 사용하면 됨.
'''
a = []
print(a)
b = list()
print(b)

# range를 사용하여 리스트 만들기
'''
* 연속된 숫자를 생성하는 기능
range(10) : 0~9 시작은 0부터 하고, 끝은 입력한 값 직전 (10->9)
'''
print(range(10)) # range(n) : 0부터 n 직전까지의 숫자를 생성
# range(0,10)
print(list(range(10)))

# 수를 나열한 리스트를 만들 때
# 리스트 = list(range(횟수)) : 횟수

# 시작점과 끝점이 모두 있는 range
r = range(8, 14)
print(list(r)) # 8-13 range(8,14) --> list(range(8,14))

# 시작점과 끝점, 증가폭
r2 = range(100, 1000, 100)
print(list(r2)) # 100씩 증가 range(100,1000,100) --> list(range(100,1000,100))

r3 = range(1000, 100, -100)
print(list(r3))





