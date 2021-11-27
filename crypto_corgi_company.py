from cisc108 import assert_equal

def string_conversion(message: str) -> [int]:
    
    '''
    This function converts any message to a list of integers by
    using the ord function.
    
    Args:
    message (str): A message is taken as a string by this function.
    
    Returns:
    ([int]): A list of integers is returned by this function.
    '''
    
    values = []
    for charcter in message:
        value = ord(charcter)
        values.append(value)
    return(values)

assert_equal(string_conversion("H"), [72])
assert_equal(string_conversion("z"), [122])
assert_equal(string_conversion("."), [46])
assert_equal(string_conversion("!"), [33])


def list_conversion(values: [int]) -> str:
    
    '''
    This function converts a list of integers to their string
    value by using the chr function.
    
    Args:
    values ([int]): A list of integers is taken by this function.
    
    Returns:
    (str): A string value is returned by this function.
    '''
    
    message = ""
    for value in values:
        message = message + chr(value)
    return (message)

assert_equal(list_conversion([48]), "0")
assert_equal(list_conversion([109]), "m")
assert_equal(list_conversion([126]), "~")
assert_equal(list_conversion([40]), "(")


def rotate(values: [int], rotation: int) -> [int]:
    
    '''
    This function takes a list of integers and rotates all of
    the integers by a certain value to get a new list of integers.
    
    Args:
    values ([int]): A list of integers is taken by this function.
    
    Returns:
    ([int]): A list of new integers is returned by this function.
    '''
    
    new_values = []
    for value in values:
        value = (value + rotation - 32) % 94 + 32
        new_values.append(value)
    return (new_values)

assert_equal(rotate([66, 67], 2), [68, 69])
assert_equal(rotate([56, 68], -1), [55, 67])


def encrypt_text(message: str, rotation_amount: int) -> str:
    
    '''
    This function takes any message and encrypts that message using
    the rotation value that was given.
    
    Args:
    message (str): A message is taken as a string by this function. 
    rotation (int): A single integer is taken by this function. 
    
    Returns:
    (str): A encrypted string is returned by this function. 
    '''
    
    converted_to_ascii_numbers = string_conversion(message)
    rotated = rotate(converted_to_ascii_numbers, rotation_amount)
    insert_tilde = []
    for a_number in rotated:
        insert_tilde.append(a_number)
        if a_number < 48:
            insert_tilde.append(126)
    back_to_str = list_conversion(insert_tilde)
    return back_to_str

assert_equal(encrypt_text("H", 29), "e")
assert_equal(encrypt_text("2", -30), "r")
assert_equal(encrypt_text("=", -1), "<")
assert_equal(encrypt_text("z", 5), "!~")


def decrypt_text(message: str, rotation: int) -> str:
    
    '''
    This function takes any message and decryptes that message using
    the rotation value that was given.
    
    Args:
    message (str): A message is taken as a string by this function.
    rotation (int): A single integer is taken by this function.
    
    Returns:
    (str): A decrypted string is returned by this function.
    '''
    
    converted_to_original = string_conversion(message)
    filter_tilde = []
    for a_number in converted_to_original:
        if a_number == 126:
            continue
        else:
            filter_tilde.append(a_number)
    un_rotated = rotate(filter_tilde, -rotation)
    back_to_str = list_conversion(un_rotated)
    return back_to_str

assert_equal(decrypt_text("e$++.", 29), "Hello")
assert_equal(decrypt_text("We11", 2), "Uc//")
assert_equal(decrypt_text("blueHens", 4), "^hqaDajo")
assert_equal(decrypt_text("#college", 6), "{]iff_a_")


def hash_text(message: str, base: int, hash_size: int) -> int:
    
    '''
    This function takes any message and converts that message into
    a integer using base and hash_size to uniquely represent that text.
    
    Args:
    message (str): A message is taken as a string by this function.
    base (int): A single integer is taken by this function.
    hash_size (int): A single integer is taken by this function.
    
    Returns:
    (int): An integer representing the message is returned by this
           function.
    '''
    
    list_message = string_conversion(message)
    total = 0
    for count,value in enumerate(list_message):
        new_value = (count + base) ** (value)
        total = new_value + total
    return (total % hash_size)

assert_equal(hash_text("Hello", 10, 10), 2)
assert_equal(hash_text("26!bye", 20, 50), 1)
assert_equal(hash_text(":34we", 12, -10), 8)
assert_equal(hash_text("GoodBye!", 50, 50), 34)


def main():
    
    '''
    This main function that calls all the other functions and provides
    an crypto experience for the user. Relies on user input. 
    
    No Arguments and No Returns. 
    '''

    firstchoice = input('Do you want to encrypt or decrypt?')
    if firstchoice.lower() == "encrypt":
        message = input("Input your desired message")
        firststep = encrypt_text(message, 10)
        hashedmessage = hash_text(firststep, 31, 1000000000)
        return print("The encrypted message is " + firststep + " and its hash value is " + str(hashedmessage)+ ".")
    elif firstchoice.lower() == "decrypt":
        message = input("Input your desired encrypted message")
        firststep = decrypt_text(message, 10)
        print("What is the expected hash value?")
        expectedhash = input()
        if expectedhash == hash_text(message, 31, 1000000000):
            return None
        else:
            return print("The decrypted message is " + firststep)
    else:
        return None


main()









