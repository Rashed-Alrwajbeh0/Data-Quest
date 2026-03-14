import sys
args = sys.argv
num = len(args)
if num == 1:
    print("=== Command Quest ===")
    print("No arguments provided!\n"
          f"Program name: {args[0]}\n"
          f"Total arguments: {num}")
else:
    print("=== Command Quest ===\n"
          f"Program name: {args[0]}\n"
          f"Arguments received: {num - 1}")
    i = 0
    while i < num - 1:
        print(f"Argument {i + 1}: {args[i + 1]}")
        i += 1
    print(f"Total arguments: {num}")
