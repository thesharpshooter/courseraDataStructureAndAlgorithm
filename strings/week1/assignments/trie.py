#Uses python2
import sys
n = int(raw_input())
patterns = []
for i in range(n):
    patterns.append(raw_input())
trie = {}
def constructTrie(pattern,trie):
    curr = 0
    count = 0 if len(list(trie))== 0 else max(list(trie))
    for i in range(len(pattern)):
        if curr not in trie:
            trie[curr] = {}
        if curr in trie and pattern[i] in trie[curr]:
            curr = trie[curr][pattern[i]]
        elif pattern[i] not in trie[curr]:
            trie[curr][pattern[i]] = count+1
            count += 1
            curr = count
    return trie
for x in patterns:
    trie = constructTrie(x,trie)
for node in trie:
    for c in trie[node]:
        print("{}->{}:{}".format(node, trie[node][c], c))

