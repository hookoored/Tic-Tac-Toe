############################################
#
# LLL  L  LLL       LLL  LLL  LLL      LLL  LLL  LLL
#  L   L  L    LLL   L   LLL  L    LLL  L   L L  LLL
#  L   L  LLL        L   L L  LLL       L   LLL  LLL
#
#############################################
memory = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
turn = 'O'
def show_memory ():
    '''
    Prints memory
    '''
    row = ['','','']
    for item in range (3):
        for number in range (3):
            row[item] = str (row[item]) + str (memory[item][number]) + ' '#Make the rows
            
    for item in range (3):
        print str (item + 1) + ' ' + str (row[item])#Display the rows
    
    
def get_turn ():
    '''
    Gets the move of whoever's turn it is
    '''
    get_input = raw_input ('Your Turn:')
    retval = []
    for letter in get_input:
        if letter == '1' or letter == '2' or letter == '3':
             retval.append (int (letter) - 1)
    #if get_turn = settings:
        
    return retval
            
def win_game ():
    '''
    Checks to see if the move is a winning move
    '''
    for item in range(3):
        if memory[item][0] == memory[item][1] == memory[item][2] and memory[item][0] != '-':#Checks horizontal wins
            print memory[item][0] + " WINS"
        if memory[0][item] == memory[1][item] == memory[2][item]and memory[0][item] != '-':#Checks vertical wins
            print memory[0][item] + " WINS"
        
    if memory[0][2] == memory [1][1] == memory[2][0] and memory [1][1] != '-':#Checks bottom-left to top-right diagnol
        print memory[0][2] + ' WINS!'
    if memory[0][0] == memory[1][1] == memory[2][2] and memory [1][1] != '-':#Checks top-left to bottom-right diagnol
        print memory[0][0] + ' WINS!'
        
        
number_of_turns = range(9)
for number in number_of_turns:
    print turn + ' 1 2 3'
    show_memory()
    current_turn = get_turn()
    if memory[current_turn[1]][current_turn[0]] == '-':
        memory[current_turn[1]][current_turn[0]] = turn
    else:
        print 'Oops, you tried to overwrite something!  The punishment is that your turn is skipped!'
        number_of_turns.append('')
    #Switch turns
    if turn == 'O':
        turn = 'X'
    elif turn == 'X':
        turn = 'O'
    win_game()
