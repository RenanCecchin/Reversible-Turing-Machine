class Transition:
    def __init__(self, current_state, read_symbol, next_state, write_symbol, head_movement):
        self.current_state = current_state      #Estado atual
        self.read_symbol = read_symbol          #Simbolo atual da fita
        self.next_state = next_state            #Estado pos transicao
        self.write_symbol = write_symbol        #Escrita da fita
        self.head_movement = head_movement      #L ou R