import random # importing "random" for random operations

def RandomNumberGenerator_3000to40000():        #defining a function RandomNumberGenerator_3000to40000() for the task
x=random.randrange(3000, 40001)                 #using randrange() to generate in range from 3000 to 40000, default index starting at 0
return x #returning the value

#x=RandomNumberGenerator_3000to40000()                             #calling the function and saving it in variable "x"
#print("A random number from range 3000 to 40,000 is :", x)        #printing the number stored in "x"
