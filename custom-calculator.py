height = float(input("Input your height in meters: "))
#Here the code is asking for your height in meters, the value of the height will cange,
#based on the imput provided
weight = float(input("Input your weight in kilogram: "))
#The same is happening here with the weight as is with the height, 
#the value will be assigned based off of the umput
print("Your body mass index is: ", round(weight / (height * height), 2))
#Here is where the code processes the information and runs the formula of 
#Weight/height^2, and then prints the results