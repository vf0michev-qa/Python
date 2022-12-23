n = int(input())
s = str(input())
b = str(input())

words = s.split()
res = 0
words_number = len(words)
word_len = []
for i in range(words_number):
    word_len.append(len(words[i]))

word_begin = []
word_begin.append(0)
word_begin_sum = 0
for i in range(words_number-1):
    word_begin_sum += len(words[i])
    word_begin.append(word_begin_sum)

h = 0
for i in range(words_number):
    h = word_begin[i]
    for j in range(word_len[i]-1):
        if b[h] == b[h+1]:
            res += 1
            break
        else:
            h += 1
print(res)