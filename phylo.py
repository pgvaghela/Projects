'''
File: phylo.py
Author: Pri Vaghela
Description: The program constructs phylogenetic trees starting from the genome
sequences of a set of organisms. It performs phylogenetic analysis on genetic 
data stored in a FASTA file. The tree constructed based on the similarity of 
the genetics. 
'''

from genome import GenomeData
from tree import TreeNode

def read_fasta_file(filename, n_gram):
    '''
    The function read_fasta_file reads in the FASTA file and creates a 
    dictionary of GenomeData objects with their corresponding n-grams and 
    returns this dictionary of genome data.
    filename - this parameter takes in the name of the FASTA file
    n_gram - takes in the n_gram size
    '''
    # using with to open the file and assign it to "file"
    with open(filename, "r") as file:
        sequence_dict = {}
        sequence_lst = []
        for line in file:
            if line == "\n":
                sequence_lst = []
            elif line[0] == ">":
                name, *rest = line[1:].strip().split()
                # *rest is used to unpack any remaining elements of the line 
                # into a list called rest
                sequence_dict[name] = sequence_lst
            else:
                sequence_lst.append(line.strip())
        genome_data = {}
        # creating GenomeData objects for each name-sequence pair in the 
        # new_dict
        for name, sequence in sequence_dict.items():
            genome = GenomeData(name, "".join(sequence))
            genome.create_ngrams(n_gram)
            genome_data[name] = genome
        return genome_data

def compute_similarity(ngram1, ngram2):
    '''
    The function compute_similarity takes in two sets of n-grams and calculates 
    their Jaccard similarity. The output of this function is a float value 
    between 0 and 1, where 0 indicates no similarity between the two sets and 1
    indicates that the two sets are identical.
    ngram1 - this parameter takes in the first set of n_gram
    ngram2 - this parameter takes in the second set of n_gram
    '''
    return len(ngram1.intersection(ngram2)) / len(ngram1.union(ngram2))

def construct_phylogenetic_tree(genome_data):
    '''
    The function construct_phylogenetic_tree computes the pairwise similarity 
    scores between all pairs of genomes using the compute_similarity function, 
    and creates a phylogenetic tree based on these scores.
    genome_data - this paramter takes in the dictionary of genome data where 
    each genome is represented as a GenomeData object
    '''
    similarity_data = {}
    # computing the similarity between each pair of GenomeData objects
    for data1 in genome_data:
        for data2 in genome_data:
            if data1 != data2:
                similarity_data[(data1, data2)] = \
                    compute_similarity(genome_data[data1].get_ngrams(), \
                                       genome_data[data2].get_ngrams())
    tree_lst = []
    # creating TreeNode objects for each name in genome_data
    for name in genome_data:
        tree = TreeNode(name)
        tree.add_id(name)
        tree_lst.append(tree)
        # iterating until there is only one tree object in the list
        # fun fact: the complexity for the following nested loops is O(n^5)
    while len(tree_lst) > 1:
        max_similarity = 0.0
        # iterating over each pair of TreeNode objects in the tree_list
        for node1 in tree_lst:
            for node2 in tree_lst:
                if node1 != node2:
                    for id1 in node1.set_id():
                        for id2 in node2.set_id():
                            # if the similarity between the two pairs is 
                            # greater than the max_similarity, updating 
                            # max_similarity and the nodes
                            if (id1,id2) in similarity_data:
                                similarity = similarity_data[(id1,id2)]
                            if similarity > max_similarity:
                                max_similarity = similarity
                                t1,t2 = node1, node2
        # creating a new TreeNode object with the ids of the two nodes with 
        # the highest similarity 
        new_node = TreeNode(None)
        new_node.add_id(t1.get_id())
        new_node.add_id(t2.get_id())
        if str(t1) < str(t2):
            new_node.set_left(t1)
            new_node.set_right(t2)
        else:
            new_node.set_left(t2)
            new_node.set_right(t1)
        tree_lst.remove(t1)
        tree_lst.remove(t2)
        tree_lst.append(new_node)
    return tree_lst[0]

def main():
    '''
    The main function asks the user for the FASTA file and the n-gram size.
    It then calls the functions to achieve the necessary output and prints the 
    root of the phylotree. 
    '''
    fasta_filename = input('FASTA file: ')
    n_gram = int(input('n-gram size: '))
    genome_data = read_fasta_file(fasta_filename, n_gram)
    phylotree_root = construct_phylogenetic_tree(genome_data)
    print(phylotree_root)

main()
# calling main
