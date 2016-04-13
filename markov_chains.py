from random import choice
from sys import argv

def open_and_read_file(file_path, file_path_two):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # opens the entire file 

    content = open(file_path).read() + open(file_path_two).read()

    return content

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    
    # splits the text into a list of strings 
    words = text_string.split()

    chains = {}

    # iterates through the text and saves unique pairs of words into a dict; keeps track of the word that comes next 
    for i in range(len(words)-2):
        if (words[i], words[i+1]) in chains:
            chains[(words[i], words[i+1])].append(words[i + 2])
        else:
            chains[(words[i], words[i+1])] = [words[i + 2]]

    # for i in range(len(words)-2):
    #     word_tuple = (words[i], words[i+1])
    #     following_word = words[i+2]
    #     value = chains.get(word_tuple, [])
    #     value.append(following_word)
    #     chains[word_tuple] = value
    #     print chains
    #     print

    # finds the two last words in the file to prompt the random generator to stop 
    last_words = (words[-2], words[-1])

    return chains, last_words


def make_text(chains, last_words):
    """Takes dictionary of markov chains; returns random text."""

    punct_list = [".", "!", "?"]
    final_text = ["this", "won't", "work"]

    while final_text[-1][-1] not in punct_list:

        # Chooses a key to start at randomly and saves it to a working tuple 
        working_tuple = choice(chains.keys())

        # Continues choosing a new start word if the first character is not uppercase 
        while not working_tuple[0][0].isupper():
            working_tuple = choice(chains.keys())

        # Creates our list of strings that we add the selected words to
        final_text = list(working_tuple)

        # This counts the length of the Markov'd text, adding a space 
        len_of_text =  len(working_tuple[0]) + len(working_tuple[1]) + 1

        # continue to create new keys and add words as long as the length is less than 140 characters
        # and the last character is not a punctuation (?.!)
        # and the working pair of words is not equal to the last words of the text 

        while (len_of_text <= 140 and
               final_text[-1][-1] not in punct_list and 
               working_tuple != last_words):  
            word = choice(chains[working_tuple])
            len_of_text += len(word) + 1
            final_text.append(word)
            working_tuple = (working_tuple[1], word)

    # concatenates the words into the final text 
    return (" ").join(final_text)


input_path = argv[1] 
input_path_two = argv[2]

#Open the file and turn it into one long string
input_text = open_and_read_file(input_path, input_path_two)

# Get a Markov chain
chains, last_words = make_chains(input_text)

# Produce random text
random_text = make_text(chains, last_words)

print random_text
