#! /usr/bin/env python3


multiple_line_string = """
this is to say
it's multiple line string

Yeah!
"""
print(multiple_line_string)

raw_string = r"raw\n string"
print(raw_string)

normal_string = "raw\nstring"
print(normal_string)

b1 = b"hello"
b2 = b"\x48\x65\x6c\x6c\x6f"  # also means "Hello"

print(b1)
print(b2)

# b1[2]+=1 doesn't work!!
ba = bytearray(b1)
ba[0] += 1  # Change 'h' to 'H'

print(ba)


# note! emojies fail in byte literals, they're utf8 not ASCII


name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I'm {age} years old."
print(greeting)

pi = 3.14159
print(f"{pi:.2f}")  # Output: 3.14

