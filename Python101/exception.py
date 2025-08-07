try:
    f = open("top-100.txt")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)
finally:
    print("This will always be printed")

n = 100
if n == 0:
    #Stop the program here and throw an error on purpose
    raise Exception("n cant be 0")
if type(n) is not int:
    raise Exception("n must be an int")

print(1/n)

n = 0
# expect this to be true. if not, crash the program with an AssertionError
assert(n != 0)
print(1/n)