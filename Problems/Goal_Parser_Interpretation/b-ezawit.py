class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        result = ""
        length = len(command)
        for i in range(0,length):
            if command[i] == "G":
                result += "G"
            elif command[i] =="(" and command[i+1]==")":
                result += "o"
            elif command[i] == "(" and command[i+1]=="a" and command[i+2]=="l" and command[i+3]==")":
                result += "al"
        
        return result

#Example:
sol = Solution()
print(sol.interpret("G()(al)")) #Goal


        