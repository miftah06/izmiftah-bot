import os


def read():
    with open('ips.txt', 'r+') as fh:
        lines = fh.read()
        for line in lines:
            os.system('nslookup' + str(line))
            print(line)
            write(line)


def write(res):
    with open('results.txt', 'w+') as fh2:
        fh2.write(res)


if __name__ == "__main__":
    read()
