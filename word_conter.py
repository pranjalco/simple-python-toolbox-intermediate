def word_counter():
    """This function takes sentence from user and splits it, and return the count of the number
    of words in the sentence."""

    border = ('-' * 40)

    # Taking sentence from user as input
    sentence = input("Please enter a sentence:\n")
    print(f"\n{border}\n")

    # Counting words in sentence by splitting the sentence by spaces
    word_count = len(sentence.split())

    # Checking if count is zero or not incase if user did not enter any input
    if word_count == 0:
        print("No words or sentence entered, so the count is 0.")
        print(f"\n{border}\n")
    else:
        print(f"Total count of words in your sentence is {word_count}")
        print(f"\n{border}\n")

    # Returning the final word count
    return word_count


word_counter()
