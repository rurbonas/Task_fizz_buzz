fb_list = ([], []) # Initialises a 2D list for holding the user inputs
user_names = str(input("Chose a silly name"
                       "\nType `continue` to see results: ")) # Asks the user the name that they'd like to use
user_number = int(input("In what increments shall this number appear? write a number>> ")) # Asks the user what number they'd like to assign to that name

while user_names.strip() != "continue": # Repeats the above until the user says "exit"
    fb_list[0].append(user_number)
    fb_list[1].append(user_names)
    user_names = str(input("Chose a another silly name"
                           "\nType `continue` to see results: ").lower())
    if user_names.strip() == "continue":
        break # Breaks the program if user says "continue"
    else:
        user_number = int(input("In what increments shall this number appear? write a number>> "))

fb_zip = zip(fb_list[0], fb_list[1]) # Converts the list into a format that a dictionary can read
fb_dict = dict(fb_zip) # Converts the zip into an immutable dictionary
# Since dictionaries are immutable, they can be looped through, this is why it is important to convert to one. Using the list as is will throw an index error

limit = int(input("What number shall be our upper limit? >> ")) # Asks the user where they'd like FizzBuzz to stop counting

for counter in range(limit): # counting from 0 to the limit
    output = "" # Preparing the output which we will modify based on whether or not the number will be Fizz or Buzz
    for number in fb_dict.keys(): # Scans through the dictionary for matching keys
        if counter % number == 0:
            output += fb_dict[number] # Adds the word to the current output
    if output == "": # If the output is still empty...
        output = counter # Add the current counter value to it...
    print(output) # Print the output for this loop