# C++ Differential Testing & Testcase Minimization Tool

## 📌 Overview

This project is an automated differential testing framework for debugging C++ solutions.

It compares a brute-force implementation with an optimized implementation using automatically generated test cases.  
The system detects:

- ❌ Wrong Answers  
- ⏱ Timeouts (infinite loops / slow code)  
- 💥 Crashes (segmentation faults / runtime errors)  

Additionally, when a failure is detected, the tool automatically minimizes the failing input to produce the smallest reproducible test case.

---

## 🎯 Motivation

While solving competitive programming problems, identifying the exact test case where an optimized solution fails can be difficult.

This project automates that process by:

1. Generating valid test cases based on constraints  
2. Running both brute and optimized solutions  
3. Comparing outputs  
4. Classifying failure types  
5. Shrinking failing inputs for easier debugging  

This mirrors real-world testing techniques such as differential testing and fuzzing.

---

## ⚙️ Features Implemented

### 1️⃣ Differential Testing Engine
- Compiles `brute.cpp` and `optimal.cpp`
- Runs both on identical generated inputs
- Detects output mismatches automatically

---

### 2️⃣ Constraint-Based Test Case Generator
Test cases are generated using configurable constraints defined in `constraints.txt`.

Example:

T 1 5
n 1 10
array n -10 10


This ensures:
- Inputs follow valid format
- Constraints can be modified without changing source code

---

### 3️⃣ Multiple Test Case Support

Supports input format:

T
n
array
n
array
...


---

### 4️⃣ Edge Case Biasing

The generator intentionally produces:
- Minimum size inputs
- Maximum size inputs
- All zeros
- All minimum values
- All maximum values

This increases bug detection probability.

---

### 5️⃣ Timeout Detection

- Execution time is limited per run
- Infinite loops and inefficient algorithms are detected
- Failing test case is saved automatically

---

### 6️⃣ Crash Detection

- Detects abnormal termination (segfaults, runtime errors)
- Uses process return codes to classify crashes
- Saves the crashing input for reproduction

---

### 7️⃣ Automatic Minimal Failing Testcase Reduction

When a failure is detected:

- The tool recursively reduces:
  - Number of test cases
  - Array size
- Ensures the failure still persists
- Produces the smallest reproducible failing input

This significantly improves debugging efficiency.

---

## 🧠 Architecture

The system follows a structured differential testing pipeline:

1. `constraints.txt` defines input rules  
2. `generator.cpp` produces valid random inputs  
3. `brute.cpp` and `optimal.cpp` are compiled  
4. Both programs are executed on the same input  
5. Outputs are compared  
6. Failures are classified (Wrong Answer / Crash / Timeout)  
7. The failing input is minimized  
8. Final minimized testcase is saved to `testcases/`


---

## 📂 Project Structure

```text
cpp-diff-tester/
├── brute.cpp        # Correct but slow implementation
├── optimal.cpp      # Optimized implementation under test
├── generator.cpp    # Constraint-driven input generator
├── runner.py        # Handles compilation, execution & comparison
├── constraints.txt  # Input configuration
├── testcases/       # Stores minimized failing inputs
└── README.md
```


---

## 🛠 Technologies Used

- C++
- Python
- Git
- Subprocess-based execution

No external APIs required in the current version.

---

## 🚀 How to Run

1. Ensure you have:
   - `g++` installed
   - Python installed

2. Configure constraints in:
constraints.txt


3. Run:
python runner.py


4. If a failure is detected:
- The minimal failing test case will be saved in the `testcases/` directory.

---

## 📈 Future Improvements

- Value-level testcase reduction
- Support for more input structures (graphs, trees)
- Web-based interface
- AI-assisted brute-force generation
- Docker-based sandboxing

---

## 🧪 Testing Philosophy

This project applies principles of:

- Differential testing  
- Fuzz testing  
- Edge-case biasing  
- Failure classification  
- Automated testcase shrinking  

---

## 👩‍💻 Author

Built as part of independent system design and testing practice.