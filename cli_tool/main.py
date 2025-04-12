# main.py
import argparse
from bug_fix import fix_bugs
from refactor import refactor_code
from explain import generate_explanation

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Code Assistant (Bug Fix & Refactor Tool)")
    parser.add_argument('-f', '--file', help="Path to code file", type=str)
    parser.add_argument('-a', '--action', help="Action: bug_fix or refactor", choices=['bug_fix', 'refactor'], required=True)
    parser.add_argument('-l', '--lang', help="Programming Language (e.g., Python, Java, C++)", required=True)

    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r') as file:
                code = file.read()
        except FileNotFoundError:
            print("❌ Error: File not found.")
            return
    else:
        print("🔹 Enter your code (finish with an empty line):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        code = '\n'.join(lines)

    # Action
    if args.action == 'bug_fix':
        modified_code, raw_explanation = fix_bugs(code, args.lang)
    else:
        modified_code, raw_explanation = refactor_code(code, args.lang)

    # Generate enhanced explanation
    explanation = generate_explanation(code, modified_code, args.action, args.lang)

    # Output Results
    print("\n================= 🔍 ORIGINAL CODE =================\n")
    print(code)

    print("\n================= ✅ MODIFIED CODE =================\n")
    print(modified_code)

    print("\n================= 🧠 EXPLANATION ===================\n")
    print(explanation)

if __name__ == '__main__':
    main()
