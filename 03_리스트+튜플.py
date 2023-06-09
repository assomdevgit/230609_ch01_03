# 리스트와 튜플
## 리스트 : 1개 이상의 연속된ㄴ 값들의 묶음
# 30개의 숫자를 저장(1-30)
# 리스트(list) : 목록 --> 값을 일렬로 (순서가 있게) 늘어놓은 형태
'''
* 변수에 값을 저장할 때 [](대괄호)로 묶어주면 리스트가 됨.
* 리스트 = [값1, 값2, ... ]
'''
#from builtins import tuple

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

# 튜플(tuple)
'''
* 리스트처럼 요소(원소, element)
* 튜플은 요소를 수정할 수 없음 (read only)
* 리스트가 []라면, 튜플은 ()입니다.
* 튜플 = (값1, 값2, 값3 ...)
* 튜플 = 값1, 값2, 값3 ...
'''
# 숫자가 5개 들어있는 튜플
a1 = (23, 38, 12, 11, 7)
print(a1)
a2 = 23, 38, 12, 11, 7
print(a2)
a3 = '파이썬', 2, 3, 5
print(a3) # 튜플도 리스트처럼 자료형의 혼합이 가능

# range를 사용해서 튜플 만들기
# list(...) => range => list
# tuple(...) => range => tuple
print(tuple(range(10)))

# tuple을 list로 변환하고, list를 tuple로 변환하고 싶으면?
a = list(range(10))
print(a)
b = tuple(a)
print(b)
c = tuple(range(5, 25, 5))
print(c)
d = list(c)
print(d)

# 리스트와 튜플로 변수 만들기
'''
* 리스트 또는 튜플을 사용하면 변수 여러 개를 한 번에 만들 수 있음
* 이 때 (만들려는) 변수와 개수와 리스트(튜플)의 요소 개수는 같아야 함.
'''
l = [1, 2, 3]
a, b, c = l
print("a:", a, "b:", b, "c:", c)
t = ("dog", "cat", "tiger")
d, e, f = t
print("d:", d, "e:", e, "f:", f)

a, b, c = [1, 2, 3] # 리스트를 분해해서 각각의 변수에 집어 넣는 것? : 리스트 언팩킹
print("a:", a, "b:", b, "c:", c)

y = 10, 100, 1000 # 튜플 팩킹
l = [10, 100, 1000] # 리스트 팩킹
a, b, c = y
print(a, b, c)
print(l)

t = (1, 2, 3)
a, b, c = t
print(t)

#
s = [1, 2, 3, 4, 10, 11, 12, 13, 14]
a, b, c, d, e, f, g, h, i = s
print("서로 대입하는 수가 다를 경우:", a, b, c, d)

l, m, n = 1, 2, 3
print("오류가 있음", l, m, n)






