
import random

def game():
    dsix =0
    list= []
    for i in range(0,20):
        num = random.randint(1,6)
        list.append(num)

    six = list.count(6)
    one = list.count(1)

    for i in range(0,len(list) -1):
        # print(list[i])
        if (list[i] == list[i+1]) :
            if(list[i]==6):

                dsix+=1

    print(list)
    print("Total 6 = ",six)
    print("Total 1 = ",one)
    print("Total double sixes = ",dsix)

game()
# program 2
print("\n")
print("Program 2")


def jj():
    print("Your goal is 100 jumping jacks")

    for i in range(1,101):
        
        if(i % 10 ==0):
            ans = input("Are you tired? ")
            if(ans == "yes" or ans=="y"):
                print(f"You completed a total of {i} jumping jacks!!")
                break
            if(ans == "no" or ans =='n'):
                print(f"{100 - i} jumping jacks are remaining.")

            if(i==100):
                print("Congratulations! You completed the workout ")

jj()
