import time


print("Computing the answer")
print("......")

time.sleep(10)

with open("result.txt", "w") as f:
    f.write("The answer is 42")
