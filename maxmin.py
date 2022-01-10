def max_min(*numbers):

# I use the *args which takes an indefinite arguments to allow me to enter multiple numbers
    
    return max(numbers),min(numbers)

# python has a maximum and minimumm inbuilt function that can return the max and min of any numbers 

print(max_min(1,2,3,4,5,10,30))
    