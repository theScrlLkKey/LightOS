from cryptography.fernet import Fernet


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    print('Reading file...')
    try:
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
    except FileNotFoundError:
        print('File does not exist!')
        exit()
    except MemoryError:
        print('Gah. Your file is too big!(999Mb max)')
        exit()
    except:
        print('A error occurred.')
        exit()

    # encrypt data
    print('Encrypting file...')
    try:
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
        with open('enc_' + filename, "wb") as file:
            file.write(encrypted_data)
    except:
        print('A error occurred.')
        exit()


def encrypt_emb(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    print('Reading file...')
    try:
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
    except FileNotFoundError:
        print('File does not exist!')
        exit()
    except MemoryError:
        print('Gah. Your file is too big!(999Mb max)')
        exit()
    except:
        print('A error occurred.')
        exit()

    #encrypt data
    print('Encrypting file...')
    try:
        encrypted_data = f.encrypt(file_data)
    #write the encrypted file
        with open('enc_' + filename, "wb") as file:
            file.write(encrypted_data)
        with open('enc_' + filename, "a") as file:
            file.write(',-,'+key)
    except:
        print('A error occurred.')
        exit()


def encrypt_emb2(filename, key, password):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    print('Reading file...')
    try:
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
    except FileNotFoundError:
        print('File does not exist!')
        exit()
    except MemoryError:
        print('Gah. Your file is too big!(999Mb max)')
        exit()
    except:
        print('A error occurred.')
        exit()

    #encrypt data
    print('Encrypting file...')
    try:
        encrypted_data = f.encrypt(file_data)
        password_enc = f.encrypt(password.encode("utf-8"))
        #write the encrypted file
        with open('enc_' + filename, "wb") as file:
            file.write(encrypted_data)
        with open('enc_' + filename, "a") as file:
            file.write('`-`'+key)
        with open('enc_' + filename, "a") as file:
            file.write(',-,'+password_enc.decode("utf-8"))
    except:
        print('A error occurred.')
        exit()


def encrypt_aio(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    print('Reading file...')
    try:
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
    except FileNotFoundError:
        print('File does not exist!')
        exit()
    except MemoryError:
        print('Gah. Your file is too big!(999Mb max)')
        exit()
    except:
        print('A error occurred.')
        exit()

    #encrypt data
    print('Encrypting file...')
    try:
        encrypted_data = f.encrypt(file_data)
    #write the encrypted file
        inj = """
from cryptography.fernet import Fernet   
print('Reading file...')
key = input('Key? ')
f = Fernet(key.encode("utf-8"))
encrypted_data = data
print('Decrypting file...')
try:
    decrypted_data = f.decrypt(encrypted_data.encode("utf-8"))
    with open('dec_'+'"""+filename+"""', "wb") as file:
        file.write(decrypted_data)
except:
    print('A error occurred.')
    exit()
print('Done.')"""
        dat = 'data = """' + encrypted_data.decode("utf-8") + '"""'
        with open('enc_' + filename + '.py' , "wb") as file:
            file.write(dat.encode("utf-8"))
        with open('enc_' + filename + '.py', "a") as file:
            file.write(inj)
    except:
        print('A error occurred.')
        exit()


def encrypt_aio_emb(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    print('Reading file...')
    try:
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
    except FileNotFoundError:
        print('File does not exist!')
        exit()
    except MemoryError:
        print('Gah. Your file is too big!(999Mb max)')
        exit()
    except:
        print('A error occurred.')
        exit()

    #encrypt data
    print('Encrypting file...')
    try:
        encrypted_data = f.encrypt(file_data)
    #write the encrypted file
        inj = """
data = data.encode("utf-8")
from cryptography.fernet import Fernet   
print('Reading file...')
sep = ',-,'
sep = sep.encode("utf-8")
encrypted_data, key = data.split(sep)
f = Fernet(key)
print('Decrypting file...')
try:
    decrypted_data = f.decrypt(encrypted_data)
    with open('dec_'+'"""+filename+"""', "wb") as file:
        file.write(decrypted_data)
except:
    print('A error occurred.')
    exit()
print('Done.')"""
        dat = 'data = """' + encrypted_data.decode("utf-8") + ',-,' + key + '"""'
        with open('enc_' + filename + '.py' , "wb") as file:
            file.write(dat.encode("utf-8"))
        with open('enc_' + filename + '.py', "a") as file:
            file.write(inj)
    except:
        print('A error occurred.')
        exit()


def encrypt_aio_emb2(filename, key, password):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    print('Reading file...')
    try:
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
    except FileNotFoundError:
        print('File does not exist!')
        exit()
    except MemoryError:
        print('Gah. Your file is too big!(999Mb max)')
        exit()
    except:
        print('A error occurred.')
        exit()

    #encrypt data
    print('Encrypting file...')
    try:
        encrypted_data = f.encrypt(file_data)
        password_enc = f.encrypt(password.encode("utf-8"))
    #write the encrypted file
        inj = """
data = data.encode("utf-8")
from cryptography.fernet import Fernet   
print('Reading file...')
password = input('Password? ')
sep = '`-`'
sep = sep.encode("utf-8")
sep2 = ',-,'
sep2 = sep2.encode("utf-8")
encrypted_data, file_data = data.split(sep)
key, rpassword = file_data.split(sep2)
f = Fernet(key)
print('Decrypting file...')
try:

    decrypted_data = f.decrypt(encrypted_data)
    password_dec = f.decrypt(rpassword)
    if password_dec.decode("utf-8") == password:
        with open('dec_'+'"""+filename+"""', "wb") as file:
            file.write(decrypted_data)
    else:
        print('Wrong password.')
        exit()
except:
    print('A error occurred.')
    exit()
print('Done.')"""
        dat = 'data = """' + encrypted_data.decode("utf-8") + '`-`' + key + ',-,' + password_enc.decode("utf-8") + '"""'
        with open('enc_' + filename + '.py' , "wb") as file:
            file.write(dat.encode("utf-8"))
        with open('enc_' + filename + '.py', "a") as file:
            file.write(inj)
    except:
        print('A error occurred.')
        exit()




def write_key():
    """
    Generates a key and save it into a file
    """
    k = Fernet.generate_key()
    nbkey = k.decode("utf-8")
    return k


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    print('Reading file...')
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    print('Decrypting file...')
    try:
        decrypted_data = f.decrypt(encrypted_data)
        # write the original file
        with open('dec_' + filename, "wb") as file:
            file.write(decrypted_data)
    except:
        print('A error occurred. Check key.')
        exit()


def decrypt_emb(filename):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    print('Reading file...')
    with open(filename, "rb") as file:
        # read the encrypted data
        file_data = file.read()
    sep = ',-,'
    sep = sep.encode("utf-8")
    encrypted_data, key = file_data.split(sep)
    f = Fernet(key)
    # decrypt data
    print('Decrypting file...')
    try:
        decrypted_data = f.decrypt(encrypted_data)
        # write the original file
        with open('dec_' + filename, "wb") as file:
            file.write(decrypted_data)
    except:
        print('A error occurred.')
        exit()



def decrypt_emb2(filename, password):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    print('Reading file...')
    with open(filename, "rb") as file:
        # read the encrypted data
        file_data = file.read()
    sep = '`-`'
    sep = sep.encode("utf-8")
    sep2 = ',-,'
    sep2 = sep2.encode("utf-8")
    encrypted_data, file_data = file_data.split(sep)
    key, rpassword = file_data.split(sep2)
    f = Fernet(key)
    # decrypt data
    print('Decrypting file...')
    try:
        decrypted_data = f.decrypt(encrypted_data)
        password_dec = f.decrypt(rpassword)
        # write the original file
        if password_dec.decode("utf-8") == password:
            with open('dec_' + filename, "wb") as file:
                file.write(decrypted_data)
        else:
            print('Wrong password.')
            exit()
    except:
        print('A error occurred.')
        exit()


if __name__ == "__main__":
    while True:
        sugg_key = write_key()
        print('Random key: ' + sugg_key.decode("utf-8"))
        key = input('Key? (if you don\'t have a key, just press enter and the above key will be used, so remember it.) ')
        if key == '':
            key = sugg_key.decode("utf-8")

        filename = input('Filename? ')
        mode = input('''Mode? (scr for super-secure format (needs key and program to decrypt), emb for embedded format 1.0 (needs program to decrypt, no key), 
        emb2 for embedded format 2.0 (needs program and custom password to decrypt), aio for all in one format (no program needed, just run the file and enter the key),
        aio-emb for all in one-embedded format 1.0 (this is truly useless, no security at all), aio-emb2 for all in one-embedded format 2.0  (no program needed, just run the file and enter the custom password)
        ''')
        try:
            if mode == 'scr':
                act = input('Encrypt or Decrypt? (enc/dec) ')
                if act == 'enc':
                    encrypt(filename, key)
                elif act == 'dec':
                    decrypt(filename, key)
                else:
                    print('That is not a command.')
            elif mode == 'emb':
                act = input('Encrypt or Decrypt? (enc/dec) ')
                if act == 'enc':
                    encrypt_emb(filename, key)
                elif act == 'dec':
                    decrypt_emb(filename)
                else:
                    print('That is not a command.')
            elif mode == 'emb2':
                act = input('Encrypt or Decrypt? (enc/dec) ')
                if act == 'enc':
                    password = input('Password? ')
                    encrypt_emb2(filename, key, password)
                elif act == 'dec':
                    password = input('Password? ')
                    decrypt_emb2(filename, password)
                else:
                    print('That is not a command.')
            elif mode == 'aio':
               encrypt_aio(filename, key)
            elif mode == 'aio-emb':
                encrypt_aio_emb(filename, key)
            elif mode == 'aio-emb2':
                password = input('Password? ')
                encrypt_aio_emb2(filename, key, password)
            else:
                print('That is not a command.')
        except:
            print('A error occurred. Bad key or wrong format')


        print('Done!')
        mre = input('Encrypt or decrypt another file? (Y/n) ')
        if mre == 'y' or mre == 'Y' or mre == '':
            continue
        else:
            exit()

