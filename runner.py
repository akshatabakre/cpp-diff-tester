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

        if p.returncode != 0:
            return "CRASH", False

        return p.stdout.strip(), False

    except subprocess.TimeoutExpired:
        return "TIMEOUT", True

subprocess.run(["g++", "brute.cpp", "-o", "brute"])
subprocess.run(["g++", "optimal.cpp", "-o", "optimal"])
subprocess.run(["g++", "generator.cpp", "-o", "gen"])

for i in range(1000):
    input_data, _ = run(["./gen"], "", 1)

    out1, _ = run(["./brute"], input_data, 1)
    out2, _ = run(["./optimal"], input_data, 1)

    if out1 == "CRASH" or out2 == "CRASH":
        print("Crash detected!")
        print("Failing test case saved.")

        with open("testcases/crash.txt", "w") as f:
            f.write(input_data)
        break

    if out1 == "TIMEOUT" or out2 == "TIMEOUT":
        print("Timeout detected!")
        print("Failing test case saved.")

        with open("testcases/timeout.txt", "w") as f:
            f.write(input_data)
        break

    if out1 != out2:
        print("Wrong answer detected!")
        print("Failing test case saved.")

        with open("testcases/wrong_answer.txt", "w") as f:
            f.write(input_data)
        break

else:
    print("All tests passed")
