him = input("Enter his name: ")
her = input("Enter her name: ")

alpha_count_1 = ["T", "R", "U", "E"]
alpha_count_2 = ["L", "O", "V", "E"]

tens = 0
ones = 0

# for letters in alpha_count_1:
#     if letters.lower() in him.lower():
#         tens += 1

# for letters in alpha_count_1:
#     if letters.lower() in him.lower():
#         tens += 1
for letters in him+her:
    if  letters.upper() in alpha_count_1:
        tens += 1

for letters in her+him:
    if letters.upper() in alpha_count_2:
        ones += 1

print(f"Congratulations {him} and {her} your love percentage is {tens}{ones}% !!!")
