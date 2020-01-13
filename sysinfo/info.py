import platform

def get_sys_info():

    return {
        'machine': platform.machine(),
        'version': platform.version(),
        'platform': platform.platform(),
        'uname': platform.uname(),
        'system': platform.system(),
        'processor': platform.processor()
    }