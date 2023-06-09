# 문자열
# "" 혹은 ''를 묶여진 글자들의 묶음
text = "Hello World"
print(text) # 출력

# 한글 문자열
korean = "먹어도 먹어도 배고프다"
print(korean)

# 문자열 만들기 : " " (큰따옴표)로 묶기
double_quotation = "my name is python"
print(double_quotation) # ctrl + space (처음완성 or 기능 추천)

single_quotation = 'my name is python'
print(single_quotation)

# '''...'''로 묶거나 """..."""로 묶기
t1 = '''hello guys'''
t2 = """hello guys"""
print(t1, t2)

# 여러 줄로 된 문자 사용
a1 = '''green red
red green
hello buy'''
print(a1)
print("green red\nred green\nhello buy")

# 여러 줄로 된 문자열은 큰따음표나 작은따음표 3개로 시작해서 3개로 마쳐주면 된다.
# 여러줄 주석 <- 실제로는 여러 줄 문자열인데... -> 이걸 저장하는 변수나 실행하는 구문
text = "이름하여' 파이썬!"
print(text)
text = "\"" # \" ,- 큰따옴표 사용가능
print(text)

t1 = '''
작은다옴표(')
큰다음표(")
'''
print(t1)
t2 = '''
작은다옴표(')
큰다음표(")
'''
print(t2)





