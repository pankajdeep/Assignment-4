#Q.1- Reverse the whole list using list methods.
li=[]
size=int(input("Enter size of list"))
for i in range(size):
    inp=int(input("Enter element"))
    li.append(inp)
print("The actual list is :",li)
print("The reversed list is :",list(reversed(li)))


#Q.2- Print all the uppercase letters from a string.
string=input("Enter a string")
for i in string:
    if(i>='A' and i<='Z'):
        print(i)


#Q.3- Split the user input on comma's and store the values in a list as integers.
string=input("Enter some numbers seperated by commas")
l1=[]
l1=string.split(',')
size=len(l1)
for i in range(size):
    l1[i]=int(l1[i])
print(l1)


#Q.4- Check whether a string is palindromic or not.
inp=input("Enter a number whose palindrome you want to find")
tup=tuple(inp)
tup=list(tup)
tup=list(reversed(tup))
tup=''.join(tup)
if(inp==tup):
    print("Palindrome")
else:
    print("Not a Palindrome")


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
import copy as c
li=[2,4,[6,8],12]
li2=c.deepcopy(li)
li[2][0]='Hi'
print(li)
print(li2)

'''Difference between Shallow copy and Deep copy is that in shallow copy if the original object contain any references to mutable object then the duplicate
reference variable will be created pointing to the old object and no duplicate object is created whereas in deep copy a duplicate object is created.'''
