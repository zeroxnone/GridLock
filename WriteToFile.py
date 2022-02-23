import os

# Required functions
def save_to_file(string):

    all_files_availabe = os.listdir("./")

    first_file = ""
    file = ""

    # Checking for all available files
    for file in all_files_availabe:

        # Checking if file exists or not
        if '.txt' in file:
            first_file = file
            break

    # If valid text file exists
    if first_file!="":
        print("First file in which we can write string is : ",first_file)
        file_data = ""

        # Reading previous data
        dataFile = open(file,'r')
        file_data = dataFile.read()
        dataFile.flush()
        dataFile.close()

        # Writing string to the first line
        dataFile = open(file,'w')
        dataFile.writelines([string," ",file_data])
        dataFile.close()
        print("String has been successfully added to the first file.\n")

    else:
        print("No writable file found!")

# Calling the function
save_to_file("Hello friends")
