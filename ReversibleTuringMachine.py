class ReversibleTuringMachine:
    def __init__(self, states, input_symbols, queue_symbols, transitions):
        self.states = states
        self.input_symbols = input_symbols
        self.queue_symbols = queue_symbols
        self.transitions = transitions    
        
    def makeTransitions(self, state_marker, head_marker, input_tape, history_tape):
        while(state_marker != int((self.states))):
            nt = 0
            for i in self.transitions:
                if(state_marker == int(i.current_state)):
                    if(input_tape[head_marker] == i.read_symbol):
                        state_marker = int(i.next_state)
                        input_tape[head_marker] = i.write_symbol
                        if(i.head_movement == "L"):
                            head_marker -= 1
                        elif(i.head_movement == "R"):
                            head_marker += 1
                        history_tape.append(nt) #guarda num transitions
                nt += 1

    def reverse_movement(self,history_tape, head_marker, input_tape):
        i = len(history_tape) - 1
        while i >= 0:
            name = history_tape[i]
            if self.transitions[name].head_movement == "R":
                head_marker -= 1
            elif self.transitions[name].head_movement == "L":
                head_marker += 1
            i-= 1
            history_tape.pop()
            input_tape[head_marker] = self.transitions[name].read_symbol
