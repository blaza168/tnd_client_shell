import platform
import socket

def get_sys_info():

    return {
        'machine': platform.machine(),
        'version': platform.version(),
        'platform': platform.platform(),
        'uname': platform.uname(),
        'system': platform.system(),
        'processor': platform.processor(),
        'IP': socket.gethostbyname(socket.gethostname())
    }