import sys

args = sys.argv
argc = len(sys.argv)
print("=== Command Quest ===")
if argc == 1:
    print("No arguments provided!")
    print(f"Program name: {args[0]}")
    print(f"Total arguments: {argc}")
else:
    print(f"Program name: {args[0]}")
    print(f"Arguments received: {argc - 1}")
    for i in range(1, argc):
        print(f"Argument {i}: {args[i]}")
    print(f"Total arguments: {argc}")
