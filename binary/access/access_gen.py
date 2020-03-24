import sys
import py_compile

## AFNOM{Py7h0n_R3_15_W1ck3d}
## bxDXsaRIlTVePSkUHvfmQCMZqE
## AFNOM{Py7h0n_R3_15_W1ck3d}
s1 = 'AFNOM{Py7h0n_R3_15_W1ck3d}'
s2 = 'bxDXsaRIlTVePSkUHvfmQCMZqE'
s = 'AbFxNDOXMs{aPRyI7lhT0Vne_PRS3k_U1H5v_fWm1QcCkM3Zdq}E'
ints1 = [65, 98, 70, 120, 78, 68, 79, 88, 77, 115, 123, 97, 80, 82, 121, 73, 55, 108, 104, 84, 48, 86, 110, 101, 95, 80]
ints2 = [82, 83, 51, 107, 95, 85, 49, 72, 53, 118, 95, 102, 87, 109, 49, 81, 99, 67, 107, 77, 51, 90, 100, 113, 125, 69]
    
def alt(s, t):
    if not s:
        return t
    elif not t:
        return s
    else:
        return s[0] + t[0] + alt(s[1:], t[1:])

def ctoi(s):
    ints = []
    for _s in s:
        ints.append(ord(_s))
    return ints

py_compile.compile('access.py')

# print(alt(s1, s2))
# ints = (ctoi(s))
# print(','.join([str(_i) for _i in ints[:26]]))
# print(','.join([str(_i) for _i in ints[26:]]))


