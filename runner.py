import subprocess

def test_input(input_data):
    out1, _ = run(["./brute"], input_data, 1)
    out2, _ = run(["./optimal"], input_data, 1)

    if out1 == "CRASH" or out2 == "CRASH":
        return True
    if out1 == "TIMEOUT" or out2 == "TIMEOUT":
        return True
    if out1 != out2:
        return True
    return False

def reduce_testcase(input_data):
    lines = input_data.strip().split("\n")

    T = int(lines[0])
    blocks = []
    idx = 1

    for _ in range(T):
        n = int(lines[idx])
        arr = lines[idx + 1]
        blocks.append((n, arr))
        idx += 2

    # Stage 1: Try reducing number of test cases
    for i in range(len(blocks)):
        new_blocks = blocks[:i] + blocks[i+1:]
        if not new_blocks:
            continue

        new_input = str(len(new_blocks)) + "\n"
        for n, arr in new_blocks:
            new_input += str(n) + "\n"
            new_input += arr + "\n"

        if test_input(new_input):
            return reduce_testcase(new_input)

    # Stage 2: Try reducing array sizes
    for i in range(len(blocks)):
        n, arr = blocks[i]
        arr_list = list(map(int, arr.split()))

        for j in range(len(arr_list)):
            new_arr = arr_list[:j] + arr_list[j+1:]
            if not new_arr:
                continue

            new_blocks = blocks.copy()
            new_blocks[i] = (len(new_arr), " ".join(map(str, new_arr)))

            new_input = str(len(new_blocks)) + "\n"
            for nn, aa in new_blocks:
                new_input += str(nn) + "\n"
                new_input += aa + "\n"

            if test_input(new_input):
                return reduce_testcase(new_input)

    return input_data

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
        print("Reducing test case...")

        minimized = reduce_testcase(input_data)

        with open("testcases/crash.txt", "w") as f:
            f.write(minimized)

        print("Minimal failing test case saved.")
        break


    if out1 == "TIMEOUT" or out2 == "TIMEOUT":
        print("Timeout detected!")
        print("Reducing test case...")

        minimized = reduce_testcase(input_data)

        with open("testcases/timeout.txt", "w") as f:
            f.write(minimized)

        print("Minimal failing test case saved.")
        break


    if out1 != out2:
        print("Wrong answer detected!")
        print("Reducing test case...")

        minimized = reduce_testcase(input_data)

        with open("testcases/wrong_answer.txt", "w") as f:
            f.write(minimized)

        print("Minimal failing test case saved.")
        break

else:
    print("All tests passed")
