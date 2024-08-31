import random
from pyope.ope import OPE

key = OPE.generate_key()
cipher = OPE(key)

lineno = list(range(1, 100))
random.shuffle(lineno)

print(lineno)

cyphered = []
for i in lineno:
    cyphered.append(cipher.encrypt(i))

random.shuffle(cyphered)
print(cyphered)

cyphered.sort()
print(cyphered)

for i in cyphered:
    print(cipher.decrypt(i))
