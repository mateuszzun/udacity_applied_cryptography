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
            print(n)
    while len(result) < pad:
        result = [0] + result

    return result

if __name__ == "__main__":
    print("one_time_pad");

    converted = convert_to_bits(254,8)


    print("".join(map(str,converted)))


