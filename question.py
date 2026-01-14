# from numpy import number


# n=int(input("enter a number"))
# if n>1:
#  for i in range (2,n):
#     n%i==0
#     print("not prime")
# else:
#   print("prime")










for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

