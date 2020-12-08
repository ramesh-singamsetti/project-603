from token import ENDMARKER
from token1 import Token
import sys

INTEGER, PLUS, MINUS, MUL, DIV, PER, FD, SQUR, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'PER', 'FD', 'SQUR', 'EOF'
)


class Lexer(object):
    def __init__(self, text):
        # string input, e.g. "21 * 9", "24 / 4 * 4"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception ('Invalidcharacter')
        

    def next_next(self):
        """Next advances the `pos` pointer and set the `current_char` variable."""
        result = ''
        while self.current_char is not None and self.current_char == "/" or self.current_char is not None and self.current_char == "*":
            result += self.current_char
            self.next()
        return str(result)

    def next(self):
        """Next advances the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip(self):
        while self.current_char is not None and self.current_char.isspace():
            self.next()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.next()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer also known as scanner
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.next()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.next()
                return Token(MINUS, '-')

            if self.current_char == '*':
                if self.next_next() == "**":
                    return Token(SQUR, '**')
                else:
                    self.pos -= 1
                    self.next()
                    return Token(MUL, '*')

            if self.current_char == '/': 
                if self.next_next() == "//":
                    return Token(FD, '//')
                else:
                    self.pos -= 1
                    self.next()
                    return Token(DIV, '/')

            if self.current_char == '%':
                self.next()
                return Token(PER, '%')

            self.error()
            sys.exit()
    
        return Token(EOF, None)