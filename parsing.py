#########################################
# Theory of Automata Group Project      #
#########################################
# Kwasi Boamah
# William Cassell
# Raheema Kolleade
# Eli Ports
# Logan Preston
# William Vitzum

# Code for parsing the S-expression form of the machine files

import pyparsing as pp

m_list = pp.Forward() # define a recursive element

atom = pp.Word(pp.alphanums + "_") # Words can have letters, numbers, and underscores

# A list can be just an atom, or can contain any number (including 0) of atoms and lists
m_list <<= (atom | pp.Suppress("(") + pp.Group(pp.ZeroOrMore(m_list)) + pp.Suppress(")"))

# Take in a string describing an NFA and return a nested list of strings.
# Ex: (((1,0), (a, b), a, (b), ((a, 0, b)))), (110)) becomes the Python list
# [
#   [
#       ['1','0'], ['a','b'], 'a', ['b'], [['a', '0', 'b']]
#   ],
#   [
#       ['110']
#   ]
# ]
# This is desirable because we can then simply extract all the data we need from
# these lists.
def parse(machine: str):
    m = machine.replace(",", "") # commas are irrelevant for parsing
    return m_list.parse_string(m)[0] # unwrap outermost list returned by pyparsing
