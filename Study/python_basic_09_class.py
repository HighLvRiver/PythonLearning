
# coding: utf-8

# # 파이썬 객체지향 프로그래밍 기초
# 
# ## 객체
# 
# 프로그램이 어떤 작업을 수행하기 위해서는 (1)데이터와 (2)데이터를 조작하는 행위, 두 가지 요소가 필요하다. 일반적으로 데이터는 변수(variable)에 넣어서 사용하고 데이터를 조작하는 일은 함수(function)로 구성해서 쉽게 실행시킬 수 있도록 만들어 놓는다.
# 
# 객체(object)는 서로 연관된 데이터와 그 데이터를 조작하기 위한 함수를 하나의 집합에 모아놓은 것을 말한다.
# 
# 집합의 원소가 되는 변수나 함수는 멤버(member) 또는 속성(attribute)이라고 한다. 특히 객체에 합쳐진 함수는 함수가 아니라 메서드(method)라고 부른다.

# 예를 들어 사각형의 면적을 구하는 프로그램을 만든다고 하자. 필요한 변수와 함수는 다음과 같다.
# 
# 가로 길이와 세로 길이라는 두 개의 데이터를 넣을 변수
# 두 길이를 곱해서 면적을 구하는 함수
# 객체지향을 사용하지 않고 파이썬으로 구현하면 다음과 같아진다.

# In[1]:

h = 10
v = 20

def area(h, v):
    return h * v

a = area(h, v)
print(a)


# 위 프로그램에서 사각형의 가로 길이를 나타내는 변수 h, 사각형의 세로 길이를 나타내는 변수 v, 그리고 이 사각형의 면적을 계산하는 함수 area()는 제각기 떨어져 있다. 하지만 객체 지향 프로그래밍에서는 이 세가지를 하나의 객체(object)로 묶을 수 있다.
# 
# 다음은 이 프로그램을 객체 지향 방식으로 다시 구현한 것이다.

# In[2]:

class Rectangle(object):
    
    def __init__(self, h, v):
        self.h = h
        self.v = v
        
    def area(self):
        return self.h * self.v


# 이 부분은 클래스(class) 구현이라고 한다. 실제로 길이 변수들을 저장하고 면적을 계산하는 코드는 다음과 같다.

# In[3]:

r = Rectangle(10, 20)    
a = r.area()
print(a)


# 위 프로그램에서 r이 바로 객체이다. 
# 
# 객체 r은 사각형의 가로 길이와 세로 길이를 나타내는 변수 h와 v 그리고 면적을 계산하는 함수 area()가 합쳐져서 만들어진 것이다. 객체 r에 포함된 이 변수들과 함수, 즉 속성을 꺼내려면 객체 이름 뒤에 점(.)을 붙인 다음 속성 이름을 치면 된다. 다음과 같이 입력해 보면 알 수 있다.

# In[4]:

r.h


# In[5]:

r.v


# In[6]:

r.area()


# ## 클래스
# 
# 객체 지향 프로그래밍에서 객체를 만들려면 객체를 바로 만들지 못하고 항상 클래스(class)라는 것을 만든 후에 그 클래스를 이용하여 객체를 만들어야 한다.
# 
# 위 예제에서 Rectangle은 클래스이고 r은 Rectangle 클래스로 만들어진 객체이다. 객체와 클래스의 관계는 "붕어빵"과 "붕어빵을 굽는 틀"에 비유할 수 있다. 즉, 정해진 속성, 여기에서는 가로 길이 h와 세로 길이 v라는 속성을 가지도록 사각형 클래스를 한 번 만들어 놓으면 이 속성을 가지는 실제 사각형은 얼마든지 많이 만들 수 있다.

# 예를 들어 위에서 만들어 놓은 Rectangle 클래스로 다음과 같이 5개의 사각형을 만들 수도 있다.

# In[7]:

a = Rectangle(1, 1)   # 가로 1, 세로 1인 사각형
b = Rectangle(2, 1)   # 가로 2, 세로 1인 사각형
c = Rectangle(4, 2)   # 가로 4, 세로 2인 사각형
d = Rectangle(6, 3)   # 가로 6, 세로 3인 사각형
e = Rectangle(8, 5)   # 가로 8, 세로 5인 사각형


# In[8]:

print(a.area())
print(b.area())
print(c.area())
print(d.area())
print(e.area())


# ## 생성자
# 
# 파이썬에서 클래스를 정의하는 문법은 다음과 같다.
# 
# class 클래스이름(object):
# 
#     def __init__(self, 속성값1, 속성값2, 속성값3):
#         self.속성이름1 = 속성값1
#         self.속성이름2 = 속성값2
#         self.속성이름3 = 속성값3
#         
# 이 때 속성값 인수는 필요하지 않다면 없어도 된다.
# 
# 여기에서 class 블럭안에 정의된 __init__란 함수는 생성자(constructor)라고 하며 클래스 정의에서 가장 중요한 함수이다.
# 
# 객체를 생성할 때는 클래스이름이란 이름을 가진 함수를 호출해야 하는데 이 때 실제로는 __init__로 정의된 생성자 함수가 호출된다. 생성자 함수 내부에서는 생성자를 호출할 때 넣은 입력 변수, 즉 인자의 값을 속성값으로 저장한다.

# 연습문제1
# 
# 
# 삼각형의 넓이를 계산하기 위한 클래스를 만든다. 이 클래스는 다음과 같은 속성을 가진다.
# 
# 밑변의 길이 b 와 높이 h
# 삼각형의 넓이를 계산하는 메서드 area

# In[9]:

class Triangle(object):

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h / 2

t = Triangle(10,4)
a = t.area()
print(a)


# 연습문제 2¶
# 
# 사각 기둥의 부피를 계산하기 위한 클래스를 만든다. 이 클래스는 다음과 같은 속성을 가진다.
# 
# 밑면의 가로 길이 a, 밑면의 세로 길이 b, 높이 h
# 부피를 계산하는 메서드 volume
# 겉넓이를 계산하는 메서드 surface

# In[10]:

class Q_Prism(object):

    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def volume(self):
        return self.a * self.b * self.h

    def surface(self):
        return 2 * (self.a * self.b + self.a * self.h + self.b * self.h)

a = Q_Prism(10,20,15)
v = a.volume()
s = a.surface()


# In[11]:

print(v)
print(s)


# 게임 캐릭터와 객체
# 
# 컴퓨터 게임에 사용되는 플레이어의 캐릭터는 객체 지향 프로그램을 통해 만든다고 생각해 보자. 캐릭터의 능력치, 경험치 등의 숫자는 캐릭터마다 다르게 관리되어야 하므로 객체의 속성이 될 수 있다. 또한 모든 캐릭터 조작에 공통적으로 필요한 이동, 공격 등의 조작은 메서드로 구현할 수 있을 것이다.
# 
# 플레이어의 캐릭터
# 
# 속성: 캐릭터의 능력치, 경험치 등
# 메서드: 캐릭터를 움직이는 방법, 이동, 공격 등
# 
# 이를 기반으로 캐릭터를 만들어내는 Character라는 클래스를 만든다. 이 클래스로 만든 캐릭터는 1000 이라는 life 속성값을 가지고 생성되며 게임상에서 공격받을 경우에는 attacked라는 메서드가 호출되어 life 속성값을 10만큼 감속시키고 공격 받았음을 표시한다.

# In[12]:

class Character(object):
    
    def __init__(self):
        self.life = 1000
    
    def attacked(self):
        self.life -= 10
        print("공격받음! 생명력 =", self.life)   


# 이 클래스로 a, b, c 세 개의 캐릭터 객체를 생성한다.

# In[13]:

a = Character()
b = Character()
c = Character()


# 모든 객체의 초기 life 속성값은 모두 1000이다.

# In[14]:

a.life, b.life, c.life


# 하지만 공격을 받은 캐릭터의 생명력은 감소된다.

# In[15]:

a.attacked()


# In[16]:

b.attacked()


# In[17]:

a.attacked()
a.attacked()
a.attacked()
a.attacked()
a.attacked()


# In[18]:

a.life, b.life, c.life


# ## 클래스 상속
# 
# 이제 클래스 상속(class inheritance)이라는 개념을 생각한다. 위에서 만들어 본 클래스는 모든 캐릭터에 공통적인 life 속성만을 가지고 있었다. 하지만 만약 캐릭터도 전사(Warrior), 마법사(Wizard) 등 다양한 직업을 가진 캐릭터가 있고 각 캐릭터들은 서로 다른 초기 속성값을 가지고 태어난다면 어떻게 프로그램해야 할까? 각각의 직업 캐릭터를 별도의 클래스로 만들어도 되겠지만 클래스 상속을 사용하면 이미 만들어진 클래스 코드를 재사용하여 다른 클래스를 생성할 수 있다. 즉, 상속 과정에서 공통적으로 사용하는 속성이나 메서드는 두 번 반복해서 코딩할 필요가 없다. 이 때 상속을 받는 클래스를 자식 클래스(child class), 상속의 대상이 되는 클래스를 부모 클래스(parent class)라고 한다.
# 
# Character 부모 클래스에서 상속을 통해 Warrior 라는 자식 클래스와 Wizard 라는 자식 클래스를 만든다 상속을 위한 파이썬 문법은 다음과 같다.
# 
# class 자식클래스이름(부모클래스이름):
# 
#     def __init__(self, 속성값1, 속성값2):
#         super(자식클래스이름, self).__init()
#         자식 클래스의 초기화 코드
# 
# 사실 우리가 지금까지 쓰던 클래스 정의를 살펴보면 object라는 부모 클래스에서 상속을 받는 것이었다.
# 
# 이 코드에서 super(자식클래스이름, self).__init() 부분은 부모 클래스의 초기화 생성자를 호출하는 부분이다. 예를 들어 Warrior 라는 클래스에서 부모 클래스인 Character 클래스의 생성자를 호출하면 life라는 속성값을 초기화하므로 자식 클래스에서는 이 속성값을 초기화해줄 필요가 없다.
# 

# In[19]:

class Warrior(Character):
    
    def __init__(self):
        super(Warrior, self).__init__()
        self.strength = 15
        self.intelligence = 5


# In[20]:

class Wizard(Character):
    
    def __init__(self):
        super(Wizard, self).__init__()
        self.strength = 5
        self.intelligence = 15


# 이 클래스의 객체를 만들어 보면 명시적으로 만들지 않았지만 life라는 속성과 attacked 라는 메서드를 가진다.

# In[21]:

a = Warrior()
b = Wizard()


# In[22]:

a.life, b.life


# In[23]:

a.strength, b.strength


# In[24]:

a.intelligence, b.intelligence


# In[25]:

a.attacked()


# In[26]:

b.attacked()


# ## 메소드 오버라이딩
# 
# 메소드 오버라이딩(Method Overriding) 여러 클래스에 걸쳐서 같은 이름의 메서드를 만드는 것이다. 예를 들어 부모 클래스, 전사 캐릭터 클래스, 마법사 캐릭터 클래스에 공통적으로 attack 이라는 메서드가 있지만 각각의 하는 일이 다른 경우에는 다음과 같이 같은 이름의 메서드를 클래스 별로 구현하면 된다. 이렇게 되면 부모 클래스에서 만든 메서드 정의를 자식 클래스에서는 변경해서 사용한다.

# In[27]:

class Character(object):
    
    def __init__(self):
        self.life = 1000
        self.strength = 10
        self.intelligence = 10
        
    def attacked(self):
        self.life -= 10
        print("공격받음! 생명력 =", self.life) 
        
    def attack(self):
        print("공격!")      


# In[28]:

class Warrior(Character):
    
    def __init__(self):
        super(Warrior, self).__init__()
        self.strength = 15
        self.intelligence = 5
        
    def attack(self):
        print("육탄 공격!") 


# In[29]:

class Wizard(Character):
    
    def __init__(self):
        super(Wizard, self).__init__()
        self.strength = 5
        self.intelligence = 15
        
    def attack(self):
        print("마법 공격!") 


# In[30]:

a = Character()
b = Warrior()
c = Wizard()


# In[31]:

a.attack()


# In[32]:

b.attack()


# In[33]:

c.attack()


# In[34]:

a.attacked()


# In[36]:

b.attacked()


# ## 참조: 오버로딩 Overloading
# 
# 이와 비슷한 이름으로 오버로딩(Overloading)이라는 것이 있는데 이는 전혀 다른 개념이다. 오버로딩은 같은 메서드가 인수의 자료형이나 갯수를 다르게 받을 수 있는 것을 말한다. C++, Java 등에서는 지원하지만 파이썬에서는 오버로딩을 지원하지 않으므로 프로그래머가 내부적으로 알아서 처리해야 한다
# 
# 다음은 C++에서 오버로딩을 지원하는 함수 선언의 예이다.
# 
# float length(list p1, list p2);                  // 점 (p1[0], p1[1]) - (p1[0], p1[1]) 까지의 길이
# float length(int x1, int y1, int x2, int y2);    // 점 (x1, y1) - (x2, y2) 까지의 길이

# 연습문제 3
# 
# 위의 게임 캐릭터 코드에서 attacked 메서드도 오버라이딩을 하여 전사와 마법사가 공격을 받을 때 life 속성값이 다르게 감소하도록 한다.

# In[39]:

class Character(object):

    def __init__(self):
        self.life = 1000
        self.strength = 10
        self.intelligence = 10

    def attacked(self):
        self.life -= 10
        print("공격받음 생명력 =", self.life)

    def attack(self):
        print("공격!")

class Warrior(Character):

    def __init__(self):
        super(Warrior, self).__init__()
        self.strength = 15
        self.intelligence = 5

    def attacked(self):
        self.life -= 5
        print("공격받음 생명력 =", self.life)

    def attack(self):
        print("육탄 공격!")


class Wizard(Character):
    def __init__(self):
        super(Wizard, self).__init__()
        self.strength = 5
        self.intelligence = 15

    def attacked(self):
        self.life -= 10
        print("공격받음 생명력 =", self.life)

    def attack(self):
        print("마법 공격!")


a = Character()
b = Warrior()
c = Wizard()

a.attacked()
b.attacked()
c.attacked()


# 연습문제 4
# 
# 다음과 같이 자동차를 나타내는 Car 클래스를 구현한다.
# 
# 이 클래스는 최고 속도를 의미하는 max_speed라는 속성과 현재 속도를 나타내는 speed라는 속성을 가진다.
# 객체 생성시 max_speed 속성은 160이 되고 speed 속성은 0이 된다.
# speed_up, speed_down이라는 메서드를 가진다. speed_up을 호출하면 speed 속성이 20씩 증가하고 speed_down을 호출하면 speed 속성이 20씩 감소한다.
# 스피드 속성 speed의 값은 max_speed 속성 값, 즉 160을 넘을 수 없다. 또 0 미만으로 감소할 수도 없다.

# In[40]:

class Car(object):

    def __init__(self):
        self.max_speed = 160
        self.speed = 0

    def speed_up(self):
        if self.speed < self.max_speed:
            self.speed += 20
        else :
            self.speed = self.max_speed
        print("speed : ", self.speed)

    def speed_down(self):
        if self.speed > 0 :
            self.speed -= 20
        else :
            self.speed = 0
        print("speed : ", self.speed)


# In[45]:

a = Car()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()


# In[46]:

a.speed_down()
a.speed_down()
a.speed_down()
a.speed_down()
a.speed_down()
a.speed_down()
a.speed_down()
a.speed_down()
a.speed_down()


# 연습문제 5
# 
# Car 클래스를 기반으로 SportCar와 Truck이라는 두 개의 자식 클래스를 구현한다.
# 
# SportCar 클래스는 max_speed 속성이 200 이고 speed_up, speed_down 호출시 속도가 40씩 증가 혹은 감소한다.
# Truck 클래스는 max_speed 속성이 100 이고 speed_up, speed_down 호출시 속도가 10씩 증가 혹은 감소한다.
# 스피드 속성 speed의 값은 max_speed 속성 값, 즉 160을 넘을 수 없다. 또 0 미만으로 감소할 수도 없다.

# In[47]:

class SportCar(Car):

    def __init__(self):
        super(SportCar, self).__init__()
        self.max_speed = 200
        self.speed = 0

    def speed_up(self):
        if self.speed < self.max_speed:
            self.speed += 40
        else :
            self.speed = self.max_speed
        print("speed : ", self.speed)

    def speed_down(self):
        if self.speed > 0 :
            self.speed -= 40
        else :
            self.speed = 0
        print("speed : ", self.speed)


class Truck(Car):
    def __init__(self):
        super(Truck, self).__init__()
        self.max_speed = 100
        self.speed = 0

    def speed_up(self):
        if self.speed < self.max_speed:
            self.speed += 10
        else:
            self.speed = self.max_speed
        print("speed : ", self.speed)

    def speed_down(self):
        if self.speed > 0:
            self.speed -= 10
        else:
            self.speed = 0
        print("speed : ", self.speed)


# In[48]:

a = SportCar()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()


# In[50]:

b = Truck()
b.speed_up()
b.speed_up()
b.speed_up()
b.speed_up()
b.speed_up()
b.speed_up()
b.speed_up()
b.speed_up()
b.speed_up()
b.speed_up()
b.speed_up()

