import hashlib
import hmac
from Crypto.Cipher import AES


def generate_key(password):
    hasher = hashlib.sha256()
    hasher.update(password.encode())
    return hasher.digest()


def encrypt_it(data, password):
    key = generate_key(password)
    cipher = AES.new(key, AES.MODE_SIV)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return ciphertext + tag


def decrypt_it(encrypted_data, password):
    key = generate_key(password)
    cipher = AES.new(key, AES.MODE_SIV)
    ciphertext, tag = encrypted_data[:-16], encrypted_data[-16:]
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_data.decode()


def hmac_it(data, password):
    h = hmac.new(password.encode(), data.encode(), hashlib.sha256)
    return h.hexdigest()


plainDict = {'var': 'input',
             'sink': 'var'}

cryptDict = {encrypt_it('var', 'password'): hmac_it('input', 'password'),
             hmac_it('sink', 'password'): encrypt_it('var', 'password')}

while True:
    search = input('Enter search token: ')
    if search == 'exit':
        break
    xsearch = hmac_it(search, 'password')
    if xsearch in cryptDict:
        print('Found! Printing full data flow')
        while True:
            print(xsearch)
            if xsearch in cryptDict:
                xsearch = cryptDict[xsearch]
            else:
                break
        if hmac_it('input', 'password') == xsearch and search == 'sink':
            print('Vulnerability detected!')
    else:
        print('Not found!')
