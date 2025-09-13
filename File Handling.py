# file1 = open('example.txt', 'r'), # Opens the file in read mode
#
# # This is used to open a file in read mode in python.
# with open('example.txt', 'r') as file:
#     data = file.read()
#     print(data)

# Using "with" automaticaly handles "CLOSING" of files
with open('output.txt', 'w+') as file:
    file.write("Hello, Python!")
    file.seek(0) # This is used to move the cursor back to beginning
    data = file.read()
    print(data)

# We use "try and except" error handling when dealing with files
try:
    with open('output.txt', 'w+') as file:
        file.write("School: {Name: Gaji, School: Lasu}")
        file.seek(0)
        data = file.read()
        print(data)

except FileNotFoundError:
        print("File not found. Please check the file name")
finally:
    file.close() # This is unnecessary as "with" closes files automatically


# Code challenge:

# Opening and writing into a new file
try:
    with open('input.txt', 'w') as inputFile:
        inputFile.write("Hello World \n I'm Gaji Yaqub \n It is so nice to learn 'file handling' in python\n Hopefully, we get to do wonderful things together\n Let's go get it")

    with open('input.txt', 'r') as readInput: # "readInput" is not an actual variable, instead it acts as an instance of the file
        data = readInput.read() # "data" IS a variable that we can now perform all types of data manipulation on
        print(data)
        dataLength = len(data) # Getting the data length
        print(dataLength)
        upperData = data.upper()
        print(upperData) # changing content to all caps
except FileNotFoundError:
    print("Kindly confirm file name. Not found!")

try:
    with open('output2.txt', 'a+') as outputFile: # I'm using "a" append here to add to the file not OVERWRITE
        stringValue = str(dataLength)
        outputFile.write(stringValue)
        outputData = outputFile.read()
        print(outputData)
except FileNotFoundError:
    print("This data can't be saved here. Check again")






