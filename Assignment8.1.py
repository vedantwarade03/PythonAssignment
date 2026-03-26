src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

f1 = open(src, "r")
data = f1.read()
f1.close()

data = data.upper()

f2 = open(dest, "w")
f2.write(data)
f2.close()

print("File copied successfully.")

print("\nContent written in destination file:\n")
print(data)