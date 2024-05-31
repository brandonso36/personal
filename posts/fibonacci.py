start = input("Enter a non-negative integer:") # gets user inputi
start = int(start) # converts input into an integer

if start < 0: #Only counts positive integers
    print("Enter a non-negative integer input")

elif start == 0: # if zero is inputted then the sequence displays 0
    print("0")

elif start > 0: # takes valid inputs
    a = 0
    b = 1
    for i in range (0, start): # repeats for the number entered times
        print(a)
        c = a + b
        a = b 
        b = c
        
else: # filters out inputs that arent integers
    print("Enter a valid input")
