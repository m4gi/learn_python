a='594234427b425448'
b='3448545f5633525f'
c='455f5354'
d='7d5a'

a=bytearray.fromhex(a).decode()
b=bytearray.fromhex(b).decode()
c=bytearray.fromhex(c).decode()
d=bytearray.fromhex(d).decode()

a="".join(reversed(a))
b="".join(reversed(b))
c="".join(reversed(c))
d="".join(reversed(d))

print(a+b+c+d)