import sys
import string

from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto import Random

global x, y

class CipherInterface:
    def __init__(self):
        self.key = None

    def setKey(self, key):
        global x,y
        # set key in bytes
        self.key = key.encode()
        if len(self.key) == 8:
                x = DES.new(self.key,DES.MODE_ECB)
        elif len(self.key) == 16:
                y = AES.new(self.key, AES.MODE_ECB)
        else:
            print("Invalid Key")

    def ctol(self, string):
        string.encode('ascii')
        print(string)
        return string

    def ltoc(self, data):
        pass

class AES_cipher(CipherInterface):
    def __init__(self):
        super(AES_cipher, self).__init__()

    # def encrypt(self, lists, key):
    def encrypt(self, buffer, block_size):
        print("buffer: ", buffer)
        print("block size: ", block_size)
        # encrypt and add padding if neccessary
        if len(buffer) % 16 != 0:
            ciphertext = y.encrypt(pad(buffer, block_size))
        else:
            ciphertext = y.encrypt(buffer)
        print("ciphertext: ", ciphertext)
        return ciphertext

    def decrypt(self, buffer, block_size):
        print("buffer: ", buffer)
        print("block size: ", block_size)
        # decrypt and add padding if neccessary
        if len(buffer) % 16 != 0:
            plaintext = unpad(y.decrypt(buffer), block_size)
        else:
            plaintext = y.decrypt(buffer)
        print("plaintext: ", plaintext)
        return plaintext

# 
class DES_cipher(CipherInterface):
    def __init__(self):
        super(DES_cipher, self).__init__()

    # def encrypt(self, lists, key):
    def encrypt(self, buffer, block_size):
        print("buffer: ", buffer)
        print("buffer size: ", len(buffer))
        print("block size: ", block_size)
        # encrypt and add padding if neccessary
        # while len(buffer) % 8 != 0:
            # buffer += b'0'
        # ciphertext = x.encrypt(buffer)
        
        if len(buffer) % 8 != 0:
            ciphertext = x.encrypt(pad(buffer, block_size))
        else:
            ciphertext = x.encrypt(buffer)

        print("ciphertext: ", ciphertext)
        return ciphertext

    # def decrypt(self, output, matrix):
    def decrypt(self, buffer, block_size):
        print("buffer: ", buffer)
        print("buffer size: ", len(buffer))
        print("block size: ", block_size)
        # decrypt and add padding if neccessary
        # while len(buffer) % 8 != 0:
        #     buffer += b'0'
        # plaintext = x.decrypt(buffer)

        if len(buffer) % 8 != 0:
            plaintext = unpad(x.decrypt(buffer), block_size)
        else:
            plaintext = x.decrypt(buffer)        

        print("plaintext before replacing padding: ", plaintext)
        if ('\x01' in plaintext.decode('ASCII')):
            print("padding found!")
            plaintext = plaintext.rstrip(b'\x01')
        elif ('\x07' in plaintext.decode('ASCII')):
            print("space padding found!")
            plaintext = plaintext.rstrip(b'\x07')
        
        print("plaintext after replacing padding: ", plaintext)
        return plaintext

# note: buffer size = 8 was in 2nd param before
# def chunks(filename, buffer_size):
#     print("in chunks: buffer size: ", buffer_size)
#     with open(filename, "rb") as fp:
#         chunk = fp.read(buffer_size)
#         while chunk:
#             yield chunk
#             chunk = fp.read(buffer_size)

# # note: buffer size = 8 was in 2nd param before
# def blocks(filename, buffersize):
#     print("in chunks: buffer size: ", buffersize)
#     blocksize = buffersize / 2
#     for chunk in chunks(filename, buffersize):
#         type(chunk[:blocksize])
#         block = [chunk[:blocksize],chunk[blocksize:]]
#         yield block

def main():
    cipher = None
    cipherName = sys.argv[1]
    enc = sys.argv[3]
    inputFile = sys.argv[4]
    outputFile = sys.argv[5]
    buffersize = 0

    if cipherName == "AES":
        cipher = AES_cipher() 
        buffersize = 16
    elif cipherName == "DES":
        cipher = DES_cipher()
        buffersize = 8
    else:
        print("Enter supported cipher")
        exit

    cipher.setKey(sys.argv[2])

    # open files for reading/writing later
    input_file = open(inputFile, 'rb')
    output_file = open(outputFile, 'wb')

    # read 8/16 bytes depending on DES/AES
    buffer = input_file.read(buffersize)
    
    while len(buffer) > 0:
        if enc == 'ENC':
            # store the encrypted data and write it to a file,
            # then move the buffer to the next data block
            cipher_text = cipher.encrypt(buffer, buffersize)
            output_file.write(cipher_text)
            buffer = input_file.read(buffersize)
        elif enc == 'DEC':
            # store the decrypted data and write it to a file,
            # then move the buffer to the next data block
            plain_text = cipher.decrypt(buffer, buffersize)
            output_file.write(plain_text)
            buffer = input_file.read(buffersize)
        else:
            print("Choose ENC/DEC")
            exit()
    # close files
    input_file.close()
    output_file.close()

    # with open(outputFile, "wb") as fp:
    #         for block in blocks(inputFile, buffersize):
    #             if enc == "enc":
    #                 fp.write(cipher.encrypt(block, len(block)))
    #             elif enc == "dec":
    #                  fp.write(cipher.decrypt(block, len(block)))
    #             else:
    #                 print("Choose enc/dec")
    #                 exit

if __name__ == "__main__":
    if len(sys.argv) == 6:
        main()
    else:
        print("Argument List Length Error")