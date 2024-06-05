
'''1. Write a function that takes two arguments, 145 and 'o'
, and uses the `format` function to return a formatted string. Print the
result. Try to identify the representation used.'''

print("Subproblem 1")
def func(int ,char):
    return "{} students passed with grade {}.".format(int ,char)

result= func(145 ,'O')

print(result)
# output => 145 students passed with grade O.


print("\n")
'''2. In a village, there is a circular pond with a radius of 84 meters.
Calculate the area of the pond using the formula: Circle Area = π
r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
1.4 liters of water in a square meter, what is the total amount of
water in the pond? Print the answer without any decimal point in
it. Hint: Circle Area = π r^2 Water in the pond = Pond Area/
Water per Square Meter'''

print("Subproblem 2")
def pond(r ,pi):
    area = int(pi*r*r)
    print(f"Total area of the pond is {area} m^2")

    total_water = int(area / 1.4)
    print("Total amount of water in the pond is ",total_water ," litres")

pond(84,3.14)

print("\n")

'''3. If you cross a 490meterlong street in 7 minutes, calculate your
speed in meters per second. Print the answer without any decimal
point in it. Hint: Speed = Distance / Time'''

print("Subproblem 3")
distance = 490 
t_min= 7
t_sec = t_min *60 # converting minute into seconds

speed = int(distance /(t_sec)) 

print(f"Speed is {speed} m/s^2")