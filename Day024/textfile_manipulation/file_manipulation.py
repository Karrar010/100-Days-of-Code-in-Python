# open()
# this is func used to deal with text/word files to read,write,apend etc and perform other actions on them

#for understanding relative and absolute file path watch vid 5 
File = open("./Day24/textfile_manipulation/textfile.txt") # this opens the file in the background
contents_of_file = File.read() 
print(contents_of_file) 
File.close() #when we open a file we need to close it at some time python automatically closes it later but dunno when

with open("./Day24/textfile_manipulation/textfile.txt") as file: #this func doesnot require file.close() as it is only run once
    contents_of_file = file.read()
    print(contents_of_file)  

# with open("./Day24/textfile_manipulation/textfile.txt" , mode="w") as file: # mode w speifies that we are writing the text file this remove all content of that file and 
#     file.write("5th line say goodbye")          # adds only this new line of text

with open("nofile.txt" , mode="w") as file:#if only in mode w (write) a file name doesnot exist then python creates the file directly and writes string in it
    file.write("5th line say goodbye")      

with open("./Day24/textfile_manipulation/textfile.txt" , mode="a") as file: # mode a appends the string into the next line after previous last line of text file
    file.write("\n5th line say goodbye") 
