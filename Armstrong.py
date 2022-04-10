number = input("Please enter a number: ")       
lenght = len(number)
result = 0
if str(number).isdecimal():
    for i in number:
        result += int(i) ** lenght
    if result == int(number):
        print(number, "is an Armstrong number.")  
    else:
        print(number, "is not an Armstrong number.")  
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!") 
