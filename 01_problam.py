"""unique_number=set()

print("Enter unique number")

for i in range(8):
    num=int(input(f"{i+1}:"))
    unique_number.add(num)

    print("\n your unique number")

    print(unique_number)"""

number_set = set()

num1 = int(input("Enter number 1: "))
number_set.add(num1)

num2 = int(input("Enter number 2: "))
number_set.add(num2)

num3 = int(input("Enter number 3: "))
number_set.add(num3)

num4 = int(input("Enter number 4: "))
number_set.add(num4)

num5 = int(input("Enter number 5: "))
number_set.add(num5)

num6 = int(input("Enter number 6: "))
number_set.add(num6)

num7 = int(input("Enter number 7: "))
number_set.add(num7)

num8 = int(input("Enter number 8: "))
number_set.add(num8)

# Poore set ko dekhne ke liye
print("Unique number:", number_set)

    