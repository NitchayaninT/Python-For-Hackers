import sys
import time

print(sys.version)
print(sys.executable) #current executable bin
print(sys.platform) #linux

for line in sys.stdin:
    if line.strip() == "exit":
        break
    sys.stdout.write(">> {}".format(line))

for i in range(1,5):
    sys.stdout.write(str(i))
    sys.stdout.flush()

for i in range(1,5):
    print(i)

for i in range(0, 51):
    time.sleep(0.1)
    sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(50-i)))
    sys.stdout.flush()
sys.stdout.write("\n")

#Useful when we wanna pass username and pass to the script during execution
print(sys.argv) 

if len(sys.argv) !=3:
    print("[X] to run {} enter a username and password")
    sys.exit(-1)

username = sys.argv[1]
password = sys.argv[2]

print("{} {}".format(username,password))

print(sys.path)
print(sys.modules)

sys.exit(0)