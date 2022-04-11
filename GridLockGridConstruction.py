import random  # use random prime function need to import random package.
import math
from GridLockEncryptionBoard import *
import array
import base64

def random_num_prime(m):
  if m > 1:
    for i in range(2, m):
        if (m % i) == 0:
            return f"{m} is not prime"
            break
    else:
      return m

def random_num(x,y):
  num = random.randint(3,32)
  while random_num_prime(num) != num:
    num = random_num(3,32)
  return num


def Grid_Gen_Key():
    random_key = "["  # declare  empty list to store generated random numberrs.
    for i in range(4):  # call prime function random() 4 times
       random_key += (str(i + 1) + ",")
       random_key += str(random_num(3,34))

     # store generated random number as string.
       if i < 3:
          random_key += ":" #if this is not the last number, add : for next pair
    random_key += "]"
    return str(random_key)

print("Random Key is : ")
Rand_key = Grid_Gen_Key()  # call to the function
print(Rand_key)
 # display list of random number.

def Grid_Size_Estimate(input): #put a string in, get the square root of the length out
    length = len(input)
    size1 = (math.sqrt(length)) #this is just a fancy way of finding the square root and rounding up
    size = math.ceil(size1)
    return size

print(Grid_Size_Estimate("12345678912345678"))

def Grid_Construct(inlist): #this function is now proven to work!   DO NOT PUT BYTES IN THE GRID CONSTRUCTOR, STRINGS ONLY FOR NOW
    max_size = Grid_Size_Estimate(inlist)
    itemlist = inlist
    print(itemlist)
    grid_rows = []
    for i in itemlist: #for each item in the list
        added = False
        for r in grid_rows:
            if ( len(r) < max_size ) and added == False:
                r.append(i)
                added = True
        if added == False:
            grid_rows.append([i]) #add character as new array if it still hasn't been added
            added = True
    for i in grid_rows:     #fill in all the empty spaces and rows with *'s as necessary
        if len(grid_rows) < max_size:
            grid_rows.append(['*'])
        while len(i) < max_size:
                i.append('*')

    for i in grid_rows:
        print(i)
    final_grid = grid_rows
    return final_grid
#end of function_________________

#encryption

test_grid = (Grid_Construct("Test String, LOL!!!!!!"))
print('\n')
def shiftright(starting_grid):  #this will shift any values in a grid(comprised of rows) one value right
    new_grid = starting_grid
    for r in starting_grid:
        temp = r[len(r)-1] #grab the last value on the row
        r.insert(0,temp)
        r.pop(len(r)-1)    #slap it on the back

    #for r in new_grid:
    #    print(r)
    #print("shifted right")
    return new_grid

print('\n')
print(shiftright(test_grid))

def shiftdown(starting_grid):  #this will shift any values in a grid(comprised of rows) one value down
    new_grid = starting_grid
    temp = new_grid[len(new_grid) - 1]  # grab the last value on the row
    new_grid.insert(0, temp)
    new_grid.pop(len(new_grid) - 1)  # slap it on the back

    # for r in new_grid:   this has been commented out for efficiency reasons
    # print(r)
    #print("shifted down")
    return new_grid

print('\n')
print(shiftdown(test_grid))


#now for some Mirror functions for the DECRYPT cycle
def shiftleft(starting_grid):  #this will shift any values in a grid(comprised of rows) one value left
    new_grid = starting_grid
    for r in starting_grid:
        temp = r[0] #grab the last value on the row
        r.insert(len(r),temp)
        r.pop(0)    #slap it on the back

   #for r in new_grid:   this has been commented out for efficiency reasons
       # print(r)
    #print("shifted left")
    return new_grid

print('\n')
print(shiftleft(test_grid))

def shiftup(starting_grid):  #this will shift any values in a grid(comprised of rows) one value up
    new_grid = starting_grid
    temp = new_grid[0]  # grab the last value on the row
    new_grid.insert(len(new_grid), temp)
    new_grid.pop(0)
      # slap it on the back

    # for r in new_grid:   this has been commented out for efficiency reasons
    #   print(r)
    #print("shifted up")
    return new_grid

print('\n')
print(shiftup(test_grid))

def grid_to_string(grid_goes_here):
    grid = grid_goes_here
    exitstring = ""
    for r in grid:
        for i in r:
            exitstring += i
    return exitstring

print("final string is, ", grid_to_string(test_grid))


def interpret_random_key(key_goes_here):  #DO NOT CHANGE THISS
    current_key = key_goes_here
    addfact = 1
    mulfact = 1
    shiftrowfact = 1  #factors of how intense each action is
    shiftcolfact = 1
    chunk = 1
    tempstr = ""
    stripped_key = current_key[1:]
    for i in range (len(stripped_key)):
        x = current_key[i]
        #while inside the first colon zone
        if x != '[' and x != ':' and current_key[i+1] != ',' and x != ',' and  x != ']': #if x is not bracket, not equal to colon, and the next spaace is not colon'
            tempstr += x
        if x == ':' or x == ']' or current_key[i+1] == ']':    #sort which chunk this is every colon
            if chunk == 1:
                addfact = int(tempstr)
            if chunk == 2:
                mulfact = int(tempstr)
            if chunk == 3:
                shiftrowfact = int(tempstr)
            if chunk == 4:
                shiftcolfact = int(tempstr)
            tempstr = ""
            chunk += 1
    print("add,", addfact, "mul,", mulfact, "shiftrow,", shiftrowfact, "shiftcol,", shiftcolfact)
    return [addfact,mulfact,shiftrowfact,shiftcolfact]
#print (interpret_random_key("[1,13:2,47:3,5:4,3]"))
print('\n')

def findasciitotal(instring):
    totalascii = 0
    for x in instring:
        totalascii = int(ord(x))
    return totalascii
def gridlock_encrypt(AppName, UsePassString):
    App_Name = AppName
    User_inf = UsePassString  # define necessary info
    random_key = Grid_Gen_Key()
    instruction_stack = interpret_random_key(random_key)  # generate random key
    file = open("UniqueKeyStorage.txt", "r")  # recover unique user key
    unique_user_key = file.readline()
    file.close()
    print(instruction_stack)
    # put the string on a grid
    clean_grid = Grid_Construct(strtoNormalarray(User_inf)) # turn the normal array into a list of characters
    basic_offset = findasciitotal(unique_user_key)
    advanced_offset = int(findasciitotal(unique_user_key) * 17)   #finding the ascii value and distorting it to make our offset
    print(clean_grid)
    # turn's values of grid into bytes
    for r in clean_grid:  #for each row

       for i in range(len(r)): #for every element in each row
            r[i] = charTo_byte(r[i]) #turn them all to bytes

    print('\n')
    # add the total ascii value of the unique key to each of the bytes in the grid
    for r in clean_grid:
        for e in r:
            e = addTo_byte(e,advanced_offset)
    # in a loop of 10 times, do each of the 4 processes necessary
    for i in range(14): #start of encrpytion loop !!!!
        for r in clean_grid:
            print(r)
            for i in range(len(r)):
                r[i] = addTo_byte(r[i],int(instruction_stack[0] + int(0.1*len(User_inf))/int(3.2*instruction_stack[0]))) #add the appropriate value
        print("new bytes before moving", clean_grid)
        mult_total = 0 #moving to multiplication process
        for r in clean_grid:
            for i in range(len(r)):
                mult_total += instruction_stack[1]
        ("multiplying\n")
        for i in range(len(r)):
            r[i] = mul_byte(r[i], int(mult_total/(16 + int(3.1*instruction_stack[1]) + int(0.9*len(User_inf)-6))))  # change the mult total the appropriate value
        for i in range(instruction_stack[2]):
            clean_grid = shiftdown(clean_grid) #shift down
        print("shifted down")
        for i in range(instruction_stack[3]):
            clean_grid = shiftright(clean_grid) #shift right
        print("shifted right")
    # turn every byte back int utf-32 characters
    used_grid = clean_grid
    print("final bytes: ", used_grid)
    #for r in used_grid:  # for each row
        #for i in range(len(r)):  # for every element in each row
           #r[i] = byteTo_char(r[i])  # turn all bytes to char
    print("final result: \n", used_grid)
    # save result in utf-32
    finished_password = ""
    for r in clean_grid:
        row_password = ""
        for e in r:
            row_password += (e.decode('utf-32'))
        finished_password += row_password


    print(finished_password)
    file = open("passdump.txt", "w", encoding='utf-32')
    file.write(str("<" + AppName + ">"))
    file.write('\n')
    for r in used_grid:
        file.write(str(r))
        file.write('\n')
    file.write('\n')
    file.write(finished_password)
    file.write('\n')
    file.write(random_key)
    file.close()
    return(finished_password)

    # put key underneath for later
gridlock_encrypt("app_name_test","username;;password;")

#-----decryption process below


def gl_scan_encrypted_file(AppName,file_name):
    file = open(file_name, "r", encoding='utf-32')
    intake = file.readline()

    flag = 0
    if intake[1:-2] == AppName:
        print("file approved!")
        flag = 1
    scanned_grid = []
    if flag == 1:
        # the scanned grid is an attempt to read the file's byte rows
        print("the grid from this file looks like: ")
        while (intake != "" and intake != " " and intake != EOFError and intake != None):
            intake = file.readline()
            if str(intake):
                if str(intake)[0:2] == '[b':
                    scanned_grid.append(intake)
        file.close()
        for i in range(len(scanned_grid)):
            if scanned_grid[i] == "" or scanned_grid[i] == " " or scanned_grid[i] == None:
                scanned_grid.remove(scanned_grid[i])
        for r in scanned_grid:
            print(r)
        return scanned_grid

def gridlock_decrypt(AppName,file_name):
    encrypted_grid = gl_scan_encrypted_file(AppName,file_name) #scan with passed parameters

    #do the startup in reverse
    
    #all information scanned, moving on
    #start decryption
gridlock_decrypt("app_name_test","passdump.txt")
