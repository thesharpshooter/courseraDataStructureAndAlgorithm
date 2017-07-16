#Uses python2
text = raw_input()
n = int(raw_input())
patterns = []
for i in range(n):
    patterns.append(raw_input())

def formTrie(patterns):
    trie = {0:{}}
    node = 1
    for pattern in patterns:
        curr = 0
        for p in pattern:
            if p not in trie[curr]:
                trie[curr][p] = node
                trie[node] = {}
                node += 1
            curr = trie[curr][p]
    return trie

def patternMatch(text,patterns):
    res = []
    trie = formTrie(patterns)
    for i in range(len(text)):
        for j in range(len(text[i:])):
            currText = text[i:j]
            print currText
            found = match(trie,currText,i)
            if found != None and found not in res:
                res.append(found)
    return res

def match(trie,string,i):
    curr = 0
    for c in string:
        if trie[curr] == {}:
            return i
        if c in trie[curr]:
            curr = trie[curr][c]
        elif c not in trie[curr]:
            return None
    if trie[curr] == {}:
        return i
    else:
        return None

res = sorted(patternMatch(text,patterns))
for x in res:
    print x,
