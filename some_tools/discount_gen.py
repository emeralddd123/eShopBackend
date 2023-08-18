import random
import os

current_directory = os.getcwd()
# Generate 10 random numbers
random_numbers = [random.randint(1, 67) for i in range(10)]

# Save output to a text file
file_path = os.path.join(current_directory, 'output.txt')

with open(file_path, 'w') as file:
    for number,i  in random_numbers:
        file.write(str(number) + '\n')

print("Random numbers generated and saved to 'output.txt' file.")



