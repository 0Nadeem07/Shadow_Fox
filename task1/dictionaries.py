
print("Sub-program 1")
def friends():
    li = ["rahul" ,"rohit","shubham","preety","shri"]

    final =[]
    for item in li:
        tup=()
        l = len(item)
        tup = tup + (item,l)

        final.append(tup)

    print(final)

friends()

print("\n")
print("Sub-program 2")

def track():
    expense1 = {}
    my_exp = 0
    pat_exp =0
    expense2 = {}
    factor =["Hotel","Food","Transportation","Attractions","Miscellaneous"]

    for element in factor:
        print(f"Enter expense for {element}:")
        ex1 = int(input())
        my_exp+= ex1
        expense1[element] = ex1

    print(f"Total Expense of person 1: {expense1}")
    

    for element in factor:
        print(f"Enter expense for {element}:")
        ex2 = int(input())
        pat_exp+= ex2
        expense2[element] = ex2

    print(f"Total Expense of person 2: {expense2}")
    print('\n')


    print(f"person1:{my_exp} || person2:{pat_exp}")

# who spent most
    if(my_exp > pat_exp):
        print("Person 1 spent more money!")

    else:
        print("Person 2 spent more money!")

    # Calculate differences and find the key with the maximum difference

    common_keys = set(expense1.keys()).intersection(set(expense2.keys()))
    max_diff = 0
    key_with_max_diff = None

    for key in common_keys:
        diff = abs(expense1[key] -expense2[key])
        if diff > max_diff:
            max_diff = diff
            key_with_max_diff = key

    print(f"The key with the most difference is '{key_with_max_diff}' with a difference of {max_diff}.")


track()

