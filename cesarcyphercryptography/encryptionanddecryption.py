def returnTheModulus(number):
    key = 3
    value = number + key
    if value < 26:
        return value
    return value % 26


def getValueOfCharacter(plain_text):
    character_values = []
    for character in plain_text:
        if is_validate_character(character):
            character = character.lower()
            number = ord(character) - ord('a')
            character_values.append(number)
    return character_values

def is_validate_character(character)->bool:
    if not str.isalpha(character):
        return False
    return True

def getEncryptedModulusValue(plain_text):
    modulus_values = []
    character_values = getValueOfCharacter(plain_text)
    for number in character_values:
        modulus_values.append(returnTheModulus(number))
    return modulus_values


def getEncryptedResult(plain_text):
    encrypted_values = []
    modulus_values = getEncryptedModulusValue(plain_text)
    for value in modulus_values:
        character = chr(value + ord('a'))
        encrypted_values.append(character)
    return encrypted_values


def returnDecryptedModlus(number):
    key = 3
    decryption_value = number - key
    if decryption_value < 0:
        return 26 + decryption_value
    elif decryption_value < 26 and number >= key:
        return decryption_value
    else:
        return decryption_value % 26


def getDecryptedModulusValue(plain_text):
    decrypted_modulus_values = []
    character_values = getValueOfCharacter(plain_text)
    for number in character_values:
       decrypted_modulus_values.append(returnDecryptedModlus(number))
    return decrypted_modulus_values


def getDecryptedResult(plain_text):
    decrypted_values = []
    modulus_values = getDecryptedModulusValue(plain_text)
    for value in modulus_values:
        character = chr(value + ord('a'))
        decrypted_values.append(character)
    return decrypted_values