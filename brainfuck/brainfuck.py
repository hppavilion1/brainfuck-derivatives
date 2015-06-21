from __future__ import print_function

def lex(script):
    r = []
    for x in script:
        if x == '>':
            r.append(x)
        elif x == '<':
            r.append(x)
        elif x == '+':
            r.append(x)
        elif x == '-':
            r.append(x)
        elif x == '.':
            r.append(x)
        elif x == ',':
            r.append(x)
        elif x == '[':
            r.append(x)
        elif x == ']':
            r.append(x)
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
            if len(tape) < ip:
                tape.append(0)
            
        elif c == '<':
            ip-=1

        elif c == '+':
            tape[ip]+=1

        elif c == '-':
            tape[ip]-=1

        elif c == '.':
            print(chr(tape[ip]), end='')

        elif c == ',':
            tape[ip] = ord(raw_input())

        elif c == '[':
            if tape[ip] == 0:
                foundendend = 0
                i2 = 0
                while foundend != 1:
                    i2+=1
                    if script[i2] == '[':
                        foundend -= 1
                    elif script[i2] == ']':
                        foundend += 1
                i = i2
                
        elif c == ']':
            if tape[ip] == 0:
                foundendend = 0
                i2 = 0
                while foundend != 1:
                    i2-=1
                    if script[i2] == ']':
                        foundend -= 1
                    elif script[i2] == '[':
                        foundend += 1
                i = i2

        i+=1
