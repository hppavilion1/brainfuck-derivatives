import re

tags = {
    (r"'[^']'",         'CHAR'),
    (r'<',              'MOVE'),
    (r'>',              'MOVE'),
    (r'\+',             'CHNG'),
    (r'-',              'CHNG'),
    (r'_',              'CHNG'),
    (r'\[',             'LOOP'),
    (r'\]',             'LOOP'),
    (r'\.',             'INOT'),
    (r',',              'INOT'),
    (r'[0-9]+',         'INTG'),
    (r'[^<>+-_\[\]\.,]+', None) #Comment
    }
def lex(script, tags):
    i = 0
    r = []
    while i < len(script):
        for x in tags:
            #print x
            m = re.match('^'+x[0], script[i:])
            if m:
                if x[1]:
                    r.append((m.group(0), x[1]))
                i+=len(m.group(0))
                print i
                break
        continue
        print i
    return r

r = raw_input()
print(len(r))
print('\n')
print(lex(r, tags))
