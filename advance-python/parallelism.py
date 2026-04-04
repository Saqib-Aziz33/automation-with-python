# Parallelism → actually running tasks simultaneously (at the same time, using multiple CPUs)

"""
Parallelism is useful for CPU-bound tasks, like:

Image processing
Machine learning
Heavy calculations

Python uses multiprocessing for true parallelism because of the GIL (Global Interpreter Lock).
"""

from multiprocessing import Pool
import time


def square(n):
    time.sleep(1)
    return n * n


if __name__ == "__main__":
    with Pool(4) as p:
        result = p.map(square, [1, 2, 3, 4])
    print(result)


"""
🔹 Real-world use case (Parallelism)

👉 Image processing pipeline

Example:

Processing 1000 images
Each CPU core handles a batch

Used in:

AI/ML workloads
Video rendering
Scientific computing
"""


# Use asyncio / threading 👉 when waiting (network, disk)
# Use multiprocessing 👉 when computing (CPU heavy)
