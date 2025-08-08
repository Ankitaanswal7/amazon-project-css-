print("hello world")
print("my name is Ankita")
print("hello world ", "my favourite game is cricket.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
print(17)
print(2+4)
print(2*4)

name="Ankita"
age = 17
price = 24.99
old= False
a=None

print(name)
print(price)
print(age)
print(old) 
print(a)

print("my name is :" , name)
print("my age is :" , age)

age2 = age 
print(age2)

print(type(name))  #string-sentence -can be in single and double code  ''    ""   ''' '''
print(type(age))   #int
print(type(price))   # float
print(type(old))      #boolean  True False  T and F - captial letters 
print(type(a))    #none  random variable    a=none

#keywords-- and , as , assert , break , class , continue , def , del, elif , else , except, finally , False , for, from , global , if , import, in , is , lambda.
#keywords-- nonlocal, None , not , or , pass, raise, return, True, try, with , while , yield.
#keywords are reserved words


name1 ='AA'
name2="AA"
name3='''AA'''

print(name1)
print(name2)
print(name3)

#python - case sensitive
a=2
b=6
sum=a+b
print(sum)

c=9
d=3
diff=c-d 
print(diff)


"""" my
name is ankita """
# for multiline comment """"""

print("hello world")
print("hello world")
print("hello world")    # select and  ctrl + forward slash 

#arithmetic operators
a=5
b=2

sum = a + b
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print( a % b )  # for remainder
print( a ** b )  #  a^b

#Relational operators 
a= 50
b= 20

print( a ==b )  # False
print( a != b )  #True
print( a >= b)   # True
print( a > b)  # True 
print( a <= b )  # False
print ( a < b)  # True


# assignment operators
num = 10
num = num + 10   # 10+10= 20 
num += 10      #10+10= 20
print( "num :" , num )

num -= 10      #10-10  = 0
print( "num :" , num )

num *= 10      #10*10  = 100
print( "num :" , num )

num /= 5       #10/5= 2
print( "num :" , num )

num %= 5
print("num " , num)


# Logical opertaors 

a= 50
b = 30

print( not False)
print( not(  a  > b ))


# print ( not True )

val1 = True
val2 = True 
print( " and operator: " , val1 and val2 )

# ans True only if both the values are true

val1 = True
val2 = False
print( " and operator: " , val1 and val2 )

print(" or operator :" , val1 or val2 )

print(" or operator : ",  ( a==b) or ( a > b ))
