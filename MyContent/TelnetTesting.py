import sys
import time

if not ('packages.zip' in sys.path):
    sys.path.insert(0, 'packages.zip')

    from _nx import utils
    import pyte
    import telnetlib



class Myscreen(pyte.Screen):
    def set_tab_stop(self):
        utils.clear_terminal()
        pyte.Screen.set_tab_stop(self)

    def draw(self, data):
        print("\n".join(self.display))
        pyte.Screen.draw(self, data)


if __name__ == '__main__':
    screen = Myscreen(80, 24)
    stream = pyte.Stream(screen)

    tnserv = telnetlib.Telnet("towel.blinkenlights.nl")

    while True:
        try:
            read_data = tnserv.read_very_eager()
            # time.sleep(0.5)
            stream.feed(read_data.decode('utf-8', 'ignore'))
        except EOFError:
            break

