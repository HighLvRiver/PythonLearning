
# coding: utf-8

# # Python Basics

# ## Whitespace Is Important

# In[1]:

listOfNumbers = [1, 2, 3, 4, 5, 6]

for number in listOfNumbers:
    print number,
    if (number % 2 == 0):
        print "is even"
    else:
        print "is odd"
        
print "All done."
        


# ## Importing Modules

# In[2]:

import numpy as np

A = np.random.normal(25.0, 5.0, 10)
print A


# ## Lists

# In[3]:

x = [1, 2, 3, 4, 5, 6]
print len(x)


# In[4]:

x[:3]


# In[5]:

x[3:]


# In[6]:

x[-2:]


# In[7]:

x.extend([7,8])
x


# In[8]:

x.append(9)
x


# In[9]:

y = [10, 11, 12]
listOfLists = [x, y]
listOfLists


# In[10]:

y[1]


# In[11]:

z = [3, 2, 1]
z.sort()
z


# In[12]:

z.sort(reverse=True)
z


# ## Tuples

# In[13]:

#Tuples are just immutable lists. Use () instead of []
x = (1, 2, 3)
len(x)


# In[14]:

y = (4, 5, 6)
y[2]


# In[15]:

listOfTuples = [x, y]
listOfTuples


# In[16]:

(age, income) = "32,120000".split(',')
print age
print income


# ## Dictionaries

# In[17]:

# Like a map or hash table in other languages
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print captains["Voyager"]


# In[18]:

print captains.get("Enterprise")


# In[19]:

print captains.get("NX-01")


# In[20]:

for ship in captains:
    print ship + ": " + captains[ship]


# ## Functions

# In[21]:

def SquareIt(x):
    return x * x

print SquareIt(2)


# In[22]:

#You can pass functions around as parameters
def DoSomething(f, x):
    return f(x)

print DoSomething(SquareIt, 3)


# In[23]:

#Lambda functions let you inline simple functions
print DoSomething(lambda x: x * x * x, 3)


# ## Boolean Expressions

# In[24]:

print 1 == 3


# In[25]:

print (True or False)


# In[26]:

print 1 is 3


# In[27]:

if 1 is 3:
    print "How did that happen?"
elif 1 > 3:
    print "Yikes"
else:
    print "All is well with the world"


# ## Looping

# In[28]:

for x in range(10):
    print x,


# In[29]:

for x in range(10):
    if (x is 1):
        continue
    if (x > 5):
        break
    print x,


# In[30]:

x = 0
while (x < 10):
    print x,
    x += 1





