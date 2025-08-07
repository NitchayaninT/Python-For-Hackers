# How to read and write files
# Maybe read from common.txt!
# read, write, append mode
d = open('/usr/share/dirb/wordlists/common.txt')
print(d.readlines())

# Results in empty list
print(d.readlines())

# change the pointer to the 0 position since the file have been read from above
d.seek(0)
print(d.readlines())

d.seek(0)

# Iterate over each line in a file
for line in d:
    print(line.strip())

d.close()

# Write to file, starter.txt doesnt exist at first
f = open("starter.txt", "w")
f.write("test line!")
f.close()

# Append Mode
f = open("starter.txt", "a")
f.write("Line two")
f.close()

print(f.name)
print(f.closed)
print(f.mode)

# Iterate rockyou.txt, which is a large file
# We can use the file object as an iterator "f"
with open("/usr/share/wordlists/rockyou.txt", encoding='latin-1') as f:
    for line in f:
        pass

# Input
while True:
    test = input("Enter the IP:")
    print(">>> {}".format(test))
    if test == "exit":
        break
    else:
        print("exploiting...")