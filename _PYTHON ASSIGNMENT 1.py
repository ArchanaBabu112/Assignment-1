#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Example 1 (list)


# In[4]:


mylist1=[1,2.5,'abc','exam']


# In[5]:


mylist1.append(10)


# In[6]:


mylist1


# In[7]:


mylist1.insert(1,15.3)


# In[8]:


mylist1


# In[13]:


mylist1.pop()
mylist1


# In[14]:


mylist1.remove(2.5)
mylist1


# In[15]:


b=[True,5,17.25,'Archana']
mylist1.extend(b)
mylist1


# In[ ]:


#Example 2


# In[24]:


mylist2=['car','jeep',5,10.7,False]


# In[25]:


mylist2.remove('car')
mylist2


# In[26]:


mylist2.pop()
mylist2


# In[27]:


mylist2.append(True)
mylist2


# In[28]:


mylist2.insert(1,7)
mylist2


# In[ ]:


#example 1 (tuple)


# In[29]:


a=(1,True,'school',12.3)
len(a)


# In[ ]:


#example 2


# In[31]:


b=(5,False,'climate',20.07)


# In[32]:


#tuple is immutable

b.pop()


# In[33]:


len(b)


# In[ ]:


#example 1 (dictionary)


# In[35]:


dic1={'name':'Archana','Class':5,'Roll no':22}


# In[40]:


dic1['name']='Aiswariya'
dic1


# In[41]:


dic1['Subject']=['Mathematics']
dic1


# In[44]:


del dic1['Subject']
dic1


# In[46]:


del dic1


# In[47]:


dic1


# In[ ]:



#example 2


# In[52]:


dict2={'Name':'Archana','Department ':'Civil','Year':3}


# In[54]:


dict2['Name']=['Megha']
dict2


# In[56]:


del dict2['Year']


# In[57]:


dict2


# In[58]:


dict2['Score']='75'
dict2


# In[61]:


new=dict2['Score']
del dict2['Score']
dict2['marks']=new


# In[62]:


dict2


# #example 1(set)
# 

# In[63]:


set1={17,2,3.5,True,'abc'}
set1


# In[65]:


set2={100,78,2,95.3,False,'xyz'}
set1.union(set2)


# In[66]:


set1.intersection(set2)


# In[67]:


set1&set2


# In[ ]:




