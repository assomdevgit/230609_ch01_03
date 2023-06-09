# 불(bool) 과 비교, 논리 연산자
## 불과 비교 연산자 사용하기
'''
* 프로그램 -> 참, 거짓 판단 -> 참(True) : 어떠한 조건이나 수식을 만족시키는가? / 거짓(False)
* 불(Bool) 혹은 불리언(Boolean) : 참과 거짓으로 구성된 자료형
* 두 값의 관계를 판단하는 비교 연산자 | 두 값의 논리적 관계를 판단하는 논리 연산자
'''
print(True, False) # 다른 언어들은 대게 true, false
print(int(True), int(False)) # 1 , 0

# 비교 연산자 - 판단 결과
## 등호(가타, 다르다)와 부등호(크다, 작다) --> 비교하는 식이 맞으면 True
print("10 > 5", "10이 5보다 크다, 10은 5를 초과한다", 10 > 5)
print("10 < 5", "10이 5보다 작다, 10은 5를 미만이다", 10 < 5)
## 숫자가 같은지 다른지 비교
'''
* 일반적 수학에서는 =(등호)로 ㅆ는데, 파이썬 등 프로그래밍에서는 ==을 등로(동등 연산자, equal)로 쓴다.
'''
print("1 == 1 :", 1 == 1)

# 문자열 동등 여부 비교
print("'python' == 'phthon'", "python" == "python")
print("'Python' == 'python'", "Python" == "python")
print("'Python' != 'python'", "Python" != "python")

# 숫자 비교 : 부등호
print("1 < 2", 1 < 2) # 미만
print("1 > 2", 1 > 2) # 초과
print("1 <= 2", 1 <= 2) # 이하
print("1 >= 2", 1 >= 2) # 이상

# 객체가 같은지 다른지 비교하기
'''
* is, is not --> 연산자, ==, !=, 왜 is(~이다), is not(~는 ~가 아니다)
'''
print("1 == 1.0 :", 1 == 1.0)
#print("1 is 1.0 :", 1 is 1.0)
#print("1 is not 1.0 :", 1 is not 1.0)
# a = 1 is 1.0
# print("1 is 1.0 :", a)

print("'1' == 1 :",  '1' == 1)

# 논리 연산자
## 논리 연산자는 and, or, not, (연산자가 꼭 특수문자나 기호일 필요는 없음)
## 그리고(and) 연산
have_car = True
have_money = True
print("have_car and have_money :", have_car and have_money)
have_car = False
have_money = True
print("have_car and have_money :", have_car and have_money)
have_car = True
have_money = False
print("have_car and have_money :", have_car and have_money)
have_car = False
have_money = False
print("have_car and have_money :", have_car and have_money)

print(have_car & have_money) # 되긴하지만 권장하지 않음

# 또는(or) 연산
hungry = True
study = True
print("hungry or study :", hungry or study)
hungry = False
study = True
print("hungry or study :", hungry or study)
hungry = True
study = False
print("hungry or study :", hungry or study)
hungry = False
study = False
print("hungry or study :", hungry or study)

print("hungry | study :", hungry | study)


# not (논리값 -> bool) True -> False, False -> True
sleepy = True
print("sleepy", sleepy)
print("not sleepy", not sleepy)
# ! 은 없다.
# and, or, not -> not (1), and (2), or (3) <-- 우선 순위
print("not True and False or not Flase", not True and False or not False)

# 논리 연산자 + 비교 연산자 (무조건 비교 연산자가 먼저임)
# 비교 연산자를 통해서 값을 비교하고 이것을 통해 True 또는 False 결과값(Bool 같이 나옴)
# 산술 -> 비교 -> 논리 연산자 순. (그래도 괄호와 변수로 표한된 건 먼저 처리가 된 상태임.)
print("10 == 10 and 10 !=5", 10 == 10 and 10 != 5) # True
print("(10 == 10) and (10 != 5)", (10 == 10) and (10 != 5)) # True
print("10 > 5 or 10 <3", 10 > 5 or 10 < 3) # True
print("not 7 + 3 > 5", not 7 + 3 > 5) # False

# 정수, 실수, 문자열을 불(참,거짓)으로 만들기 /판별
'''
정수, 실수, 문자열 -> 불(bool) => bool(1)
'''
print('bool(1)', bool(1)) # True
print('bool(0)', bool(0)) # False
print("bool(-1)", bool(-1)) # True
print("bool('아무거나')", bool('아무거나')) # True
print("bool('')", bool('')) # False 빈 문자열만 False



