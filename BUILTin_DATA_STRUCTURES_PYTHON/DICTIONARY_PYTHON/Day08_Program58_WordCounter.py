word = "MISSISSIPPI"
counter = {}

for letter in word:
    counter[letter] = counter.get(letter, 0) + 1

print("Letter Frequency:", counter)
