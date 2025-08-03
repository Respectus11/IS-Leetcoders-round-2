class Solution:
    def interpret(self, command: str) -> str:
        BE = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                BE += 'G'
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                BE += 'o'
                i += 2
            elif command[i] == '(' and command[i+1:i+4] == 'al':
                BE += 'al'
                i += 4
        return BE
