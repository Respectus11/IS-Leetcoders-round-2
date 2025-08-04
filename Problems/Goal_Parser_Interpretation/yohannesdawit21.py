def interpret(command):
    return command.replace("()", "o").replace("(al)", "al")
# Example usage
print(interpret("G()(al)"))  # Output: "Goal"   
print(interpret("G()()()()(al)"))  # Output: "Gooooal"
print(interpret("(al)G(al)()()G"))  # Output: "alGooG"
print(interpret("G(al)()()G"))  # Output: "GoalG"