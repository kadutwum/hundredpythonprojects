intro ='''A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization.
Below is a function that takes a string and check if it is a palindrome. '''

print(intro)

def is_palindrome(phrase):
    #change phrase to lowercase
    phrase = phrase.lower()
    # initialize two new phrases to be compared
    original_phrase = ""
    reversed_phrase = ""
    # Loop throught each character in the phrase and for all non-space characters
    # add to the end of original_phrase, and to the front of reversed_phrase.
    for character in phrase:
        if not character.isspace():
            original_phrase = "{}{}".format(original_phrase,character)
            reversed_phrase = "{}{}".format(character,reversed_phrase)
    # Compare the two phrases
    if reversed_phrase == original_phrase:
        return True
    else:
        return False


print(is_palindrome("kofi")) # Should be False
print(is_palindrome("radar")) # Should be True

