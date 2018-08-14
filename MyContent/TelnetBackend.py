import sys

if not ('packages.zip' in sys.path):
    sys.path.insert(0, 'packages.zip')

    import pyte
    import telnetlib


class TelnetBackend:
    def __init__(self, MudData):
        self.screen = pyte.Screen(80, 24)
        self.stream = pyte.ByteStream(self.screen)
        self.telnetConnection = telnetlib.Telnet()
        self.MudDataInner = MudData

    def OpenIt(self):
        try:
            self.telnetConnection.close()
            self.telnetConnection.open(self.MudDataInner['server_host'], self.MudDataInner['server_port'])
            return True
        except:
            self.MudDataInner[
                'World_text'] = "Error Connection Failed Pleease Try Again\nPlease Enter the server info like this: serverhost,port\n"

    def UpdateWorld(self):
        try:
            tnet_data = self.telnetConnection.read_very_eager()
            if tnet_data != b'':
                self.stream.feed(tnet_data)
        except EOFError:
            self.MudDataInner[
                'World_text'] = "Error Connection Closed Pleease Reconnect\nPlease Enter the server info like this: serverhost,port\n"
            self.MudDataInner['Entered_server_data'] = False

    def PrintWorld(self):
        self.MudDataInner['World_text'] = "\n".join(self.screen.display)

    def SendMessage(self):
        playerText = self.MudDataInner['Player_text'] + "\r\n"
        if(playerText != "\n"):
            self.telnetConnection.write(playerText.encode('ascii'))
        self.MudDataInner['Clear_Player_data'] = True
