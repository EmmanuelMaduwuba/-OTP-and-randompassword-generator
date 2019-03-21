import random
import math
import itertools
import string

name = input("Input number for verification code:")
print(name)


def generateOTP():
    OTP = "0123456789"
    code = ""
    for i in range(4):
        code += OTP[random.randint(0, 9)]
    return code


if __name__ == "__main__":
    print("Your OTP IS :", generateOTP())


def pseudorandom(stringLength=10):
    lettersandnumbers = string.ascii_letters + string.digits
    generator = ""
    return generator.join(random.choice(lettersandnumbers)
                          for i in range(stringLength))


if __name__ == "__main__":
    print("Feeling Lazy? Use this secure password: ", pseudorandom())


def newpassword():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678=^%$#"
    password = ""
    for i in range(10):
        gen = random.choice(characters)
        password += gen
    return password


if __name__ == "__main__":
    print('Another way to generate random passwords :', newpassword())
