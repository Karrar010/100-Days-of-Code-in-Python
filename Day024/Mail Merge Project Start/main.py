#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as names: #reads the name file
    name = names.readlines() # allocates the list of invited_names to name 
    for x in range(len(name)): 
        recipient_name = name[x].strip() #strip the name of spaces before and after name in loop one by one 
        with open("./Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_doc:
            letter_content = letter_doc.read() #allocate the letter doc content to a variable
            new_letter = letter_content.replace("[name]",recipient_name) #replace a certain string from letter_content variable
            # if recipient_name == "Appa":
            #     print(new_letter)
            with open(f"./Day24/Mail Merge Project Start/Output/ReadyToSend/letter_to_{recipient_name}.txt",mode="w") as letter_to:
                letter_to.write(new_letter) #create a new letter for each invited_name
