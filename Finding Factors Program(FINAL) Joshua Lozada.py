from tkinter import *

print("Finding Factors Program by Joshua Lozada")

name=input("what is your name?")
print ("Hello",name, " Welcome To My Finding factors Program")


def factor_finder(x): #define something
    print("The factors of",x,"are:")
    for i in range(1, x + 1):     #In order to find factors of a number, we have to run a loop over all numbers from 1 to itself and see if it is divisible. 
        if x % i == 0:
            print(i)
        



#try:  
#    num = int(input("Enter a number: "))
#    factor_finder(num)
#except ValueError:
#    print("Sorry, I didn't understand that.");
    
#When you try to convert non numeric string to int, suppose the input was 'abc' or any other non numeric string,
#it will throw an ValueError. int(input('Enter a number)) => input is 'ab' => int('ab') =>
#This will throw ValueError. the statements that throw the Error or exceptions are to be kept inside try block.
#immediately after the try block catch block should be placed. The catch block will catch the exception throw from the try block
#and executes the statements written in catch block. Note: Once the error is thrown,
#the statements next to line which threw error are not executed further 


    
while True:
    try:
        num = int(input("Enter an integer (0 to exit): "))
        if num == 0:
             window = Tk()
             window.title("Thank you!")
             window.configure(background="black")
             Label (window, bg="black") 
             Label(window, text = "Thank You "+name+" For Using My Program!" , bg ="black", fg="white", font= "none 12 bold") .grid(row=0, column=0,sticky=W)
             window.mainloop()
             break
        factor_finder(num)
    except ValueError:
        print("Sorry, you must enter an integer")
