from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.interpreter import Interpreter
from interpreter.interpreter import NUMBER
from interpreter.trie import Trie

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main():
    root = Trie("ROOT", "ROOT")
    while True:
        try:
            text = input('\033[1mmilemath: \033[0m')
        except (EOFError, KeyboardInterrupt):
            break
        if not text:
            continue
        elif text == "EXIT":
            print("ALOO")
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser, root)
        result = interpreter.interpret()


        if result in (True, False):
            print (result)
        elif result == NUMBER:
            pass
        elif float(result).is_integer():
            print("%.0f" % result)
        else:
            print("%.3f" % result)


if __name__ == '__main__':
    main()
