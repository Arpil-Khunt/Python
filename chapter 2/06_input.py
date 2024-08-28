#This input function take input from the user but it's type is always a string
#if you want to get integer then you need to convert type of the input

a = input("Enter number 1 :")
b = input("Enter number 2 :")
print('type of number 1 and 2 is:' ,type(a),type(b)) # type of a and b is str
print('The sum of number 1 and 2 is:',int(a)+int(b))#convert the type of a and b to integer