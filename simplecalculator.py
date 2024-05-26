
print("select operation -\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")

select = int(input( "Select operations form 1, 2, 3, 4 :" ) )
num_1 = float(input( "Enter first number: "))
num_2  = float(input( "Enter second number: "))

if select == 1:
   print("the addition of given two number is",num_1 + num_2)

elif select == 2:
   print("the subtraction of given two number is",num_1 - num_2)

elif select == 3:
   print("the multiplication of given two number is",num_1 * num_2)

elif select == 4:
   print("the division of given two number is",num_1 / num_2)

else:
   print("this is an invalid input")

   
