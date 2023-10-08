'''
File: rhymes.py
Author: Pri Vaghela
Description: This code creates a dictionary of words as the keys and their 
respective rhyme stressors as the values. The code prints rhyming words to the
one input by the user using the user input dictionary of phenomes. 
'''

def read_input_file(file_name):
    '''
    The function read_input_file takes in the file name and then using creates 
    a list of lines using strip and split.
    file_name - this parameter takes in the name of the file.
    '''
    # using with function to open file
    with open(file_name, 'r') as file:
        lines = []
        # going through all of the lines in then file
        for line in file:
            lines.append(line.strip().split())
    return lines

def create_word_dict(lines):
    '''
    The function create_word_dict creates a dictionary with each word as the 
    key and a list of its respective phonemes as the value.
    lines - this parameter takes in the a list of lines. 
    '''
    word_dict = {}
    for line in lines:
        # extract the word from the current line
        word = line[0]
        if word not in word_dict:
            word_dict[word] = []
        # append the rhyme stressor for the current word to its value list
        word_dict[word].append(line[1:])
    return word_dict

def break_word_in_pieces(word_dict, word):
    '''
    The function break_word_in_pieces breaks the word into phoneme pieces and 
    returns a list of tuples containing three elements: the preceding phoneme, 
    the current phoneme, and the remaining phonemes.
    word_dict - this parameter takes in the dictionary made in the 
    create_word_dict function.
    word - this is the string of which the rhyming words are to be found.
    '''
    word_pieces = []
    # get the phoneme sets for the given word from the word_dict dictionary
    phoneme_sets = word_dict.get(word.upper(), [])
    # loop through each phoneme set for the word
    for phoneme_set in phoneme_sets:
        # loop through each phoneme in the phoneme set
        for i in range(len(phoneme_set) - 1):
            # loop through each character in the phoneme
            for j in range(len(phoneme_set[i])):
                if phoneme_set[i][j] == '1':
                    # add a tuple of the surrounding phonemes and stress marker 
                    # to word_pieces list
                    word_pieces.append((phoneme_set[i-1], phoneme_set[i],\
                                    phoneme_set[i+1:]))
    return word_pieces

def find_rhyming_words(word_pieces, word_dict):
    '''
    The function find_rhyming_words checks all the phoneme sets in the 
    word_dict dictionary for words that rhyme with the input word, based on the 
    phoneme sets generated for the input word in the break_word_in_pieces 
    function. It then returns a sorted list of the matching words.
    word_pieces - this parameter takes in a list of tuples containing phoneme 
    sets for the input word.
    word_dict - this parameter takes in the dictionary made in the 
    create_word_dict function. 
    '''
    rhyming_words = []
    for piece in word_pieces:
        # loop through each word in the dictionary
        for word, phoneme_sets in word_dict.items():
            # loop through each phoneme set in the word
            for phoneme_set in phoneme_sets:
                # loop through each phoneme in the phoneme set
                for i in range(len(phoneme_set) - 1):
                    # if the phoneme matches the last phoneme in the word piece
                    if phoneme_set[i] == piece[1]: 
                        # if the remaining phonemes in the phoneme set match 
                        # the remainder of the word piece
                        if phoneme_set[i + 1:] == piece[2]:    
                            # if the previous phoneme in the phoneme set 
                            # doesn't match the first phoneme in the word piece
                            if phoneme_set[i - 1] != piece[0]:
                                # add the word to the list of rhyming words
                                rhyming_words.append(str(word))
    return sorted(rhyming_words)
    
def main():
    '''
    The main function inputs the file name of the .txt file that contains the 
    phoneme data. It then prints the words from the list of rhyming words found 
    in find_rhyming_words.
    '''
    file_name = input()
    word = input()
    lines = read_input_file(file_name)
    word_dict = create_word_dict(lines)
    word_pieces = break_word_in_pieces(word_dict, word)
    found_words = find_rhyming_words(word_pieces, word_dict)
    for word in found_words:
        print(word)

main()
# calling main