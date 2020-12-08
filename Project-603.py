from token1 import Token
from lexer import Lexer
from interpreter import Interpreter

def main():
    while True:
        try:
            # To run under Python3 replace 'input' call
            # with 'input'
            text = input('calculator> ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()