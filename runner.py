import subprocess

def run(cmd, input_data, timeout=1):
    try:
        p = subprocess.run(
            cmd,
            input=input_data,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        return p.stdout.strip(), False
    except subprocess.TimeoutExpired:
        return "TIMEOUT", True

subprocess.run(["g++", "brute.cpp", "-o", "brute"])
subprocess.run(["g++", "optimal.cpp", "-o", "optimal"])
subprocess.run(["g++", "generator.cpp", "-o", "gen"])

for i in range(1000):
    input_data, _ = run(["./gen"], "", 1)

    out1, t1 = run(["./brute"], input_data, 1)
    out2, t2 = run(["./optimal"], input_data, 1)

    if t1 or t2:
        print("Timeout detected!")
        print("Input:")
        print(input_data)
        break

    if out1 != out2:
        print("Mismatch found!")
        print("Input:")
        print(input_data)
        print("Brute:", out1)
        print("Optimal:", out2)
        break
else:
    print("All tests passed")
