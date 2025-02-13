def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage:
fizzbuzz(15)

def fizzbuzz(j):
    for k in range(2, j + 1):
        if  k % 4 == 1 and k % 7 == 0:
            print ("FizzBuzz")
        elif k % 4 == 1:
            print ("Fizz")
        elif k % 7 == 0:
            print ("Buzz")
        else:
            print (k)