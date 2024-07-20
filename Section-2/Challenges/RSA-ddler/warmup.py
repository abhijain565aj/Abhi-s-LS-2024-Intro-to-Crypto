def run_brainfuck(code):
    tape = [0] * 30000
    pointer = 0
    code_pointer = 0
    brackets = []
    output = []

    while code_pointer < len(code):
        command = code[code_pointer]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            tape[pointer] = (tape[pointer] + 1) % 256
        elif command == '-':
            tape[pointer] = (tape[pointer] - 1) % 256
        elif command == '.':
            output.append(chr(tape[pointer]))
        elif command == ',':
            # This implementation does not handle input (',')
            pass
        elif command == '[':
            if tape[pointer] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        open_brackets += 1
                    elif code[code_pointer] == ']':
                        open_brackets -= 1
            else:
                brackets.append(code_pointer)
        elif command == ']':
            if tape[pointer] != 0:
                code_pointer = brackets[-1]
            else:
                brackets.pop()

        code_pointer += 1

    return ''.join(output)

# Your Brainfuck code
brainfuck_code = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++..----.-.++++++.+++++++++++.-------------------.+++.+++++.>----------.<-----.>----.<-.>---.<-------------------.>--------.-..++.-------.<.>++++++++++++++++.+++++.-------.---------.<+++.>-----.++++++++++++++++..--.<---.>+++.---------------.+++.+.+++++++++++.-----------------.++++++++++++++++.<.>----------.+.--.------.+++++++++++++++++.----------.+++++++++++.-----------.++++++++++.------------.+++++.----------.+.++++++++++++++.-----.---.++.----.+++++++++++++.<++++++++++++++++++.>.<+++++++++.++++.<++++++++++++++++++++.>-----.--..++++.---------.++++.>.<++.+.-.>++++.<-----.>----.<+++++.>---.<.++++.-----.>-.<+.>++++.<.>--.-.<+.--.>+++.<----.>.<+++++++.>---.<<.>>++++.<---.>-.<-.>--.<----.>.-.<++++++.--.>+++++++.<-.---.++++++.>-------.<<.>>++++.<-.++++.-------.--.>.-----.<++++++.<.>--.>++++++++.<-------.>----.<+++++.>-.<<.>++++.--.<+++.>---.-.>++.-.---.<-.+++++++.>+++++++.<-.>-----.++.----.+++++++.----.<-.>++++.<+++.-------.++.>----.<<---.>>--.<++.<+++.>----.>+.<++++++++.>--..+++.<--.>.<---.---.>---.---.<++++.<++++++++."

# Decode the Brainfuck code
output = run_brainfuck(brainfuck_code)
print(output)
