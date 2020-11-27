alphabet = "abcdefghjklmnopqrstuvwxyz"

sentence = input("Enter your sentence: ")
output = ""
for letter in sentence:
    # find letter in alphabet
    letterval = alphabet.find(letter)
    # move two letters across
    letterval += 2
    # make sure we haven't gone off the end
    letterval = letterval % 26
    # add to output
    output += alphabet[letterval]

print(output)


