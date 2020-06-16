# Taking input from the user for lower limit of the range.
lower=int(input("Enter the lower limit for the range: "))

# Taking input from the user for the uper limit of the range.
upper=int(input("Enter the upper limit for the range: "))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
