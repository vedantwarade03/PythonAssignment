src = input("Enter source python file: ")
dest = input("Enter destination file: ")

f1 = open(src, "r")
lines = f1.readlines()
f1.close()

f2 = open(dest, "w")

for line in lines:
    if not line.strip().startswith("#"):
        f2.write(line)

f2.close()

print("\nSource File Content:\n")
f1 = open(src, "r")
print(f1.read())
f1.close()

print("\nDestination File Content:\n")
f2 = open(dest, "r")
print(f2.read())
f2.close()