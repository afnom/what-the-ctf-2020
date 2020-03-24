# This one requires some maths.
# 
# Essentially, once we reverse engineer the program, we can work out that we
# calculate each character based on the XORs of all the characters occuring
# before it. We then repeat this process until we have at least 60 characters
# in the flag.
#
# The program runs too slowly, in fact, exponentially slowly, to even think
# about trying to run the program in the time limits of the CTF challenge.
#
# So to solve this challenge, we optimize the program to produce the flag
# quicker. Essentially, we realize that we aren't XORing with random bytes,
# it's the same bytes of the flag over and over again, which means that a lot
# of them will cancel out.
#
# If we arrange the characters we will XOR into blocks we get:
# f_1       + f_2       + ... + f_n    +
# f_(n + 1) + f_(n + 2) + ... + f_(2n) +
# ...
# f_(2^n - n + 1) + f_(2^n - n + 2) + ... + f_(2^n)
#
# where f_k is the `k`th character of the flag, and n is the current length of
# the flag.
#
# Note that f_(2^n) will probably not be in the bottom right corner, and there
# will be some blank spaces left! These are what we're interested in.
#
# From the diagram, we can see that each two rows will cancel out, so the only
# ones that actually have an effect on the final result are the ones at the end!
# 
# Mathematically this translates to only calculating from 0 to (2^n) % (2*n).
#
# This changes the computation of each character from an exponential
# calculation to a linear one, allowing us to quickly speed through and
# calculate the whole thing!

def generate():
    flag = list('AFNOM{')

    while len(flag) < 60:
        part = 0
        iters = (2 ** len(flag)) % (2 * len(flag))
        for i in range(iters):
            part ^= ord(flag[i % len(flag)])

        flag.extend(hex(part)[2:])

    flag.append('}')
    flag = ''.join(flag)
    print(flag)

if __name__ == "__main__":
    generate()
