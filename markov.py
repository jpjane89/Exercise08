#!/usr/bin/env python

import sys
import random

def read_clean_file(args):

    filename = args[1]

    my_file = open(filename)
    text = my_file.read()
    my_file.close()

    text = text.replace("\n"," ")
    text = text.replace("--", " ")

    words = text.split(" ")
    
    clean_words = []

    for word in words:

        if word != "": 
            #clean_word = word.strip('".,!?#:;()/*&')
            #clean_word = clean_word.strip("'")

            clean_words.append(word)

    return clean_words

def make_chains(clean_words):

    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    markov_chains = {}

    for i in range(len(clean_words)-2):

        tuple_word1 = clean_words[i]
        tuple_word2 = clean_words[i+1]
        value = clean_words[i+2]

        if (tuple_word1, tuple_word2) not in markov_chains:
            markov_chains[(tuple_word1, tuple_word2)] = [value]
        else:
            markov_chains[(tuple_word1, tuple_word2)].append(value)

    return markov_chains

def generate_random_number(return_list):

    random_num = random.randint(0,len(return_list)-1)

    return random_num

def add_start_words(random_num,return_list):

    random_text = []

    start_words = return_list[random_num]

    word1, word2 = start_words

    random_text.append(word1)
    random_text.append(word2)

    return random_text

def add_next_word(random_text, markov_chains):

    word_tuple = (random_text[-2],random_text[-1])

    possible_next_words = markov_chains[word_tuple]

    random_num = generate_random_number(possible_next_words)

    next_word = possible_next_words[random_num]

    random_text.append(next_word)

    return random_text

def make_text(markov_chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    random_num = generate_random_number(markov_chains.keys())

    random_text = add_start_words(random_num,markov_chains.keys())

    for i in range(100):
        random_text = add_next_word(random_text,markov_chains)
        i+=1

    return random_text

def main():
    args = sys.argv

    words = read_clean_file(args)

    markov_chains = make_chains(words)

    random_text = make_text(markov_chains)

    random_text = " ".join(random_text)

    print random_text

if __name__ == "__main__":
    main()