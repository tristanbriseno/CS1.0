fahrenheit = float(input("Input tempurature in Fahrenheit here: "))
 celsius = (fahrenheit - 32) * 5/9
 if celsius < 20:
  print("Man it getting cold in here!!!")
 if celsius > 19:
     Print("Now that perfect!")
 if celsius > 40:
     print("Whew, its getting hat in here!")
 print("The temperature in celsius is: " , celsius)
#this was my first attempt at the calculator

 fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))
#this was my seconf attempt but I dont know how the blue "%.2f" and "%0.2f" work so I felt like it was cheating until I actually learned it.


print("Your body mass index is: ", round(weight / (height * height), 2))
#Here is where the code is printing the text and the result of the conversion.