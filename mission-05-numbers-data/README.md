# Mission 5 — Numbers and Data

## 1. Task and Objective

The objective of this mission was to understand how computers represent numbers and text. I practised converting numbers between decimal, binary and hexadecimal systems, verified the conversions using Python, created a number converter program and learned about ASCII and UTF-8 encoding.

## 2. Task 5.1 — Manual Number Conversions

### A. Decimal 13 to Binary

Divide the number repeatedly by 2 and record the remainders:

- 13 ÷ 2 = 6, remainder 1
- 6 ÷ 2 = 3, remainder 0
- 3 ÷ 2 = 1, remainder 1
- 1 ÷ 2 = 0, remainder 1

Read the remainders from bottom to top.

**Answer: 13₁₀ = 1101₂**

### B. Decimal 25 to Binary

- 25 ÷ 2 = 12, remainder 1
- 12 ÷ 2 = 6, remainder 0
- 6 ÷ 2 = 3, remainder 0
- 3 ÷ 2 = 1, remainder 1
- 1 ÷ 2 = 0, remainder 1

Read the remainders from bottom to top.

**Answer: 25₁₀ = 11001₂**

### C. Binary 1010 to Decimal

Each binary digit represents a power of 2:

\[
(1\times 2^3)+(0\times 2^2)+(1\times 2^1)+(0\times 2^0)
\]

\[
=8+0+2+0=10
\]

**Answer: 1010₂ = 10₁₀**

### D. Binary 1101 to Decimal

\[
(1\times 2^3)+(1\times 2^2)+(0\times 2^1)+(1\times 2^0)
\]

\[
=8+4+0+1=13
\]

**Answer: 1101₂ = 13₁₀**

### E. Hexadecimal A to Decimal

In hexadecimal, A represents 10.

**Answer: A₁₆ = 10₁₀**

### F. Hexadecimal 1F to Decimal

In hexadecimal, F represents 15.

\[
(1\times 16^1)+(15\times 16^0)
\]

\[
=16+15=31
\]

**Answer: 1F₁₆ = 31₁₀**

### G. Binary 1111 to Hexadecimal

Group the binary digits into four bits:

\[
1111_2 = 15_{10}
\]

In hexadecimal, 15 is represented by F.

**Answer: 1111₂ = F₁₆**

## 3. Task 5.2 — Verification Using Python

I used Python's built-in conversion functions in the interactive environment to verify the manual calculations.

Open Python from Terminal using:

```bash
python3
```

Then enter these expressions one by one:

| Expression | Expected result |
|---|---|
| `bin(13)` | `'0b1101'` |
| `bin(25)` | `'0b11001'` |
| `int('1010', 2)` | `10` |
| `int('1101', 2)` | `13` |
| `hex(13)` | `'0xd'` |
| `int('1F', 16)` | `31` |
| `hex(int('1111', 2))` | `'0xf'` |

The results should match the manual calculations. Python adds `0b` before binary values and `0x` before hexadecimal values to identify their number systems.

To exit the interactive environment, enter:

```python
exit()
```

## 4. Task 5.3 — Building a Number Converter

I created a Python program named `number_converter.py`.

The program:
- Accepts a positive decimal number from the user.
- Converts the decimal number into binary.
- Converts the decimal number into hexadecimal.
- Displays the converted values.

### Python functions used

- `input()` accepts information entered by the user.
- `int()` converts the entered text into an integer.
- `bin()` converts an integer into its binary representation.
- `hex()` converts an integer into its hexadecimal representation.
- `upper()` changes hexadecimal letters into uppercase.

### Test cases

The following are the expected results for three test inputs. I will verify them by running the program.

| Decimal input | Binary output | Hexadecimal output |
|---:|---:|---:|
| 13 | 1101 | D |
| 25 | 11001 | 19 |
| 42 | 101010 | 2A |

### Understanding

Binary uses only two digits, 0 and 1, while hexadecimal uses sixteen symbols: 0–9 and A–F. Python's built-in conversion functions make it easy to convert integers between these number systems without manually calculating every digit.

## 5. Task 5.4 — How Is Text Stored?

### ASCII codes

- Uppercase `A` = 65
- Lowercase `a` = 97

### Why does a computer need an encoding standard?

A computer stores information as numbers and bits. An encoding standard assigns numeric values to characters so that computers can store, process and exchange text consistently.

### Example of a character outside basic ASCII

The character `₹` (Indian Rupee symbol) is not part of basic ASCII. UTF-8 can represent it.

## 6. Commands and Tools Used

- `python3` — opened the Python interpreter and ran the converter.
- `bin()` — converted decimal numbers into binary.
- `hex()` — converted decimal numbers into hexadecimal.
- `int()` — converted binary and hexadecimal strings into decimal integers.
- `input()` — accepted user input in the converter program.
- Visual Studio Code — created and edited the Python and README files.
- Terminal — executed Python commands and the converter.

## 7. My Understanding

Through this mission, I understood that computers use binary because their basic digital representation works with two states, 0 and 1. Decimal, binary and hexadecimal are different ways of representing numerical values. I also learned that Python provides built-in functions for converting between these systems. Finally, I understood that encoding standards such as ASCII and UTF-8 allow computers to represent text using numbers.

## 8. Difficulties Faced

One thing I needed to understand was how binary and hexadecimal values are represented in Python. The prefixes `0b` and `0x` initially looked like part of the converted number.

## 9. How I Resolved Them

I checked the output of Python's built-in conversion functions and learned that `0b` identifies a binary value and `0x` identifies a hexadecimal value. I also used the manual calculations to cross-check the results.

## 10. Evidence and Files

- `README.md` — manual calculations, Python verification, program explanation and text-encoding notes.
- `number_converter.py` — Python program for converting decimal numbers into binary and hexadecimal.

## 11. Commit Details

**Commit message:**

"Build number converter and practise data representation"


The changes should be committed and pushed to the GitHub repository. I will verify that both files are visible in the Mission 5 folder on GitHub.