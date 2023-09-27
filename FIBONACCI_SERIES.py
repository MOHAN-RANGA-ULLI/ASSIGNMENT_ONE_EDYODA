number= int(input('enter the number:'))

first_value=0 # Initializing the first value
second_value=1 # Initializing the second value

print(first_value,end=' ') 
print(second_value,end=' ')

for i in range(2,number):
    third_value=first_value+second_value
    first_value= second_value
    second_value=third_value
    print(third_value,end=' ' )# Print the Fibonacci numbers
   
       

