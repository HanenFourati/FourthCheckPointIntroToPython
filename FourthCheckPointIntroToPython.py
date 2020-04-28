#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a Python function to find the Max of three numbers.
def Max(n1,n2,n3):
    return max(n1,n2,n3)
Max(1,2,7)


# In[71]:


# Write a function that sums the elements of a list of integers.
def SumList(list) : 
    result = 0
    for x in list: 
         result = result + x  
    return result  
SumList([3, 2, 4])

# Write a function that multiplies the elements of an integer list.
def MultiplyList(list) : 
    result = 1
    for x in list: 
         result = result * x  
    return result  
MultiplyList([3, 2, 4])

# Use the two functions to sum the elements whose position is an even number (0,2,4…) and multiply the rest.
def QuestionTwo(list):
    L1=[]
    L2=[]
    i=0
    j=0
    for x in range(len(list)):
        if (x % 2) == 0:
            L1.insert(len(L1)+1, list[x])
        else:
            L2.insert(len(L2)+1, list[x])
    return "The inial list: ", list , "The elemnts with even positions sum: " , SumList(L1) , "The rest multplication: " , MultiplyList(L2)


QuestionTwo([3, 2, 4, 5])


# In[3]:


# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
words=[n for n in input().split('-')]
words.sort()
print('-'.join(words))

