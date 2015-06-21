from __future__ import print_function
import sys

def lex(script):
    r = []

    return r

def execute(script):
    script = lex(script)

    tape = [0]
    ip = 0
    i = 0
    while i < len(script):
        c = script[i]

        if c == '>':
            ip+=1
            while len(tape)-1 < ip:
                tape.append(0)

        elif c == '<':
            ip-=1

        elif c == '+':
            tape[ip]+=1
            tape[ip]%=256

        elif c == '-':
            tape[ip]-=1
            tape[ip]%=255

        elif c == '.':
            print(chr(tape[ip]), end='')

        elif c == ',':
            tape[ip] = ord(raw_input())

        elif c == '[':
            if tape[ip] == 0:
                foundend = 0
                i2 = i
                while foundend != 1:
                    i2+=1
                    if script[i2] == '[':
                        foundend -= 1
                    elif script[i2] == ']':
                        foundend += 1
                i = i2
                
        elif c == ']':
            if tape[ip] != 0:
                foundend = 0
                i2 = i
                while foundend != 1:
                    i2-=1
                    if script[i2] == ']':
                        foundend -= 1
                    elif script[i2] == '[':
                        foundend += 1
                i = i2

        elif c == '#':
            print('Debug: '+', '.join(tape))
        i+=1

if __name__ == '__main__':
    try:
        execute(open(sys.argv[1]).read())
    except:
        execute(open(raw_input()).read())
