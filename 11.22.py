wordlist = list(input().split(" "))

wordfreq = []


for w in wordlist:
    wordfreq.append(wordlist.count(w))

for i in range(len(wordlist)):
    print(wordlist[i], wordfreq[i])