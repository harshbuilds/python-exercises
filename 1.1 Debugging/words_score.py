# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = input().split()

def score_words(words):
    score = 0
    for word in words:
        vowels = 0
        for char in word:
            if char in 'aeiouy':
                vowels += 1
        score += 2 - (vowels%2)
    return score

print(score_words(words))
