# /usr/bin/python3


from base64 import b64decode, b64encode


def decrypt():
    key = "n0k3y"
    cipher = b64decode('KVUGUgoaWQABSVwCEEo2G28PABocSRtHJgMDFg==')

    flag = ''

    for c, i in enumerate(cipher):
        flag += chr(ord(key[c % 5]) ^ i)

    print(flag)


decrypt()
