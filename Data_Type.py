###############################################
#Type Casting
###############################################
#int()
###############################################
#Float to Int
# print(int(123.45))

# #Complex to Int not possible
# #print(int(1+2j))

# #boolean to int
# print(int(True))
# print(int(False))

# #str to int
# #Note: str to int only possible when str value is integral value with base 10
# print(int('10')) #valid
#print(int('Ten')) #not valid
# print(int('0B1111')) #not Valid
###############################################

#float
###############################################
#int to float
# print(float(12))
# print(float(0b1111))
# print(float(0X1111))
# print(float(0o1111))

#complex to float not possible
#print(float(1+2j)) #not valid

#boolean to int
# print(float(True))
# print(float(False))

#Str to float
#Note str to float possible only for integral int and float value with base 10
# print(float('10'))
# print(float('12.5'))
# print(float('ten')) #not valid
# print(float('0b1111')) #not valid
# print(float('0O1111')) #not valid
# print(float('0x1111')) #not valid

#complex
###############################################
#int to complex

#form1
# print(complex(10))

# #float to complex
# print(complex(10.5))

# #boolean to complex
# print(complex(True))
# print(complex(False))

#str to complex
#not in complex form 1 value should be integral int or float with base 10
# print(complex('10'))
# print(complex('10.5'))
# print(complex('ten')) #not valid
# print(complex('0B1111'))
# print(complex('0O1111'))
# print(complex('0X1111'))


#form 2
# print(complex(10,2))

# #float to complex
# print(complex(10.5,10.5))

# #boolean to complex
# print(complex(True,False))
# print(complex(False,True))

#str to complex
#not possible
# print(complex(10,'20')) #not valid
# # print(complex('10.5','20.5')) #not valid
# # print(complex('ten')) #not valid
# # print(complex('0B1111')) #not valid
# # print(complex('0O1111')) #not valid
# # print(complex('0X1111')) #not valid
###############################################

#boolean
###############################################
#int to boolean
#note if value zero then False else True, applicable for int ,float complex 
#note for string it False when string is empty else true
# print(bool(10)) #True  
# print(bool(0)) #False

#Float to boolean
# print(bool(10.5)) #True  
# print(bool(-10.5)) #True 
# print(bool(0.5)) #True 
# print(bool(0.0)) #False

#complex to boolean
# print(bool(10.5+5j)) #True 
# print(bool(10.5-5j)) #True 
# print(bool(10.5+0j)) #True 
# print(bool(10+0j)) #True 
# print(bool(0+0j)) #True 

#String to boolean
# print(bool('10'))
# print(bool('10.5'))
# print(bool('Ten'))
# print(bool(''))


###############################################
#String
###############################################
# print(str(10))
# print(str(0B1111))
# print(str(10.5))
# print(str(True))
# print(str(1+3j))

###############################################
#Fundamental datatype are immutable
###############################################
#Fundamental datatype are as follows
# int
# float
# complex
# boolean
# string

#Note : All fundamental data types are immutable.
#Onces we create object we cannot perform any changes in that object, and if we try to make any changes in that object, with those changes new object will created.
# x=10
# y=10

# print(type(x))
# print(type(y))

# print(id(x)) #same address
# print(id(y)) #same address

# print(x is y) #if both reference variable pointing to same object
# #note :  'is' for Address specification

# y+=1 #after changes in y object , with new changes new object created.
# print(id(x)) 
# print(id(y))

###############################################

# x=10.5
# y=10.5

# print(type(x))
# print(type(y))

# print(id(x)) #same address
# print(id(y)) #same address

# print(x is y) #if both reference variable pointing to same object
# #note :  'is' for Address specification

# y+=1 #after changes in y object , with new changes new object created.
# print(id(x)) 
# print(id(y))

###############################################

# x=True
# y=True

# print(type(x))
# print(type(y))

# print(id(x)) #same address
# print(id(y)) #same address

# print(x is y) #if both reference variable pointing to same object
# #note :  'is' for Address specification

# y+=True #after changes in y object , with new changes new object created.
# print(type(x))
# print(type(y))

# print(id(x)) 
# print(id(y))

###############################################

# x='durga'
# y='durga'

# print(type(x))
# print(type(y))

# print(id(x)) #same address
# print(id(y)) #same address

# print(x is y) #if both reference variable pointing to same object
# #note :  'is' for Address specification

# y+='Software' #after changes in y object , with new changes new object created.
# print(type(x))
# print(type(y))

# print((x))
# print((y))

# print(id(x)) 
# print(id(y))
###############################################

# l1=[10,20,30,40,50]

# print(l1)
# print(type(l1))

# l2=l1

# print(l2)
# print(type(l2))

# print(id(l1))
# print(id(l2))

# l2[0]=11

# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))

# l1[1]=22

# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))
###############################################

# ###############################################
# #list
# ###############################################
# #order preserved
# #heterogenous objects are allows
# #growable in nature
# #duplicates allows
# #[]
# #mutable
# #indexing and slicing

# l=[10,'durga',20,30,True,40.5,1+2j]
# print(l)
# print(type(l))

# #indexing and slicing
# print(l[:5])
# print(l[3])
# print(l[-1])

# #insert data in list
# l.append(80)
# l.append(90)
# print(l)

# #pop
# print(l.pop())
# print(l)

# #remove specific element from list
# l.remove(20)
# print(l)

# ###############################################
# #tuple
# ###############################################
# #order preserved
# #heterogenous objects are allows
# #growable in nature
# #duplicates allows
# #()
# #immutable
# #indexing and slicing

# l=(10,'durga',20,30,True,40.5,1+2j)
# print(l)
# print(type(l))

# #indexing and slicing
# print(l[:5])
# print(l[3])
# print(l[-1])

# # l[1]='Durgasoftware'
# # print(l)

# ###############################################
#SET
# ###############################################
#order not preserved
#Indexing and slicing not allow
#heterogenous objects allows
#duplicates not allow
#{}
#mutable
#growable in nature

# s={}
# print(s) 
# print(type(s))  #always dict

# s1=set(s) #use set function
# print(type(s1))

# s = {10,20,'durga',True,1+2j,30.5}
# print(type(s))
# print(s)

# s.add(40)
# print(s)

# s.remove(10)
# print(s)

# ###############################################
#ForzenSET
# ###############################################
#order not preserved
#Indexing and slicing not allow
#heterogenous objects allows
#duplicates not allow
#{}
#immutable


# s={}
# print(s) 
# print(type(s))  #always dict

# s1=set(s) #use set function
# print(type(s1))

# s = {10,20,'durga',True,1+2j,30.5}
# print(type(s))
# print(s)

# fs=frozenset(s)

# print(type(fs))
# print(fs)

# fs.add(40) #error
# print(s)

# fs.remove(10) #error
# print(s)

# ###############################################
#Dictionary
# ###############################################

#Order not applicable
#Indexing and slicing not possible
#heterogenous objects allow
#mutable
#growable in nature
#duplicate of value allow but duplication of key not allow and still if we try then previous key value get replace

d={}
print(type(d))
print(d)

d['A']='Apple'
d['B']='Ball'
d[1]=100
d[2]=200

print(type(d))
print(d)

d[1]=1000

print(type(d))
print(d)

del d[1]
print(type(d))
print(d)











