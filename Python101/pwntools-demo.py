from pwn import *
import hashlib

print(cyclic(50))
print(cyclic_find("laaa"))

print(shellcraft.sh()) # Returns assembly (as text) for spawning 
print(hexdump(asm(shellcraft.sh()))) # Assembles that assembly into raw machine code (bytes) and print in hex

# Local Process interaction
p = process("/bin/sh") # Spawns a local process
p.sendline("echo hello;") # Sends a line to the process' stdin
p.interactive() # Gives us interactive TTY to that process

# Remote Process interaction
r = remote("127.0.0.1", 1234) # Open TCP connection to host:port
r.sendline("hello!")
r.interactive()
r.close()

# Packing/Unpacking
print(p32(0x13371337)) # Packs a 32-bit integer into little-endian bytes (e.g., for stack overwrite payloads)
print(hex(u32(p32(0x13371337)))) # Unpacks 4 little-endian bytes back to a Python int.

# ELF parsing & symbols
l = ELF('/bin/bash') # Loads and parses an ELF binary, lets us query symbols/sections

print(hex(l.address))
print(hex(l.entry))

print(hex(l.got['write']))
print(hex(l.plt['write']))

for address in l.search(b'/bin/sh\x00'):
    print(hex(address))

print(hex(next(l.search(asm('jmp esp')))))

# ROP gadgets
r = ROP(l)
print(r.rbx)

# Encodings, hashing
# (A ^ B) ^ A -> (A ^ A) ^ B -> 0 ^ B
print(xor(xor("A","B"), "A")) # simplifies to "B"
print(b64e(b"test"))
print(b64d(b"dGVzdA=="))
print(md5sumhex(b"hello"))
print(sha1sumhex(b"hello"))

print(bits(b'a')) # Converts bytes to a list of bits (0/1). Default is little-endian bit order.
print(unbits([0,1,1,0,0,0,0,1]))