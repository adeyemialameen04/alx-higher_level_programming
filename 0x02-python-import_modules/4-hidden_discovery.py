#!/usr/bin/python3

if __name__ == "__main__":
    import dis

    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
        dis.disassemble(code)
