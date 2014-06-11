#!/usr/bin/env python

import sys
import random

def read_clean_file(argument):

    clean_words = []

    filename = argument

    my_file = open(filename)
    text = my_file.read()
    my_file.close()

    words = text.split()

    for word in words:

        if word != "" and word.isdigit() == False:
            clean_words.append(word)

    return clean_words

def make_chains(markov_chains, clean_words):

    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    for i in range(len(clean_words)-2):

        tuple_words = (clean_words[i], clean_words[i+1])
        value = clean_words[i+2]

        if tuple_words not in markov_chains:
            markov_chains[tuple_words] = [value]
        else:
            markov_chains[tuple_words].append(value)

    return markov_chains

def generate_random_number(return_list):

    random_num = random.randint(0,len(return_list)-1)

    return random_num

def generate_start_words(random_num, tuple_list):

    start_words = tuple_list[random_num]

    return start_words


def add_next_word(word_tuple, markov_chains):
    
    # if word_tuple not in markov_chains:

    #     return None

    #     # random_num = generate_random_number(markov_chains.keys())

    #     # word_tuple = generate_start_words(random_num, markov_chains.keys())

    #     # add_next_word(word_tuple, markov_chains)

    # else:

    possible_next_words = markov_chains[word_tuple]

    random_num = generate_random_number(possible_next_words)

    next_word = possible_next_words[random_num]

    return next_word

def make_text(markov_chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    random_num = generate_random_number(markov_chains.keys())

    random_text = []

    start_words = generate_start_words(random_num, markov_chains.keys())
 
    random_text.extend(start_words)


    for i in range(500):
        word_tuple = (random_text[-2],random_text[-1])
        next_word = add_next_word(word_tuple, markov_chains)
        random_text.append(next_word)

    return random_text

def main():
    args = sys.argv

    first_text_words = read_clean_file(args[1])

    second_text_words = read_clean_file(args[2])

    markov_chains = {}

    markov_chains = make_chains(markov_chains, first_text_words)
    markov_chains = make_chains(markov_chains, second_text_words)

    random_text = make_text(markov_chains)

    stanza1 = " ".join(random_text[0:(len(random_text)/4)])
    stanza2 = " ".join(random_text[(len(random_text)/4):(len(random_text)/2)])
    stanza3 = " ".join(random_text[(len(random_text)/2):(3*(len(random_text)/4))])
    stanza4 = " ".join(random_text[(3*(len(random_text)/4)):])

    random_stanzas = stanza1 + 2*"\n" + stanza2 + 2*"\n" + stanza3 + 2*"\n" + stanza4 + 2*"\n"

    print random_stanzas


if __name__ == "__main__":
    main()