test_unique_key = "Filler_Unique_key"
test_info = "Jacob1234567¶¶Mike12!^"


export = test_info.encode('utf-32') #this is a complete byte list
print("Literal bytes read as ", str(export))
print(export.decode('utf-32'))

print("\n")

#encryption process:
#We made this function to turn a string into an array of base 32 bytes
def strto32bitarray(instring):
    temparr= []
    x = 0
    for i, x in enumerate(instring):
        temparr.append(x.encode('utf-32')) #translate each character into 1 32bit value
    return temparr
flatarr = strto32bitarray(test_info) #make a single flat array of the encoded bytes
print(flatarr)

def strtoNormalarray(instring):
    temparr= []
    x = 0
    for i, x in enumerate(instring):
        temparr.append(x) #translate each character into 1 32bit value
    return temparr


#these are debug tests to make sure each typecast works v
test1 = int(int.from_bytes(flatarr[0], "little")) #testing integer translation to base 10 number
print("Test of Byte to integer (in decimal): ", test1)
#test2 = str((test1,32))        #testing base changing
#print("Test of Byte to integer (in base-32):", test2)
test3 = (flatarr[0].decode('utf-32'))     #testing decoding retreived values from arrays
print("the first should read: ",test3)
#fourth test should turn an integer (base 10) back into bytes
test4 = bytes(str(test3), 'utf-32')
print("The byte comes back as: ",test4)


print("Testing Byte Manipulation,\n")
testx = int(test1 * 2.0) #test changing the value of a byte to get the next symbol in table. Since we're using little endian
#we need small numbers instead of large ones

testz = testx.to_bytes(8, 'little') #turning added number back into bytes
print("The 1st byte should now be: ",(testz))
print("since we've multiplied by 3, the byte is 3x higher, and its symbol is now: ", testz.decode('utf-32'))
#Add the ascii value of the User Unique_Key to each byte as our offset (don't forget this)
print("All tests successful")

#-------- Beneath are Organized functions to make byte translation easier
#now we define our functions for easy cleanup, now that the tests are out of the way
#turn byte to integer
#!!!THESE FUNCTIONS CANNOT BE FOUND ONLINE, DO NOT ERASE, THEY ARE ONE OF A KIND

def byteTo_integer(input):
    #we need to take the entire byte value and subtract the prefix that means "string".
    raw_num = int(int.from_bytes(input, "little"))          #turning the whole index into one massive number
    utf32rep = raw_num - 133144051455                   #subtracting the "string" prefix, 133144051455
    return utf32rep         #return only the part of the number that represents the bytes value on the utf-32 table

#turn integer back to byte
def integerTo_byte(input): #now we need to put the offset back, so that the utf encoding knows this still represents a stringlike character
    raw_byte = input
    finished_byte = (raw_byte + 133144051455).to_bytes(8,"little")
    return finished_byte

#turn byte to character
def byteTo_char(input):
    raw_byte = input
    chara = raw_byte.decode('utf-32')
    return chara

#turn character back to byte
def charTo_byte(input):
    rawchar = input
    finished_byte = rawchar.encode('utf-32')
    return finished_byte

#add value to a byte character without adding to the entire byte
def addTo_byte(thebyte,add_value):  #turn a byte into a number, add to it, then put it back
    new_value = byteTo_integer(thebyte) + add_value
    new_byte = integerTo_byte(new_value)
    print("added,", add_value)
    return new_byte

#multiply value of byte
def mul_byte(thebyte,mulvalue):  #turn a byte into a number, add to it, then put it back
    new_value = byteTo_integer(thebyte) * mulvalue
    new_byte = integerTo_byte(new_value)
    print("multiplied,", mulvalue)
    return new_byte
#decrpytion mirrors-------
def subfrom_byte(thebyte,sub_value):  #turn a byte into a number, sub from it, then put it back
    new_value = byteTo_integer(thebyte) - sub_value
    new_byte = integerTo_byte(new_value)
    return new_byte

#div value of byte
def div_byte(thebyte,divvalue):  #turn a byte into a number, add to it, then put it back
    new_value = byteTo_integer(thebyte) / divvalue
    new_byte = integerTo_byte(new_value)
    return new_byte


#debug test for smallest offset
#print(byteTo_integer(flatarr[0]))
#print(integerTo_byte(byteTo_integer(flatarr[0])))

print("testing addition (adding 300)")
print(addTo_byte(flatarr[0],300))
print(byteTo_char(addTo_byte(flatarr[0],300)))

print("testing multiplication (multiplying by 800)")
print(mul_byte(flatarr[0],320))
print(byteTo_char(mul_byte(flatarr[0],700)))

#now we try putting each value on a grid, given a test size:


