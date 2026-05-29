hindi_dict = {
    "pankha": "Fan",
    "ghar": "House",
    "pustak": "Book",
    "paani": "Water",
    "kalam": "Pen"
}

print("Different types of words:")
user_world=input("Enter words:")

meaning = hindi_dict.get(user_word, "Sorry, this word is not available in the dictionary!")

print("English meaning is:", meaning)

