#########################################
# Theory of Automata Group Project      #
#########################################
# Kwasi Boamah
# William Cassell
# Raheema Kolleade
# Eli Ports
# Logan Preston
# William Vitzum

import parsing

from typing import DefaultDict

class NFA:
    def __init__(self, parse_result) -> None:
        self.alphabet = set(parse_result[0])
        self.delta = DefaultDict(list)
        self.populate_delta(parse_result[4])
        self.start = parse_result[2]
        self.accepting = set(parse_result[3])
        self.state_queue = []

        self.current_state = self.start
        self.input = ""

    # Populates the transition function. Takes a list of lists of the form
    # [state, char, state], where the first two elements are the input and the
    # third element os the resulting state. As we're doing an NFA, we assume that
    # identical inputs can lead to different states, so in the transition function
    # dictionary we store a *list* of resulting states to go to.
    def populate_delta(self, transition_list) -> None:
        for t in transition_list:
            self.add_transition(t[0], t[1], t[2])

    # Add an individual transition to the transition function dictionary.
    def add_transition(self, state: str, symbol: str, next_state: str) -> None:
        self.delta[(state, symbol)].append(next_state)
    
    # Checks an input string to determine if all its characters are in the given
    # alphabet. Returns True if they are, and False otherwise.
    def checkAlphabet(self, input: str) -> bool:
        for c in input:
            if c not in self.alphabet:
                print(f"Unrecognized character '{c}'")
                return False
        return True

    # Perform a single step of computation. Return a boolean indicating whether
    # the NFA has accepted the string (True if accept, False otherwise)
    def compute_step(self) -> bool:
        if len(self.input) == 0:
            if self.current_state in self.accepting:
                # We're done! The input has been accepted.
                return True
            else:
                # This branch of computation has been rejected - return false and
                # add nothing to the queue.
                return False
        else:
            next_states = self.delta[(self.current_state, self.input[0])]
            for state in next_states:
                # Add all possible next states to the queue to search later
                self.state_queue.append((state, self.input[1:]))
            return False

    # Run a full computation on a given input. Prints whether the string is
    # accepted or rejected.
    def compute(self, input: str) -> None:
        # Check that the string contains only characters in the alphabet
        if not self.checkAlphabet(input):
            print("REJECT")
            return
        self.state_queue.clear()
        self.state_queue.append((self.start, input))
        while len(self.state_queue) != 0:
            self.current_state, self.input = self.state_queue.pop(0)
            accepted = self.compute_step()
            if accepted:
                print("ACCEPT")
                return
        # If we don't accept before the queue runs out, we reject.
        print("REJECT")



def main():
    print("=== Group 19 Automata project. ===")
    # Loop until a valid file is given
    while True:
        filename = input("Input file to load: ")
        try:
            with open(filename, "r") as f:
                contents = f.read()
                # If we succesfully read the file, exit the loop and continue
                break
        except IOError:
            print("Could not read the given file. Please try another.")

    # Parse the file, create and populate a new NFA
    # TODO: catch parsing errors for bad files
    parse_result = parsing.parse(contents)
    nfa_list = parse_result[0]
    test_inputs_list = parse_result[1]

    nfa = NFA(nfa_list)

    # If we were given strings to test, then test those.
    if test_inputs_list:
        for test_string in test_inputs_list:
            print(f"String {test_string}: ", end='')
            nfa.compute(test_string)
    # Otherwise, read strings from input.
    else:
        print('Enter strings to test. Type "quit" to leave the program.')
        while True:
            try:
                test_string = input("> ")
                if test_string == "quit":
                    break
                else:
                    nfa.compute(test_string)
            except EOFError:
                break # handle EOF cleanly.
        print("Goodbye.")


if __name__ == "__main__":
    main()

