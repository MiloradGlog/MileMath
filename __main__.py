from ExpressionInterpreter.interpreter.lexer import Lexer
from ExpressionInterpreter.interpreter.parser import Parser
from ExpressionInterpreter.interpreter.interpreter import Interpreter
from ExpressionInterpreter.interpreter.trie import Trie

def main():
    while True:
        try:
            text = input('milemath>>>> ')
        except (EOFError, KeyboardInterrupt):
            break
        if not text:
            continue

        root = Trie("ROOT", "ROOT")
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser, root)
        result = interpreter.interpret()

        print("%.2f" % result)


if __name__ == '__main__':
    main()
