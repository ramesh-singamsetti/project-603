from token1 import Token
import sys
import math

INTEGER, PLUS, MINUS, MUL, DIV, MOD, FD, SQUR, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'MOD', 'FD', 'SQUR', 'EOF'
)

class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')
        sys.exit()

    def eat(self, token_type):
        """compare the current token type with the passed token type and if they match then "eat" the current token
        and assign the next token to the self.current_token, otherwise raise an exception."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()

        else:
            self.error()

    def factor(self):
        """factor : INTEGER"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        result = self.factor()

        while self.current_token.type in (MUL, DIV, MOD, FD, SQUR):
            token = self.current_token

            if token.type == SQUR:
                value = result
                self.eat(SQUR)
                i = 1
                if self.current_token.value > 0:
                    while i < int(self.current_token.value):
                        result *= value
                        i += 1
                else:
                    result = 1
            elif token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()
            elif token.type == FD:
                self.eat(FD)
                result = math.floor(result / self.factor())
            elif token.type == MOD:
                self.eat(MOD)
                last_num = self.current_token 
                division = math.floor(result / self.factor())
                product_div = division * last_num.value
                result = result - product_div

        return result

    def expr(self):
        """Arithmetic expression parser / interpreter.
        calc>  14 + 2 * 5 - 6 / 3 = 22
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER
        """
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        return result