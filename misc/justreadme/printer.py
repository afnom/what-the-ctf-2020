import subprocess

FLAG = 'AFNOM{N07_7hA7_hARD_i5_I7}'

def main():
    proc = subprocess.run(['figlet', FLAG, '-w', '1000'], stdout=subprocess.PIPE)
    lines = proc.stdout.decode().split('\n')
    maxlen = max(len(line) for line in lines)

    final = '| '.join(line + ' ' * (maxlen - len(line)) for line in lines)
    print(final)

if __name__ == "__main__":
    main()