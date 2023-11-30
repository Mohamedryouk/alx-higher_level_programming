#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arguments = dir(hidden_4)
    for argument in arguments:
        if argument[:2] != "__":
            print(argument)
