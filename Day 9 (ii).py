#Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’
# Open and read the file
with open("poems.txt", "r") as f:
    content = f.read()

# Check for the word
if "twinkle" in content.lower():
    print("Yes, the word 'twinkle' is present.")
else:
    print("No, the word 'twinkle' is not present.")
The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import os

# Dummy game function returning a score
def game():
    return 85  

current_score = game()

# Read the previous high score
if os.path.exists("Hi-score.txt"):
    with open("Hi-score.txt", "r") as f:
        hi_score_str = f.read()
    
    # If file is not empty, convert to int; else set to 0
    hi_score = int(hi_score_str) if hi_score_str.strip() != "" else 0
else:
    hi_score = 0

print(f"Current Score: {current_score}, Previous High Score: {hi_score}")

# Update high score if broken
if current_score > hi_score:
    print("Congratulations! New High Score!")
    with open("Hi-score.txt", "w") as f:
        f.write(str(current_score))
#Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
import os

# Create a folder for the tables if it doesn't exist
os.makedirs("tables", exist_ok=True)

# Loop from table 2 to 20
for i in range(2, 21):
    with open(f"tables/table_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")
            
print("Tables from 2 to 20 generated successfully in the 'tables' folder!")
A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
# Read the content first
with open("sample.txt", "r") as f:
    content = f.read()

# Replace the word
updated_content = content.replace("Donkey", "#####")

# Write it back to the same file
with open("sample.txt", "w") as f:
    f.write(updated_content)

print("Censored 'Donkey' from the file.")
Repeat program 4 for a list of such words to be censored.
words_to_censor = ["Donkey", "badword", "monkey", "stupid"]

with open("sample.txt", "r") as f:
    content = f.read()

# Loop through list and replace each word
for word in words_to_censor:
    content = content.replace(word, "#####")

with open("sample.txt", "w") as f:
    f.write(content)

print("All listed words have been censored.")
#Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt", "r") as f:
    log_data = f.read()

if "python" in log_data.lower():
    print("Yes, 'python' is present in the log file.")
else:
    print("No, 'python' is not present in the log file.")
#Write a program to find out the line number where python is present from ques 6
with open("log.txt", "r") as f:
    lines = f.readlines()

line_number = 1
found = False

for line in lines:
    if "python" in line.lower():
        print(f"Found 'python' on line number: {line_number}")
        found = True
    line_number += 1

if not found:
    print("'python' was not found in any line.")
#Write a program to make a copy of a text file “this.txt
# Read from original file
with open("this.txt", "r") as f_source:
    content = f_source.read()

# Write to destination file
with open("copy_of_this.txt", "w") as f_dest:
    f_dest.write(content)

print("File copied successfully.")
#Write a program to find out whether a file is identical & matches the content of another file.
with open("file1.txt", "r") as f1:
    content1 = f1.read()

with open("file2.txt", "r") as f2:
    content2 = f2.read()

# Compare content strings
if content1 == content2:
    print("The files are identical.")
else:
    print("The files are NOT identical.")
Write a program to wipe out the content of a file using python
# Just opening in 'w' mode empties the file automatically
with open("file_to_wipe.txt", "w") as f:
    pass  # 'pass' means do nothing inside the block

print("File content wiped out completely.")
#Write a python program to rename a file to “renamed_by_python.txt”.
import os

old_filename = "old_file_name.txt"
new_filename = "renamed_by_python.txt"

# Rename the file safely
if os.path.exists(old_filename):
    os.rename(old_filename, new_filename)
    print(f"File successfully renamed to {new_filename}")
else:
    print(f"The file '{old_filename}' does not exist.")


