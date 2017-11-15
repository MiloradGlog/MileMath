# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF, LOG, POW, SQRT, SIN, COS, TAN, CTG, \
MORE, LESS, EQUALS, MOREEQL, LESSEQL, ASSIGN, VARIABLE = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF', 'LOG', 'POW', 'SQRT', 'SIN', 'COS', 'TAN', 'CTG',
    'MORE', 'LESS', 'EQUALS', 'MOREEQL', 'LESSEQL', 'ASSIGN', 'VARIABLE'
)


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]



    def isOperation(self, word):
        if (        word == LOG or
                    word == POW or
                    word == SQRT or
                    word == SIN or
                    word == COS or
                    word == TAN or
                    word == CTG):
            return True
        else:
            return False


    def getOperation(self, word):
        if (word == "LOG"):
            return LOG
        if (word == "POW"):
            return POW
        if (word == "SQRT"):
            return SQRT
        if (word == "SIN"):
            return SIN
        if (word == "COS"):
            return COS
        if (word == "TAN"):
            return TAN
        if (word == "CTG"):
            return CTG


    def word(self):
        result = ""
        if (self.current_char is not None and self.current_char.isalpha()):
            result += self.current_char
            self.advance()
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char.isalpha()):
            result += self.current_char
            self.advance()
        return str(result)

    def nextIsEquals(self):
        if self.current_char == '=':
            self.advance()
            return True
        else:
            return False


    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char.isalpha():
                word = self.word()
                if (self.isOperation(word)):
                    print("Ulazim u isoperation if")
                    return Token(self.getOperation(word), 0)

                return Token(VARIABLE, word)


            if self.current_char == '<':
                self.advance()
                if self.nextIsEquals():
                    return Token(LESSEQL, '<=')
                return Token(LESS, '<')
            if self.current_char == '>':
                self.advance()
                if self.nextIsEquals():
                    return Token(MOREEQL, '>=')
                return Token(MORE, '>')
            if self.current_char == '=':
                self.advance()
                if self.nextIsEquals():
                    return Token(EQUALS, '==')
                return Token(ASSIGN, '=')

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)