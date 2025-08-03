class Solution(object):
    def interpret(self, command):
        word=""
        i=0
        while i<len(command):
            if command[i]=="G":
                word+="G"
                i+=1
            elif command[i:i+2]=="()":
                word+="o"
                i+=2
            elif command[i:i+4]=="(al)":
                word+="al"
                i+=4
        return word

        