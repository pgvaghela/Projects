'''
File: genome.py
Author: Pri Vaghela (CSC 120, 4:00 pm)
Description: The program is to create the GenomeData class that gets imported 
in phylo.py.
'''

class GenomeData:
    def __init__(self,name,sequence):
        '''
        intializing the name and sequence to the parameters and ngrams to an 
        empty set
        '''
        self._id = name
        self._sequence = sequence 
        self._ngrams = set()
    
    def create_ngrams(self, n):
        '''
        The method create_ngrams creates n-grams from the sequence by splitting
        it into substrings of length n.
        n - this parameter takes in an integer n for the substring length
        '''
        self._ngrams = \
            set(self._sequence[i:i+n] for i in range(len(self._sequence)-n+1))

    def get_id(self):
        '''
        The method get_id returns the id. 
        '''
        return self._id
    
    def get_sequence(self):
        '''
        The method get_sequence returns the sequence. 
        '''
        return self._sequence
    
    def get_ngrams(self):
        '''
        The method get_ngrams returns the ngrams. 
        '''
        return self._ngrams
    