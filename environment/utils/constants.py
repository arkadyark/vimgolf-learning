import string
VOCAB = string.ascii_letters + string.digits + '!@#$%^&*(){}?+<>,.=-_ ' + '\x1b'
REGISTERS = [chr(x) for x in range(34,122)]
