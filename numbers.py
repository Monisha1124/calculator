def is_even(n):
    return n % 2 == 0

def square(n):
    return n * n

def cube(n):
    return n * n * n

if __name__ == "__main__":
    print("Is 10 even?", is_even(10))
    print("Square of 4:", square(4))
    print("Cube of 3:", cube(3))