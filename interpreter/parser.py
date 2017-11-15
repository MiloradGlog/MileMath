from .lexer import *
import math


###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################

class AST(object):
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class LogOP(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class VarOP(AST):
    def __init__(self, var, assign, right):
        self.var = var
        self.assign = assign
        self.right = right

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class MathOP(AST):
    def __init__(self, op, right):
        self.op = op
        self.right = right


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : INTEGER | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        elif token.type == VARIABLE:
            var = token.value
            self.eat(VARIABLE)
            token = self.current_token
            if (token.type == ASSIGN):
                self.eat(ASSIGN)
                print(token)
                return VarOP(var=var, assign=True, right=self.expr())
            else:
                return VarOP(var=var, assign=False, right=0)

    def operation(self):
        node = self.factor()

        token = self.current_token



        if token.type == LOG:
            self.eat(LOG)
            node = MathOP(op=token, right=self.factor())
        elif token.type == POW:
            self.eat(POW)
            node = MathOP(op=token, right=self.factor())
        elif token.type == SQRT:
            self.eat(SQRT)
            node = MathOP(op=token, right=self.factor())
        elif token.type == SIN:
            self.eat(SIN)
            node = MathOP(op=token, right=self.factor())
        elif token.type == COS:
            self.eat(COS)
            node = MathOP(op=token, right=self.factor())
        elif token.type == TAN:
            self.eat(TAN)
            node = MathOP(op=token, right=self.factor())
        elif token.type == CTG:
            self.eat(CTG)
            node = MathOP(op=token, right=self.factor())


        if (token.type == MORE):
            self.eat(MORE)
            node = LogOP(left=node, op=token, right=self.factor())
        elif (token.type == MOREEQL):
            self.eat(MOREEQL)
            node = LogOP(left=node, op=token, right=self.factor())
        elif (token.type == LESS):
            self.eat(LESS)
            node = LogOP(left=node, op=token, right=self.factor())
        elif (token.type == LESSEQL):
            self.eat(LESSEQL)
            node = LogOP(left=node, op=token, right=self.factor())
        elif (token.type == EQUALS):
            self.eat(EQUALS)
            node = LogOP(left=node, op=token, right=self.factor())

        elif (token.type == ASSIGN):
            self.eat(ASSIGN)
            # node = VarOP(left=node, op=token, right=self.factor())


        return node


    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.operation()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinOp(left=node, op=token, right=self.operation())

        return node

    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        node = self.expr()
        if self.current_token.type != EOF:
            self.error()
        return node

