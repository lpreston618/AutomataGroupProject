#########################################
# Theory of Automata Group Project      #
#########################################
# Kwasi Boamah
# William Cassell
# Raheema Kolleade
# Eli Ports
# Logan Preston
# William Vitzum


from typing import DefaultDict


class NFA:
    def __init__(self) -> None:
        self.alphabet = set()
        self.delta = {}
        self.start = None
        self.accepting = set()
        self.state_queue = []

    def fill_alphabet(self, s: str) -> None:
        for c in s:
            self.alphabet.add(c)

    def add_transition(self, state: str, symbol: str, next_state: str) -> None:
        self.delta[(state, symbol)] = next_state


def main():
    print("=== Group 19 Automata project. ===")
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
    automata = NFA()

if __name__ == "__main__":
    main()

