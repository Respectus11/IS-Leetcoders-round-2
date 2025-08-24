class Solution:
    def interpret(self, command: str) -> str:
      BE=""
     for i in len(command):
         if i =='G':
            BE.append(i)
         elif i=='(' and i+1==')':
            BE.append('o')
         else i=='(' and i+1=='a' and i+2=='l' and i+3==')':
             BE.append('al')
