
# coding: utf-8

# In[1]:

t = lambda x:x*2+1


# In[2]:

t(6)


# In[3]:

t = lambda x: print("test")


# In[4]:

t = lambda x: print("test: {}".format(x+3))


# In[5]:

seq = [1,2,3,4,5]


# In[6]:

map(lambda num: num*3,seq)


# In[7]:

list(map(lambda num: num*3,seq))


# In[8]:

filter(lambda num: num%2 == 0, seq)


# In[9]:

list(filter(lambda num: num%2 == 0, seq))


# In[10]:

s = 'hello my name is Jayden'


# In[11]:

s.lower()


# In[12]:

s.upper()


# In[13]:

s.split()


# In[14]:

tweet = 'Go Sports! #Sports'


# In[15]:

tweet.split()


# In[16]:

tweet.split('#')


# In[17]:

tweet.split('#')[1]


# In[18]:

d = {'k1':1, 'k2':2}


# In[19]:

d


# In[20]:

d.keys()


# In[21]:

d.items()


# In[22]:

d.values()


# In[23]:

lst = [1,2,3]


# In[24]:

lst.pop()


# In[25]:

lst


# In[26]:

lst = [1,2,3,4,5]


# In[27]:

item = lst.pop()


# In[28]:

lst


# In[29]:

item


# In[30]:

first = lst.pop(0)


# In[31]:

lst


# In[32]:

first


# In[33]:

lst.append('new')


# In[34]:

lst


# In[35]:

'x' in [1,2,3]


# In[36]:

'x' in ['x','y','z']


# In[37]:

x = [(1,2),(3,4),(5,6)]


# In[38]:

x


# In[39]:

x[0]


# In[40]:

x[0][0]


# In[41]:

x[0][1]


# In[42]:

for item in x:
    print(item)


# In[43]:

for (a,b) in x:
    print(a)


# In[45]:

for a,b in x:
    print(a)
    print(b)


# In[ ]:



