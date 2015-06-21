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
        i+=1
