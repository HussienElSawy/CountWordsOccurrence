file = open("quran.txt", "r", encoding="utf-8")
content = file.read()
file.close()
words = content.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
sorted_dict = dict(sorted(word_counts.items(), key=lambda item: item[1]))
file = open("result.txt", "w", encoding="utf-8")
for word, count in sorted_dict.items():
    file.write(word+": "+str(count)+"\n")
