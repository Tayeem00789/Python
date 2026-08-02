a = 5
b = 2.5
name = "Tayeem"
student = True
print(type(a))
print(type(b))
print(type(name))
print(type(student))

#Typecasting

b = int(b)
print(type(b))
student = str(name)
print(type(student))




word1 = "mango"
word2 = "juice"

#Starting Index

print(word1[2])
print(word2[0])
print(word1[-1]) #Last Index always -1

#Slicing

print(word1[0:3]) #slicing=> {start index : end index +1 }

#Concatanate
word3 = word1 + " " + word2
print(word3)