# int 타입의 변수 선언
# NumberZero라는 이름의 변수를 만들고 여기에 숫자 0을 넣어주세요.
NumberZero = 0

# float 타입의 변수 선언
# FloatSix라는 이름의 변수를 만들고 여기에 실수 6.0을 넣어주세요.
FloatSix = 6.0 

# char 타입의 변수 선언
# CharA라는 이름의 변수를 만들고 여기에 문자 A를 넣어주세요.
CharA = 'A'

# bool 타입의 변수 선언
# IsTrue라는 이름의 변수를 만들고 여기에 True 값을 넣어주세요.
IsTrue = True


# 입력 받기
# Input변수 = 입력기('입력 받을 때 표시 될 문구')
Input = input('input the number : ')
# 출력(Input변수)
print(Input)


# For 반복문
# 반복 [0부터5까지]:
for i in range(0,5):
#   출력기('a')
    print('a')


#  While 반복문 
# Condition 변수 = 참
Condition = True
# 반복 [Condition 변수가 참인 동안]
while Condition:
#    출력기('*')
    print('*')
    
#### 위 While 문 예시는 무한 반복이므로 아래 while 문 예시를 테스트 하시려면 위의 구문을 주석 처리(#) 혹은 지우고 테스트 해주세요.


# While 반복문 응용
# CurrentInput 변수 = -1
CurrentInput = ''
# 반복 [CurrentInput 변수가 0이 아닌 동안]
while CurrentInput != '0':
    # CurrentInput 변수 = 입력기('숫자를 입력해주세요. (0을 입력하면 멈춥니다.')
    CurrentInput = input('input the word (for break input 0) : ')
    # 출력('지금 입력된 단어는 ->')
    print('Current Input word is -> ')
    # 출력(CurrentInput 변수)
    print(CurrentInput)
    