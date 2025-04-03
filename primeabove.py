num = int(input("Enter a number: "))
def is_prime(n):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
               print("Not a Prime Number")
               break
    else:
        print("Prime Number")
next_num = num + 1
next_num += 1
print("Next Prime Number:", next_num)
