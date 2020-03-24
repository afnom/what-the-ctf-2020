import sys
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Password Check Program', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("password", help="The password to check")
    args = parser.parse_args()

    password = ''
    str = '65,98,70,120,78,68,79,88,77,115,123,97,80,82,121,73,55,108,104,84,48,86,110,101,95,80,82,83,51,107,95,85,49,72,53,118,95,102,87,109,49,81,99,67,107,77,51,90,100,113,125,69'

    intPass = str.split(",")

    for _i in range(len(intPass)):
        if _i % 2 == 0:
            password = password + chr(int(intPass[_i]))
   
    if args.password == password:
        print('Nice work!')
        print('The password is the flag!')
    
    else:
        print('Nope. Try again!')