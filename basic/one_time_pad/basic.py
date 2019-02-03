#!/usr/bin/env python3
import pprint

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

if __name__ == "__main__":
    print("one_time_pad");

    converted = convert_to_bits(7,8)
    display_bits(converted)

    print("".join(map(str,converted)))


