import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    print("ERROR: OPENAI_API_KEY not found")
    exit(1)

client = OpenAI(api_key=api_key)


def generate_brute(problem_text):
    prompt = f"""
You are generating a BRUTE FORCE solution in C++.

Rules:
- Code must be correct, not optimized
- Use simple loops
- Handle multiple test cases
- No recursion
- No advanced STL tricks
- Read input from stdin
- Write output to stdout
- Output ONLY valid C++ code
- Do NOT explain anything

Problem:
{problem_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def main():
    with open("problem.txt", "r") as f:
        problem_text = f.read()

    code = generate_brute(problem_text)

    with open("brute.cpp", "w") as f:
        f.write(code)

    print("brute.cpp generated successfully")


if __name__ == "__main__":
    main()
