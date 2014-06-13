#!/usr/bin/env python

import sys
import random
import twitter

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

def add_start_words(random_num, tuple_list, random_text):

    start_words = tuple_list[random_num]
    random_text.extend(start_words)

    return random_text


def add_next_word(word_tuple, markov_chains, random_text):
    
    if word_tuple not in markov_chains:

        random_num = generate_random_number(markov_chains.keys())
        random_text = add_start_words(random_num, markov_chains.keys(), random_text)
        new_word_tuple = (random_text[-2],random_text[-1])
        add_next_word(new_word_tuple, markov_chains,random_text)

    else:

        possible_next_words = markov_chains[word_tuple]
        random_num = generate_random_number(possible_next_words)
        next_word = possible_next_words[random_num]
        random_text.append(next_word)

    return random_text

def make_text(markov_chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    random_num = generate_random_number(markov_chains.keys())
    random_text = []
    random_text = add_start_words(random_num, markov_chains.keys(), random_text)

    for i in range(100):
        word_tuple = (random_text[-2],random_text[-1])
        random_text = add_next_word(word_tuple, markov_chains, random_text)

    return random_text

def text_as_poem(random_text):

    poem_list = []

    for i in range(0,len(random_text),5):
        line = " ".join(random_text[i:i+5]) + '\n'
        poem_list.append(line)

    poem_length = len(poem_list)

    for i in range(poem_length/4,poem_length, poem_length/4):
        poem_list[i] += '\n'

    poem = " ".join(poem_list)

    return poem

def text_as_tweet(random_text):

    words_70 = random_text[:140]
    words_70_dict = {}

    for word in words_70:
        new_word = word + " "
        words_70_dict[new_word] = len(new_word)

    string_length = 0
    tweet_words = []

    for new_word in words_70_dict:
        string_length += words_70_dict[new_word]
        if string_length <= 140:
            tweet_words.append(new_word)

    tweet_string = "".join(tweet_words)

    return tweet_string

def main():

    args = sys.argv

    first_text_words = read_clean_file(args[1])
    second_text_words = read_clean_file(args[2])

    markov_chains = {}

    markov_chains = make_chains(markov_chains, first_text_words)
    markov_chains = make_chains(markov_chains, second_text_words)

    random_text = make_text(markov_chains)

    #poem = text_as_poem(random_text)

    tweet = text_as_tweet(random_text)

    print tweet

if __name__ == "__main__":
    main()