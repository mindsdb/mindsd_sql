from mindsdb_sql.parser.ast.base import ASTNode
from mindsdb_sql.parser.utils import indent


class NativeQuery(ASTNode):
    """
        Not parsed query to integration
    """

    def __init__(self, integration, query: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.integration = integration
        self.query = query

    def to_tree(self, *args, level=0, **kwargs):
        return indent(level) + \
               f'NativeQuery(integration={self.integration.to_string()}, query="{self.query}")'

    def get_string(self, *args, **kwargs):
        return f'{self.integration.to_string()} ({self.query})'


class StrQuery(ASTNode):
    def __init__(self, query: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query = query

    def to_tree(self, *args, level=0, **kwargs):
        return indent(level) + \
               f'StrQuery(query="{self.query}")'

    def get_string(self, *args, **kwargs):
        return f'({self.query})'

    def to_string(self, alias=True):
        s = self.get_string()
        if self.alias is not None:
            s = f'{s} as {self.alias.parts[0]}'
        return s
