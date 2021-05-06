#test
import hashlib
import binascii

def main():
    # user = "root:0e0c1080$1adb8dfa0cca642b24a7f70609fcab90::0:99999:7:::"
    # colon1 = user.find(":")
    # colon2 = user.find(":", colon1 + 1)
    # dollar = user.find("$")
    # salt = user[colon1 + 1:dollar]
    # password = user[dollar + 1:colon2]
    # salted_password = salt + password
    #
    # print(salted_password)
    # print(colon1)
    # print(colon2)
    # print(password)
    # print(salt)

    jeff = "jondich:2fe7cec3131fa9662906ecfb2eac8a49::0:99999:7:::"

    colon1 = jeff.find(":")
    colon2 = jeff.find(":", colon1 + 1)

    password = jeff[colon1 + 1:colon2]

    test = compute_hash("moose")

    if test == password:
        print("Success")


def compute_hash(password):
    # Compute the MD5 hash of this example password
    #print('password ({0}): {1}'.format(type(password), password))

    encodedPassword = password.encode('utf-8') # type=bytes
    #print('encodedPassword ({0}): {1}'.format(type(encodedPassword), encodedPassword))

    md5 = hashlib.md5(encodedPassword)
    passwordHash = md5.digest() # type=bytes
    #print('passwordHash ({0}): {1}'.format(type(passwordHash), passwordHash))

    passwordHashAsHex = binascii.hexlify(passwordHash) # weirdly, still type=bytes
    #print('passwordHashAsHex ({0}): {1}'.format(type(passwordHashAsHex), passwordHashAsHex))

    passwordHashAsHexString = passwordHashAsHex.decode('utf-8') # type=string
    #print('passwordHashAsHexString ({0}): {1}'.format(type(passwordHashAsHexString), passwordHashAsHexString))

    return passwordHashAsHexString


main()
