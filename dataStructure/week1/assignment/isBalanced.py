#Uses python2
s = raw_input()
def isBalanced(s):
    a = []
    pos = []
    n = len(s)
    for i in range(n):
        if s[i] in "{[(":
            a.append(s[i])
            pos.append(i+1)
        elif s[i] in "}])":
            if len(a)==0:
                return False,i+1
            elif "{[(".index(a.pop())!= "}])".index(s[i]):
                return False,i+1
            else:
                pos.pop()
    if len(a) != 0:
        return False,pos[-1]
    else:
        return True,None

status,pos = isBalanced(s)
if status:
    print "Success"
else:
    print pos



