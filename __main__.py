from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.trie import Trie



def main():
    root = Trie("ROOT", "ROOT")
    while True:
        try:
            text = input('milemath>>>> ')
        except (EOFError, KeyboardInterrupt):
            break
        if not text:
            continue
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser, root)
        result = interpreter.interpret()

        if result in (True, False):
            print (result)

        elif float(result).is_integer():
            print("%.0f" % result)
        else:
            print("%.3f" % result)


if __name__ == '__main__':
    main()
