# Assigning int value to Variable x and then multiplying with 5
x = 5
print(x * 5)
##OP - 25

# Assigning string value to Variable yt and then multiplying with 5
yt = 'Youtube'
print(yt * 5)
##OP - YoutubeYoutubeYoutubeYoutubeYoutube

# if we create string Variable and then add brackets [] and pass the int value that int use as index of the string
# The initial index of string is 0
print(yt[0])  # Y
print(yt[1])  # o
print(yt[2])  # u
print(yt[3])  # t
print(yt[4])  # u
print(yt[5])  # b
print(yt[6])  # e
print(yt[7])  #IndexError: string index out of range        #Becoz string index last value is 6

# if we pass -1 then it gives the value from the last
print(yt[-1])  # e
print(yt[-2])  # b
print(yt[-3])  # u
print(yt[-4])  # t
print(yt[-5])  # u
print(yt[-6])  # o
print(yt[-7])  # y
print(yt[-8])  #IndexError: string index out of range        #Becoz string index last value is -7

# [inclusiveIndex : ExclusiveIndex]
print(yt[0:5])  # Youtu
print(yt[:5])  # Youtu
print(yt[3:])  # tube
print(yt[1:100])  # outube

# String in Pythin is immutable We can not change after assignment;
yt[0:3] = '555'  # TypeError: 'str' object does not support item assignment
yt[0] = 'R'  # TypeError: 'str' object does not support item assignment

# Find the Length of the string the length white space
myName = 'Deepak Gupta'
length = len(myName)
print(length)
## OP = 12