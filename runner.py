import subprocess

def run(cmd, input_data):
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(input_data)
    return out.strip()

subprocess.run(["g++", "brute.cpp", "-o", "brute"])
subprocess.run(["g++", "optimal.cpp", "-o", "optimal"])
subprocess.run(["g++", "generator.cpp", "-o", "gen"])

for i in range(1000):
    input_data = run(["./gen"], "")
    out1 = run(["./brute"], input_data)
    out2 = run(["./optimal"], input_data)

    if out1 != out2:
        print("Mismatch found!")
        print("Input:")
        print(input_data)
        print("Brute:", out1)
        print("Optimal:", out2)

        with open("testcases/failing.txt", "w") as f:
            f.write(input_data)
        break
else:
    print("All tests passed")
