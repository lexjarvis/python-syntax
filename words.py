def print_upper_words(words, must_start_with):
    """
    Prints out each word in the given list that starts with any of the letters in the given set, in all uppercase.

    Parameters:
    words (list): A list of strings representing the words to be printed.
    must_start_with (set): A set of characters representing the letters that the words must start with.

    Returns:
    None
    """
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())


# Testing the function
words = ["hello", "hey", "goodbye", "yo", "yes"]
print_upper_words(words, must_start_with={"h", "y"})
