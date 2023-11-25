"""
Files

1. Write code that asks the user for their name,
then opens a file called "name.txt" and writes that name to it. Remember to close your file.
"""
FILENAME = "name.txt"

name = input("input your name: ")
with open(FILENAME, "w") as out_file:
    print(name, file=out_file)
"""
2. (In the same file, but as if it were a separate program)
 Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file)
"""
FILENAME = "name.txt"

with open(FILENAME, "r") as in_file:
    text = in_file.read()
print(f"Your name is {text}")

"""
3. Create a text file called numbers.txt and save it in your prac directory.
 Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and 
adds them together then prints the result, which should be... 59.
"""
FILENAME = "numbers.txt"
total = 0
with open(FILENAME, "r") as in_file:
    for i in range(2):
        total += int(in_file.readline())
print(total)

"""
4.Now write a fourth block of code that prints the total for all lines in numbers.txt 
or a file with any number of numbers.
"""
FILENAME = "numbers.txt"
total = 0
with open(FILENAME, "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)
