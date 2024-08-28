a = 35
t = type(a)
print(t)

a = 35.55
t = type(a)
print(t)

a = "arpil"
t = type(a)
print(t)

#type casting
a = 35
f = float(a) #convert  int to float of a
print(f)

#another one
a='arpil' 
# b = float(a) # It's should give an error because you can not convert words into Number like float and integer

#print(type(b))

#but you can convert number from a string into integer or number
c = "31"
d = float(c)
t = type(d)
s = str(d)
print(s)
print(type(s))
print(d)
print(t)