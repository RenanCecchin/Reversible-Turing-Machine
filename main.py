import sys
from Transition import Transition
from State import State
from copy import copy
from ReversibleTuringMachine import ReversibleTuringMachine

if(sys.argv[1] != None):
    content = open(sys.argv[1], 'r').readlines()
    num_states, num_input_symbols, num_queue_symbols, num_transitions = content[0].split()
    str_states = content[1].split()
    states = []

    for state in str_states:
        states.append(State(state))

    input_symbols = content[2].split()
    queue_symbols = content[3].split()
    transitions = []

    for i in range(4, 4 + int(num_transitions)):
        transitions.append(Transition(content[i]))
        
    reversibleTuringMachine = ReversibleTuringMachine(num_states, input_symbols, queue_symbols, transitions)

    state_marker = 1
    head_marker = 0
    entry = content[-1]
    input_tape = entry + "B"
    input_tape = list(input_tape)
    history_tape = []

    reversibleTuringMachine.makeTransitions(state_marker, head_marker, input_tape, history_tape)
    output_tape = copy(input_tape)

    print("FITA DE INPUT(antes de reverter):", input_tape)
    print("FITA DE HISTORICO(para revercao)", history_tape)

    reversibleTuringMachine.reverse_movement(history_tape, head_marker, input_tape)

    print("FITA DE INPUT REVERTIDA:", input_tape)
    print("FITA DE OUTPUT", output_tape)
    print("FITA DE HISTORICO FINAL", history_tape)