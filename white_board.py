sentence = "Benedict Cumberbatch cannot say the word penguin correctly."

def norepeatingletters(s):
    p = []
    s2 = set()
    for c in s:
        if c in s2:
            p.append("_")
        else:
            p.append(c)
            s2.add(c)
    return ''.join(p)

print(norepeatingletters(sentence))