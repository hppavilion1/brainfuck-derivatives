from __future__ import print_function
import re
import sys

STRING       = 'STRING'
CHAR         = 'CHAR'
EXP          = 'EXPRESSION'
CELLCOMMAND  = 'cCOMMAND'
TAPECOMMAND  = 'tCOMMAND'
STACKCOMMAND = 'sCOMMAND'

def lex(script):
    r = []
    s = 0
    matchables = {(r'"[^"]*',    STRING),
                  (r'\'.\'',     CHAR),
                  )r'\'.{2,}\'', EXP
                  (r'\+',        CELLCOMMAND),
                  (r'-',         CELLCOMMAND),
                  (r'>',         TAPECOMMAND),
                  (r'<',         TAPECOMMAND),
                  ()
                  }

    while s < len(script):
        for x in matchables:
            
            if re.match(x[0], script[s:]):
                r.append((re.groups()[1], x[1]))
        
        s+=len(re.groups()[1])
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
