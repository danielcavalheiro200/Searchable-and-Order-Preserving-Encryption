from se import *

foo = encrypt_it('hugo', 'password')
bar = encrypt_it(str(1), 'password')

print(foo)
print(bar)

print(decrypt_it(foo, 'password'))
print(decrypt_it(bar, 'password'))
