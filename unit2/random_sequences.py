
from Crypto.Random import random


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


def generate_sequence(f,n):
    return list(map(f,range(n)))

def display_bits(sequence):    
    return "".join(str(x) for x in sequence)
    
def generate_fake_random(n):
"""
Generate fake random sequence - avoids more than 2 consequtive values
"""
    repetition = 0
    previous = None
    res = []
    for i in range(n):
        x = random.choice([0,1])
        if x == previous:
            repetition+=1
            if repetition > 2:
                x = (x+1)%2
                repetition = 1
                previous = x
        else:
            previous = x
            repetition = 1
        res.append(x)
    return res

def main():
    length = 88
    print(display_bits(generate_sequence(lambda n: 0 if n%3 == 0 else 1, length)))
    print("=")
    print(display_bits(string_to_bits("Anyone who considers arithmetical methods of production random digit is, of course, in a state of sin.")))
    print("=")
    print(display_bits(generate_sequence(lambda n: random.choice([0,1]),length)))
    print("=")
    print(display_bits(generate_fake_random(length)))
    print("=")

if __name__ == "__main__":
    main()


