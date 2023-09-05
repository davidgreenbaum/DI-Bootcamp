# CHALLENGE 1

mult_list = []
number_s = input("give me a number ")
length_s = input("now give me a legnth ")
number = int(number_s)
length = int(length_s)

for num in range(length):
    mult = num * number
    mult_list.append(mult)


print(f"number: {number}  - length - {length} {mult_list}")


# not exactly right, but pretty close!





# CHALLENGE 2

string = input("give me a weird strung out word with repeating letters")
for 