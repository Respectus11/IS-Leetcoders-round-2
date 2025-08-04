def interpret(self, command):
    result=""
    s=0
    while s<len(command):
        if command[s]=='G':
            result+="G"
            s+=1
        elif command[s:s+2]=="()":
            result+="o"
            s+=2
        elif command [s:s+4]=='(al)':
            result+="al"
            s+=4
    return result
