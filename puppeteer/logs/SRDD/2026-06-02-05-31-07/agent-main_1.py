import ast
import json
import sys
import argparse

class CodeQualityValidator:
    def __init__(self, code):
        self.code = code

    def analyze_code(self):
        try:
            tree = ast.parse(self.code)
            issues = self.check_code_smells(tree)
            issues.extend(self.check_unused_variables(tree))
            issues.extend(self.check_long_method_bodies(tree))
            issues.extend(self.check_complex_conditions(tree))
            issues.extend(self.check_large_functions(tree))
            return json.dumps(issues)
        except SyntaxError as e:
            return json.dumps({"error": str(e)})

    def check_code_smells(self, tree):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 10:
                    issues.append({"type": "long method body", "line": node.lineno, "column": node.col_offset, "message": "Method body is too long"})
                if len(node.args.args) > 5:
                    issues.append({"type": "too many arguments", "line": node.lineno, "column": node.col_offset, "message": "Function has too many arguments"})
            elif isinstance(node, ast.ClassDef):
                if len(node.body) > 5:
                    issues.append({"type": "long class body", "line": node.lineno, "column": node.col_offset, "message": "Class body is too long"})
        return issues

    def check_unused_variables(self, tree):
        issues = []
        used_variables = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                used_variables.add(node.id)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                if node.targets[0].id not in used_variables:
                    issues.append({"type": "unused variable", "line": node.lineno, "column": node.col_offset, "message": "Variable is not used"})
        return issues

    def check_long_method_bodies(self, tree):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 10:
                    issues.append({"type": "long method body", "line": node.lineno, "column": node.col_offset, "message": "Method body is too long"})
        return issues

    def check_complex_conditions(self, tree):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                if len(node.body) > 5:
                    issues.append({"type": "complex condition", "line": node.lineno, "column": node.col_offset, "message": "Condition is too complex"})
        return issues

    def check_large_functions(self, tree):
        issues = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 20:
                    issues.append({"type": "large function", "line": node.lineno, "column": node.col_offset, "message": "Function is too large"})
        return issues

def main():
    parser = argparse.ArgumentParser(description='Code Quality Validator')
    parser.add_argument('code', type=str, help='Input code')
    parser.add_argument('-o', '--output', type=str, default='json', help='Output format (json or text)')
    args = parser.parse_args()
    code = args.code
    validator = CodeQualityValidator(code)
    issues = validator.analyze_code()
    if args.output == 'json':
        print(issues)
    elif args.output == 'text':
        print(json.loads(issues))
    else:
        print("Invalid output format")

if __name__ == "__main__":
    main()