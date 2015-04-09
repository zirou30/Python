#!/usr/bin/python

import sys, time

def main():
    print "Shell Encode"
    inputtype = raw_input("Por favor insera os dados: ")
    print "shellcode => ",
    for encoded in inputtype:
        print "\b\\x"+encoded.encode("hex"),
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
