decoded_str = input("Input a string to encode: ")


def string_to_binary(string):
    ascii_bin = ''
    for c in string:
        decoded_decimal = str(ord(c))
        binary8 = bin(int(decoded_decimal))[2:]
        while(len(binary8) < 8):
            binary8 = '0' + binary8
        print(binary8)
        ascii_bin += binary8
    return ascii_bin


def binary_to_decimal(binary):
    binary = int(binary)
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def ascii_to_str(decoded_ascii):
    b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    result_str = ''
    decoded_ascii = str(decoded_ascii)
    while len(str(decoded_ascii)) > 0:
        encoded_6_binary = decoded_ascii[0:6]
        while(len(encoded_6_binary) < 6):
            encoded_6_binary += '0'
        print(encoded_6_binary)
        decoded_ascii = decoded_ascii[6:len(decoded_ascii)]
        encoded_decimal = binary_to_decimal(int(encoded_6_binary))
        result_str += b64[encoded_decimal]
    return result_str


def base64_encode(decoded_string):
    decoded_binary = string_to_binary(decoded_string)
    encoded_string = ascii_to_str(decoded_binary)
    if len(decoded_string) % 3 == 1:
        encoded_string += '=='
    elif len(decoded_string) % 3 == 2:
        encoded_string += '='
    return encoded_string


print(base64_encode(decoded_str))
