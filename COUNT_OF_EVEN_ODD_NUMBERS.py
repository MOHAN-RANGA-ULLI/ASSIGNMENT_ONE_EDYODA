tp = input('enter the numbers:')
series=tp.split(',')

odd_numbers =0
even_numbers =0
for i in series:
    if int(i)%2 == 0:
        even_numbers +=1
    else:
        odd_numbers +=1
print('number of even numbers:' , even_numbers)
print('number of odd numbers:' , odd_numbers)
# numbers = input("Enter a series of numbers separated by spaces: ")

# # Split the input string into a list of integers
# numbers_list =  numbers.split()

# # Initialize counters for even and odd numbers
# even_count = 0
# odd_count = 0

# # Iterate through the numbers and count even and odd numbers
# for number in numbers_list:
#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# # Print the counts
# print("Number of even numbers:", even_count)
# print("Number of odd numbers:", odd_count)