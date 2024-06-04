'''1. Create a variable named pi and store the value 22/7 in it.
Now check the data type of this variable.
2. Create a variable called for and assign it a value 4. See what
happens and find out the reason behind the behavior that you
see.
3. Store the principal amount, rate of interest, and time in
different variables and then calculate the Simple Interest for 3
years. Formula: Simple Interest = P x R x T / 100'''

'''1 creating a variable pi '''
pi = 22/7 
print(type(pi)) 
# output => <class 'float'>



''' 2 assigning 4 to for variable '''
for = 4 
print(for)

# output => SyntaxError: invalid syntax    because in python for is a reserved key word


'''3 simple interest'''

principle_amount = 10000
rate_of_interest = 8
time = 3

simple_interest = (principle_amount*rate_of_interest*time)/100
print("Simple Interest for 3 years:", simple_interest)

# output => Simple Interest for 3 years: 2400.0
