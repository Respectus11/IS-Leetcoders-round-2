def goalPars(command):
    return command.replace("()", "o").replace("(al)", "al")
print(goalPars("G()"))