# Mission 4 — How Programs Run

## 1. Mission Title

Mission 4 — How Programs Run

## 2. Task / Objective

The objective of this mission was to understand how computers execute programs, create and run a simple Python program, and compare compilers with interpreters.

The mission focused on:
- Creating a Python file named `hello.py`.
- Running the program using Python 3 from Terminal.
- Understanding how source code is executed.
- Comparing compilers and interpreters.

## 3. Work Completed

### Task 4.1 — Create and Run a Python Program

I created a Python file named `hello.py` inside the Mission 4 folder.


### Task 4.2 — Compare Compiler and Interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates source code before execution. | Executes instructions during runtime. |
| Typical output | Often produces object code or an executable program. | Commonly executes instructions without producing a separate executable file. |
| One example | C compiler (GCC). | Python interpreter (CPython). |
| One advantage | Compiled programs can execute efficiently. | Makes testing and running code convenient. |

### Difference Between a Compiler and an Interpreter

A compiler translates source code into another form, often machine code, before the program is executed. An interpreter executes program instructions during runtime. Compiled programs commonly produce a separate executable or object-code output, whereas an interpreter commonly runs instructions through its runtime environment. In practice, some programming languages use a combination of compilation and interpretation.

## 4. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `python3` | Runs Python 3 programs. |
| `python3 hello.py` | Executes the `hello.py` file. |
| `print()` | Displays text or other values in Python. |
| Terminal | Used to execute the Python program. |
| Visual Studio Code | Used to create and edit the Python file. |

## 5. My Understanding

Through this mission, I understood that a program is a set of instructions written in a programming language.

Python source code is executed using a Python interpreter. When I run `python3 hello.py`, the Python runtime processes the instructions and displays the output.

I also learned that compilers and interpreters are two approaches to translating and executing programs. A compiler generally translates code before execution, while an interpreter carries out instructions during runtime.

I understood that the distinction is a simplified model because modern language implementations can combine both approaches.

## 6. Difficulties Faced

Understanding the difference between compilation and interpretation was initially confusing because both approaches ultimately help a computer execute programs.

It was also important to ensure that the Python file was saved in the correct mission folder before running it.

## 7. How I Resolved Them

I compared the two approaches based on when translation happens, their typical outputs and their advantages.

I also checked the file location and used the `python3` command from Terminal to execute the Python program.

## 8. Evidence / Files

- `README.md` — Mission 4 documentation.
- `hello.py` — Python program that displays the message `Hello from Python`.
- Program execution output from Terminal.

## 9. Commit Details

**Commit message:** `Compare compilers and interpreters`

The Mission 4 files should be staged and committed separately, pushed to GitHub, and checked online to confirm that both `README.md` and `hello.py` are visible.