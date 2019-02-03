#!/usr/bin/env python3
import pprint
import math

def convert_to_bits(n, pad):
    result = []
    while n > 0:
            if n%2 == 0:
                result = [0] + result
            else:
                result = [1] + result
            n = int(n/2)
    while len(result) < pad:
        result = [0] + result

    return result

def string_to_bits(s):
    result = []
    for c in s:
        result = result + convert_to_bits(ord(c), 7 )
    return result

def display_bits(bits):
    print("".join(str(x) for x in bits))


def xor(a, b):
    if len(a) != len(b):
        raise NotImplementedError("why i am here? length a and b are different in xor fcn")
    return [a^b for a,b in zip(a,b)]

def main():
    print("one_time_pad");

    converted = convert_to_bits(7,8)
    display_bits(converted)

    print("".join(map(str,converted)))


    print("Lesson2 ProblemSet 1, 5th Quiz")

    Y = string_to_bits("Y")
    N = string_to_bits("N")

    M = [1,0,0,1,1,1,0]

    print("Y and N xor:")
    changer = xor(Y,N)

    display_bits(changer)

    print("XOR changer with ciphertext")
    display_bits(xor(changer,M))

    print("Lesson2 ProblemSet 1, 6th Quiz")

    print("number of possible keys: 26!")

    factorial26 = math.factorial(26)
    print(factorial26)

    print("number of possible messages for given lenght")
    n = 1
    space = 26 ** n
    while space < factorial26:
        n = n + 1
        space = 26 ** n
        print("{}: {}".format(n, space))
    print("Result {}".format(n))
    


    
if __name__ == "__main__":
    main()


