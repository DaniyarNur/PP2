def interpret(command):
    return command.replace('()', 'o').replace('(al)', 'al')
    
print(interpret('G()()()()(al)'))