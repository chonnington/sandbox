

from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under']

word_counts = Counter(words)
top_three = word_counts.most_common(3)

print(top_three)  # Outputs [('eyes', 8), ('the', 5), ('look', 4)]]

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

for word in morewords:  # manually increment
    word_counts[word] += 1
print(word_counts)