class Transition:
    def __init__(self, transition):
        self.current_state, self.read_symbol = transition[transition.index("(") + 1:transition.index(")")].split(",")
        transition = transition[transition.index("=") + 1:]

        self.next_state, self.write_symbol, self.head_movement = transition[transition.index("(") + 1:transition.index(")")].split(",")

        self.current_state = self.current_state
        self.next_state = self.next_state

    def __str__(self):
        return "({},{})=({},{},{})".format(self.current_state, self.read_symbol, self.next_state, self.write_symbol, self.head_movement)