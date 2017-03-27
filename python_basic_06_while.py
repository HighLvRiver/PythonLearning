
# coding: utf-8

# ## while문의 기본 구조
# 
# 반복해서 문장을 수행해야 할 경우 while문을 사용한다. 그래서 while문을 반복문이라고도 부른다.
# 
# 다음은 while문의 기본 구조이다.
# 
# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     ...
# 
# while문은 조건문이 참인 동안에 while문 아래에 속하는 문장들이 반복해서 수행된다.
# 
# "열 번 찍어 안 넘어 가는 나무 없다" 라는 속담을 파이썬 프로그램으로 만든다면 다음과 같이 될 것이다.

# In[1]:

treeHit = 0


# In[2]:

while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


# 위의 예에서 while문의 조건문은 treeHit < 10 이다. 
# 즉, treeHit가 10보다 작은 동안에 while문 안의 문장들을 계속 수행한다. whlie문 안의 문장을 보면 제일 먼저 treeHit = treeHit + 1로 treeHit 값이 계속 1씩 증가한다. 그리고 나무를 treeHit번만큼 찍었음을 알리는 문장을 출력하고 treeHit가 10이 되면 "나무 넘어갑니다."라는 문장을 출력한다. 그러고 나면 treeHit < 10 이라는 조건문이 거짓이 되므로 while문을 빠져나가게 된다.
# 
# (※ treeHit = treeHit + 1 은 프로그래밍을 할 때 매우 자주 사용하는 기법이다. treeHit의 값을 1만큼씩 증가시킬 목적으로 사용되며, treeHit +=1 처럼 사용되기도 한다.)

# 다음을 직접 입력해 보자. 여러 가지 선택지 중 하나를 선택해서 입력받는 예제이다. 먼저 다음과 같이 여러 줄짜리 문자열을 만들어 보자.

# In[3]:

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """


# In[4]:

number = 0

while number != 4:
    print(prompt)
    number = int(input())


# ## while문 강제로 빠져나가기
# 
# while문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복적으로 수행한다. 하지만 강제로 while문을 빠져나가고 싶을 때가 있다. 예를 들어 커피 자판기를 생각해 보자. 자판기 안에 커피가 충분히 있을 때에는 동전을 넣으면 커피가 나온다. 그런데 자판기가 제대로 작동하려면 커피가 얼마나 남았는지 항상 검사해야 한다. 만약 커피가 떨어졌다면 판매를 중단하고 "판매 중지"라는 문구를 사용자에게 보여주어야 한다. 이렇게 판매를 강제로 멈추게 하는 것이 바로 break문이다.
# 
# 다음의 예는 커피 자판기 이야기를 파이썬 프로그램으로 표현해 본 것이다.

# In[5]:

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


# In[6]:

# coffee.py

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break


# ## 조건에 맞지 않는 경우 맨 처음으로 돌아가기
# 
# while문 안의 문장을 수행할 때 입력된 조건을 검사해서 조건에 맞지 않으면 while문을 빠져나간다. 그런데 프로그래밍을 하다 보면 while문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우가 생기게 된다. 이때 사용하는 것이 바로 continue문이다.
# 
# 만약 1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while문을 이용해서 작성한다고 생각해 보자. 어떤 방법이 좋을까?

# In[10]:

a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
    

