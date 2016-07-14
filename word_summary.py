filename = raw_input("filename? ")

txt = open(filename)
content = txt.read()
content = content.replace(',', '').replace('.', '').replace('!', '').replace("\n", " ")
words = content.split(" ")
print words
tally = {}
for word in words:
    count = tally.get(word, 0)
    count = count + 1
    tally[word] = count
print tally
