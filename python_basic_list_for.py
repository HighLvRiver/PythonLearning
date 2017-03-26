
# coding: utf-8

# # 파이썬에서 반복문을 사용하여 계산하기
# 
# 반복문은 리스트 자료형 변수에 대해 여러가지 계산을 할 때 많이 사용된다.
# 
# 예를 들어 10번의 시험 성적을 담고 있는 a라는 변수가 있을 때 평균 성적은 다음과 같이 구할 수 있다.
# 
# 다음 코드에서 len() 명령어는 리스트 자료형 변수의 원소의 갯수를 구하는 명령어이다.

# In[1]:

a = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
a


# In[2]:

len(a)


# In[3]:

sum = 0
for i in range(len(a)):
    sum = sum + a[i]
average = sum / len(a)    
average


# 만약 학생이 두 명이고 이런 성적 변수가 두 개 있을 경우를 생각하자. 
# 두 학생의 시험 성적의 합은 다음과 같이 구할 수 있다.

# In[4]:

s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a1 = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
a2 = [95, 90, 90, 90, 95, 100, 90, 80, 95, 90]
for i in range(len(s)):
    s[i] = a1[i] + a2[i]
s


# 학생이 5명이라면 다음과 같이 리스트의 리스트로 데이터를 나타낼 수 있다.

# In[5]:

X = [[ 85,  90,  20,  50,  60,  25,  30,  75,  40,  55],
     [ 70, 100,  70,  70,  55,  75,  55,  60,  40,  45],
     [ 25,  65,  15,  25,  20,   5,  60,  70,  35,  10],
     [ 80,  45,  80,  40,  75,  35,  80,  55,  70,  90],
     [ 35,  50,  75,  25,  35,  70,  65,  50,  70,  10]]


# In[6]:

sum = 0
num = 0
for i in range(len(X)):
    for j in range(len(X[i])):
        num = num + 1
        sum = sum + X[i][j]
sum / num


# 연습문제1
# 
# 어떤 학생이 5개의 과목을 수강하여 다음과 같은 성적(grade)을 받았다. (4점이 만점)
# 
# X=4,3,2,3,4
#  
# 이 5개 과목의 이수 학점(credit hours)은 각각 다음과 같다.
# 
# W=3,3,1,2,2
#  
# 이 때 평균 평점(GPA)은 성적의 단순 평균이 아니라 이수 학점을 가중치(weight)로 써서 다음과 같이 가중 평균을 구해야 한다.
# 
# (성적과 이수 학점을 곱한 값의 총합 즉, 가중합 ) / 이수 학점의 총합=(3×4+3×3+1×2+2×3+2×4)/(3+3+1+2+2)
# 
# i 번째 과목의 성적을  Xi 라고 하고  i 번째 과목의 이수 학점을  Wi 라고 하면 가중 평균은 다음과 같은 수식으로 나타낼 수도 있다.
# 
# (W1X1+W2X2+W3X3+W4X4+W5X5) / (W1+W2+W3+W4+W5)
#  
# 이 학생의 평균 평점을 구하는 코드를 작성한다.

# In[9]:

X = [4, 3, 2, 3, 4]
W = [3, 3, 1, 2, 2]

sum = 0
num = 0

for i in range(len(X)):
    sum = sum + X[i] * W[i]
    num = num + W[i] 

sum / num


# In[ ]:



