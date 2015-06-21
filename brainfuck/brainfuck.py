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

    i = 0
    while i < len(script):
        c = script[i]

        if c == '>':
            ip+=1
            
        elif c == '<':
            ip-=1
        i+=1
