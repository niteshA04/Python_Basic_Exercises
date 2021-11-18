#!/usr/bin/env python
# coding: utf-8

# # Exercise 1: Calculate the multiplication and sum of two numbers

# In[1]:


num1 = 29
num2 = 34
addition = num1+num2
print("The addition of the 2 no's is:", addition)

multi = num1*num2
print("The Multiplication of the 2 no's is:", multi)


# # Exercise 2: Print the sum of the current number and the previous number

# In[4]:


previous_num = 0
for i in range(1,11):
    print("Current No.", i, "Previous No.", previous_num, "Adition of two no.", previous_num + i)
    previous_num = i


# # Exercise 3: Print characters from a string that are present at an even index number

# In[2]:


inp_string = input("Enter any string: ")
str_length = len(inp_string)
x = list(inp_string)
for i in x[1::2]:
    print(i)


# # Exercise 4: Remove first n characters from a string

# In[10]:


inp_str = input("Enter the string: ")
len_str = len(inp_str)
num = int(input("Enter the number of letters to remove: "))

lst_str = list(inp_str)

if len_str < num:
    print("Number of char to remove should be less than string")
else:
    rem = lst_str[num:]
    lstTostr = ' '.join(map(str, rem))
    print(lstTostr)


# # Exercise 5: Check if the first and last number of a list is the same

# In[16]:


def fst_lst_same(n1):
    num_list = n1
    if num_list[0] == num_list[-1]:
        print("First and Last are Same")
    else:
        print("Not Same")
        
fst_lst_same([10,20,30,40,50,10])

fst_lst_same([10,20,30,40,50,1])


# # Exercise 6: Display numbers divisible by 5 from a list

# In[21]:


list_ = [10, 20, 33, 46, 55]

for i in list_:
    if i%5==0:
        print(i)


# # Exercise 7: Return the count of a given substring from a string

# In[25]:


str_x = "Emma is good developer. Emma is a writer"
s = str_x.count("Emma")
print(s)


# # Exercise 8: Print the following pattern

# ![image.png](attachment:image.png)

# In[26]:


for i in range(6):
    for j in range(i):
        print(i, end=' ')
    print('\n')


# # Exercise 9: Check Palindrome Number

# In[3]:


inp_num = input("Enter the number: ")
reverse = inp_num[::-1]

if inp_num == reverse:
    print("The given number is Palindrome")
else:
    print("The given number is not palindrome")


# # Exercise 10: Create a new list from a two list using the following condition
# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# In[7]:


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

new_list = []

for i in list1:
    if i%2 != 0:
        new_list.append(i)
    
for i in list2:
    if i%2 == 0:
        new_list.append(i)
        
print(new_list)


# # Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# In[8]:


num = input("Enter the number: ")
reverse = num[::-1]
print(reverse)


# # Exercise 12: Print multiplication table form 1 to 10

# In[12]:


for i in range(11):
    for j in range(10):
        multi = i*j
        print(multi, end=' ')
    print('\n')


# # Exercise 13: Print downward Half-Pyramid Pattern with Star     

# ![image.png](attachment:image.png)

# In[16]:


for i in range(5,0,-1):
    print('* '*i)
    


# # Exercise 14: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# In[17]:


def exponent(base, exp):
    b = base
    e = exp
    result = b**e
    return result

exponent(2, 2)


# # Exercise 12: Calculate income tax for the given income by adhering to the below rules
# 

# ![image.png](attachment:image.png)
# 
# input_income = 45,000

# In[18]:


income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

