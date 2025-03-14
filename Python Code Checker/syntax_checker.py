import ast
from flake8.api import legacy as flake8  # Import flake8 API
#Function to check syntax

class CodeAnalyzer(ast.NodeVisitor): #NodeVisitor works by calling functions like "visit_Call", "visit_Assign".
    #So methods should be named "visit_Call" or "visit_Assign" for NodeVisitor to work.
        def __init__(self):
            self.issues = []
            self.imports = set()
            self.used_names = set()
            self.wildcards = []

        def visit_Import(self, node):
            for alias in node.names:
                self.imports.add(alias.name)
            self.generic_visit(node)

        def visit_ImportFrom(self, node):
            """Handles 'from module import X' statements"""
            if len(node.names) == 1 and node.names[0].name == '*':
                self.wildcards.append(node.module)
            else:
                for alias in node.names:
                    self.imports.add(alias.name)
            self.generic_visit(node)

        
        def visit_Name(self, node):
            self.used_names.add(node.id)
            self.generic_visit(node)

        def check_unused_imports(self):
            unused = self.imports - self.used_names  # Find unused imports using difference in sets.
            for imp in unused:
                self.issues.append(f"Warning: Unused import '{imp}'")
            if self.wildcards:
                for mod in self.wildcards:
                    self.issues.append(f"Warning: Wildcard import used from '{mod}'")

        def visit_Call(self, node): #To work with NodeVisitor
            if isinstance(node.func, ast.Name) and node.func.id in ('eval', 'exec'):
                self.issues.append(f"Warning: Use of {node.func.id}() in line {node.lineno}")
            self.generic_visit(node) # Continue visiting other nodes

        def run_flake8_check(self, code):
        # Runs flake8 checks on the given code
            style_guide = flake8.get_style_guide(ignore=["E501"])  # Ignore long line warnings
            report = style_guide.input_file(file_path)

        # Capture flake8 errors
            for line in report.get_statistics("E"):  # Get error statistics
                self.issues.append(f"Flake8: {line}")



def syntax_checker(code):
    try:

        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        tree = ast.parse(code)
        print("No syntax errors found")

        analyze = CodeAnalyzer()
        analyze.visit(tree)
        analyze.check_unused_imports()
        analyze.run_flake8_check(file_path)

        for issue in analyze.issues:
            print(issue)

    except SyntaxError as e:
        print(f"Syntax Error: {e.msg} at line {e.lineno}, column {e.offset}")

if __name__ == "__main__":

    file_path = "code.txt"
    syntax_checker(file_path)
    