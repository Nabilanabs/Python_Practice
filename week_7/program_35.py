try:
    print("Block=Try.")
    x = 1 / 0  # It's gonna cause Error cause of dividing by 0 is not allowed in python

except:
    print("Block=Expect.")

finally:
    print("Block=Finally.")

#try - runs firstly on your code

#expect - is gonna run after you face any errors in your first block of code

#finally - gonna run no matter what