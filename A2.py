import sys
import string

class CipherInterface:
    def __init__(self):
        self.key = None

    def setKey(self, key):
        self.key = key

    def ctol(self, string):
        string.encode('ascii')
        print(string)
        return string

    def ltoc(self, data):
        pass

class AES(CipherInterface):
    def __init__(self):
        super(AES, self).__init__()

    def encode(self, lists, key):
        pass

    def decode(self, output, matrix):
        pass

class DES(CipherInterface):
    def __init__(self):
        super(DES, self).__init__()

    def encode(self, lists, key):
        pass

    def decode(self, output, matrix):
        pass

def chunks(filename, buffer_size=8):
    with open(filename, "rb") as fp:
        chunk = fp.read(buffer_size)
        while chunk:
            yield chunk
            chunk = fp.read(buffer_size)

def blocks(filename, buffersize=8):
    blocksize = buffersize / 2
    for chunk in chunks(filename, buffersize):
        block = [chunk[:blocksize],chunk[blocksize:]]
        yield block

def main():
    cipher = None
    cipherName = sys.argv[1]
    enc = sys.argv[3]
    inputFile = sys.argv[4]
    outputFile = sys.argv[5]
    buffersize = 8

    if cipherName == "AES":
        cipher = AES() 
        buffersize = 8
    elif cipherName == "DES":
        cipher = DES()
        buffersize = 16
    else:
        print("Enter supported cipher")
        exit

    cipher.setKey(sys.argv[2])

    with open(outputFile, "wb") as fp:
            for block in blocks(inputFile, buffersize):
                if enc == "enc":
                    fp.write(cipher.encrypt(block))
                elif enc == "dec":
                     fp.write(cipher.decrypt(block))
                else:
                    print("Choose enc/dec")
                    exit

if __name__ == "__main__":
    if len(sys.argv) == 6:
        main()
    else:
        print("Argument List Length Error")