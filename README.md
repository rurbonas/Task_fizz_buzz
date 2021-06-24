# Fizz Buzz!

## Summary

Simple game that will substitute multiples of 3 and 5 for fizz and buzz respectively, or fizzbuzz for multiples of the two

## Tasks

Core:
* Write a program that prints the numbers from 1 to 100.
* For multiples of three print "Fizz" instead of the number
* For the multiples of five print "Buzz" instead of the number
* For numbers which are multiples of both three and five print "FizzBuzz".

Extra:
* make a new fizzbuzz file and make it functional
* make it, so we can decide which numbers to substitute for fizz and buzz using functions



Hint: loop, range, control flow

## Acceptance Criteria

* All core tasks are done
* Core works with no error

```python
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
```
example output:
```python
Chose a silly name
Type `continue` to see results: buzzy
In what increments shall this number appear? write a number>> 3
Chose a another silly name
Type `continue` to see results: gaga
In what increments shall this number appear? write a number>> 5
Chose a another silly name
Type `continue` to see results: zazu
In what increments shall this number appear? write a number>> 6
Chose a another silly name
Type `continue` to see results: continue
What number shall be our upper limit? >> 30
buzzygagazazu
1
2
buzzy
4
gaga
buzzyzazu
7
8
buzzy
gaga
11
buzzyzazu
13
14
buzzygaga
16
17
buzzyzazu
19
gaga
buzzy
22
23
buzzyzazu
gaga
26
buzzy
28
29
```