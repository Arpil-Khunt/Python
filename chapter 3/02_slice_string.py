#Slicing the string means, cut some continuous portion of the string 

name = "arpil khunt";

# #length of the string
# print(name.__len__())
# #or another way to find string length using len function
# print('length of the string is : ',len(name))

#slice
fullname = name[0:11]
shortName = name[0:3] #for a split you have to mention, startIdx =>it's including and endingIdx =>it's excluding
s1name = name[2:10]
print(fullname)
print(s1name)
print(shortName)

#last index is excluded and starting index is included
#similary we can also slice a string reverse for that we count last index -1 and so on -2,-3,-4....
reversename = name[:-1]
reversename1 = name[-11:]
reversename2 = name[-2:-1]
print(reversename2)

#split
#print(name.split(" "))
