# Computational Number Theory Library

A high-performance Python library for mathematical algorithms, originally developed to solve computational challenges (Project Euler).

**Note:** This repository contains the *tools* and generic algorithms built to solve problems efficiently. It does **not** contain direct solution scripts or spoilers for specific problem answers, respecting the Project Euler code of conduct.

## Features

### Prime Numbers (`src/primes.py`)
* **Primality Test:** Optimized trial division with $O(\sqrt{n})$ complexity. Handles edge cases and skips multiples of 2 and 3 for speed.

## Project Structure

* `src/`: Contains the reusable algorithms.
* `tests/`: Unit tests ensuring reliability and correctness.

## Usage

You can import these functions into your own scripts:

```python
from src.primes import is_prime
import src.sequences 

if is_prime(104729):
    print("It's prime!")



