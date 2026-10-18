import math
import re
from colorama import Fore, Style, init

# Initialize colorama for terminal formatting
init(autoreset=True)

class AIMathEngine:
    def __init__(self):
        # Safe math namespace whitelist
        self.safe_dict = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "pow": pow
        }

    def evaluate_expression(self, expr):
        """Safely evaluates a mathematical expression string."""
        # Clean the expression
        expr = expr.strip()
        
        # Check for disallowed dangerous characters
        if re.search(r'[^0-9\+\-\*\/\.\(\)\s\w]', expr):
            raise ValueError("Invalid characters detected in expression.")

        try:
            # Evaluate within the safe namespace
            result = eval(expr, {"__builtins__": {}}, self.safe_dict)
            return result
        except Exception as e:
            raise ValueError(f"Calculation Error: {e}")

    def analyze_expression(self, expr, result):
        """Provides AI-inspired heuristic feedback and classification on the math input."""
        insights = []
        
        if "sin" in expr or "cos" in expr or "tan" in expr:
            category = "Trigonometric Function"
            insights.append("Involves periodic angular calculations.")
        elif "sqrt" in expr or "**" in expr or "^" in expr:
            category = "Exponential / Radical Expression"
            insights.append("Involves non-linear growth or root calculations.")
        elif any(op in expr for op in ['+', '-', '*', '/']):
            category = "Arithmetic Expression"
            insights.append("Standard linear or multi-operation calculation.")
        else:
            category = "Numeric Evaluation"

        # Complexity check based on length/operators
        op_count = sum(expr.count(op) for op in ['+', '-', '*', '/', '**', 'sqrt'])
        if op_count > 4:
            complexity = f"{Fore.YELLOW}Moderate-High Complexity{Style.RESET_ALL}"
        else:
            complexity = f"{Fore.GREEN}Simple / Direct{Style.RESET_ALL}"

        return category, complexity, insights

def main():
    engine = AIMathEngine()
    
    print("=" * 60)
    print(f"{Fore.CYAN}AI SMART MATH & EXPRESSION SOLVER{Style.RESET_ALL}")
    print("=" * 60)
    print("Examples: 45 * 2 + 10, sqrt(144) + 5, sin(pi/2)")
    
    expr = input(f"\n{Fore.GREEN}Enter math expression: {Style.RESET_ALL}")

    try:
        result = engine.evaluate_expression(expr)
        category, complexity, insights = engine.analyze_expression(expr, result)

        print("\n" + "-" * 60)
        print(f"Expression        : {expr}")
        print(f"Computed Result   : {Fore.WHITE}{Style.BRIGHT}{result}{Style.RESET_ALL}")
        print(f"Classification    : {category}")
        print(f"Complexity Rating : {complexity}")
        print(f"AI Insights       : {', '.join(insights)}")
        print("-" * 60 + "\n")

    except Exception as e:
        print(f"\n{Fore.RED}Error: {e}{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
