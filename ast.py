

class Lexeme:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return self.get_value()


class NumberLexeme(Lexeme):
    pass


class FloatLexeme(Lexeme):
    pass


class OperatorLexeme(Lexeme):
    pass


class EqualLexeme(Lexeme):
    pass


class OpenBracketLexeme(Lexeme):
    pass


class CloseBracketLexeme(Lexeme):
    pass


class IdentifierLexeme(Lexeme):
    pass


class Node:
    pass


class NumberNode(Node):
    pass


class FloatNode(Node):
    pass


class ExprNode(Node):
    pass
