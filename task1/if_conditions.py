print("Sub-problem 1")
def BMI():
    height = float(input("Enter height (in meters): "))
    weight = float(input("Enter weight (in kg): "))

    BMI = weight / (height * height)

    if(BMI<18.5):
        print("Underweight")

    elif(18.5<= BMI <25):
        print("Normal")
    
    elif(25<= BMI <= 29):
        print("Overweight")

    elif(BMI >= 30):
        print("Obesity")
    
    # print(BMI)
BMI()


#   ----------------------------   #
print("\n")
Australia = ["Sydney","Melbourne" ,"Brisbane","Perth"]

UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]

India = ["Mumbai","Bangalore","Chennai","Delhi"]
#   ----------------------------   #
print("Sub-program 2")
def country_guess(l1,l2,l3):
    print('''Australia = ["Sydney","Melbourne" ,"Brisbane","Perth"]

            UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]

            India = ["Mumbai","Bangalore","Chennai","Delhi"]''')
    print("\n")


    city = input("Enter a city name: ")

    if(city in Australia):
        print(f"{city} is in Australia")
    
    elif(city in UAE):
        print(f"{city} is in UAE")

    elif(city in India):
        print(f"{city} is in India")

    else:
        print("Enter the city from given list! ")

country_guess(Australia,UAE,India)




print("\n")
print("Sub-program 3")

def cities(l1,l2,l3):
    city1 = input("Enter the first city:")
    city2 = input("Enter the second city:") 

    if(city1 and city2 in Australia):
        print("Both cities are in Australia")

    elif(city1 and city2 in UAE):
        print("Both cities are in UAE")

    elif(city1 and city2 in India):
        print("Both cities are in India")

    else:
        print("Both cities are in different countries")


cities(Australia,UAE,India)




