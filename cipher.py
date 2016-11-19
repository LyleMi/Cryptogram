from lib.encode.Bacon import Bacon
from lib.encode.Caesar import caesar
from lib.encode.Morse import morse_encode, morse_decode
from lib.encode.Fence import fence_encode, fence_decode
from lib.encode.Vigenere import Vigenere
from lib.crypt.RSA import RSA
from lib.crypt.AES import AES
from lib.crypt.Rabin import Rabin
from lib.crypt.polynomial import Polynomial
from lib.information.Huffman import Huffman
from lib.information.information_theory import entropy, Shanon, Fano


def console_print():
    print "+---------------------------------------------------------+"
    print "|                   Cipher Console                        |"
    print "+---------------------------------------------------------+"
    print "have fun with Bacon/caesar/Morse/Fence/RSA/Rabin here"


def main():
    console_print()
    while True:
        try:
            print '>>>', input()
        except Exception, e:
            print e

if __name__ == '__main__':
    main()
