
import base64
import Crypto.Random 

def generate_key(bits):
    generated = Crypto.Random.OSRNG.posix.DevURandomRNG()   # Returns object which generates binary
    content = generated.read(bits) # read bits
    return base64.b64encode(content) # Encode it into base64