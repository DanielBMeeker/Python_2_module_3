"""
Program: text_analysis.py
Author: Daniel Meeker
Date: 9/15/2020

Text scraping code provided by professor and modified by Daniel Meeker
"""
import re

moby_dick_word_count = {}
sense_and_sensibility_word_count = {}
sentence_ending_punctuation = ['.', '!', '?']
moby_punctuation_count = -2  # starts at -2 Because of the periods after 'Chapter 1' and 'Loomings'
sense_and_sensibility_punctuation_count = 0  # this text file is cleaner and doesn't need to account for extra periods at the beginning
# Moby Dick Scraping:
with open('Moby_Dick_Chapter_1.txt', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        # First lowercase all characters in the line
        line = line.lower()
        # Get a count of the sentence ending punctuation
        for punctuation in line:
            if punctuation in sentence_ending_punctuation:
                moby_punctuation_count += 1
        # Next clean the line of any punctuation
        line_clean = re.sub(r'[^\w\s]', ' ', line)
        # Now split the line into words
        line_split = line_clean.split()
        # Now we can add the words to our dictionary
        for word in line_split:
            if word in moby_dick_word_count.keys():
                moby_dick_word_count[word] += 1
            else:
                moby_dick_word_count[word] = 1
# Sense and Sensibility Scraping:
with open('Sense_And_Sensibility_Chapter_1.txt', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        # First lowercase all characters in the line
        line = line.lower()
        # Get a count of sentence ending punctuation
        for punctuation in line:
            if punctuation in sentence_ending_punctuation:
                sense_and_sensibility_punctuation_count += 1
        # Next clean the line of any punctuation
        line_clean = re.sub(r'[^\w\s]', ' ', line)
        # Now split the line into words
        line_split = line_clean.split()
        # Now we can add the words to our dictionary
        for word in line_split:
            if word in sense_and_sensibility_word_count.keys():
                sense_and_sensibility_word_count[word] += 1
            else:
                sense_and_sensibility_word_count[word] = 1
# *commented out functions used in testing*
# print(moby_dick_word_count)
# sorted_moby_dick_word_count = sorted(moby_dick_word_count.items(), key=lambda x: x[1], reverse=True)
# print(punctuation_count)
total_moby_words = sum(moby_dick_word_count.values()) - 3  # minus 3 because I don't consider 'Chapter 1. Loomings.' to be part of the word count
# print(total_words)
words_per_sentence_moby = total_moby_words/moby_punctuation_count
# print(words_per_sentence)
total_sense_words = sum(sense_and_sensibility_word_count.values())
words_per_sentence_sense = total_sense_words/sense_and_sensibility_punctuation_count
print("How many times does the word 'old' appear in Chapter 1 of Moby Dick? " + str(moby_dick_word_count.get('old')))
print("How many times does the word 'water' appear in Chapter 1 of Moby Dick? " + str(moby_dick_word_count.get('water')))
print("What is the average length of a sentence in Chapter 1 of Moby Dick? " + str(round(words_per_sentence_moby, 2)) + " words")
print("How many times does the word 'old' appear in Chapter 1 of Sense and Sensibility? " + str(sense_and_sensibility_word_count.get('old')))
print("How many times does the word 'water' appear in Chapter 1 of Sense and Sensibility? " + str(sense_and_sensibility_word_count.get('water')))
print("What is the average length of a sentence in Chapter 1 of Sense and Sensibility? " + str(round(words_per_sentence_sense, 2)) + " words")
# sorted_sense_word_count = sorted(sense_and_sensibility_word_count.items(), key=lambda x: x[1], reverse=True)
# print(sorted_sense_word_count)
