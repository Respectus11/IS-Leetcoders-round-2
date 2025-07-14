def goal_parser(command):
    output = command.replace("()", "o")
    return output.replace("(al)", "al")
