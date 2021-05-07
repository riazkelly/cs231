import hashlib
import binascii

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

def main():
    words = [line.strip().lower() for line in open('words.txt')]
    guessed_passwords = []

    with open("passwords1.txt") as f:
        users = f.read().splitlines()

    count = 0
    hashcount = 0
    possible_passwords = {}

    for word in words:
        for user in users:
            colon1 = user.find(":")
            dollar = user.find("$")
            salt = user[colon1 + 1:dollar]
            hash = compute_hash(salt + word)
            possible_passwords[hash] = word
            count += 1

    for user in users:
        dollar = user.find("$")
        colon2 = user.find(":", dollar + 1)
        password = user[dollar + 1:colon2]
        if password in possible_passwords:
            hashcount += 1
            user_password = user[0:colon1] + ":" + possible_passwords[password]
            print(user_password)

    print(count)
    print(hashcount)


    # for user in users:
    #     colon1 = user.find(":")
    #     colon2 = user.find(":", colon1 + 1)
    #     dollar = user.find("$")
    #     salt = user[colon1 + 1:dollar]
    #     password = user[dollar + 1:colon2]
    #
    #     for word in words:
    #         word = salt + word
    #         word_hash = compute_hash(word)
    #         # print(word_hash)
    #
    #         if(word_hash == password):
    #             user_password = user[0:colon1] + ":" + word
    #             guessed_passwords.append(user_password)
    #             print(user_password + "\n")

            # for word2 in words:
            #     long_word = salt + word + word2
            #     long_word_hash = compute_hash(long_word)
            #
            #     if(long_word_hash == password):
            #         user_password = user[0:colon1] + ":" + password
            #         guessed_passwords.append(user_password)
            #         print(user_password + "\n")

    # for password in guessed_passwords:
    #     print(password + "\n")

main()
