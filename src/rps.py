def rps(number) -> str:
    if number not in range(0, 3):
        raise ValueError
    else:
        if number == 0:
            output = "rock"
        elif number == 1:
            output = "paper"
        else:
            output = "scissors"
        return output
