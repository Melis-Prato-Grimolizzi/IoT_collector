import configparser
import time
import SessionHTTP as Http
import account as Account


class Collector:
    def __init__(self, bearer):
        self.bearer = bearer
        self.config = configparser.ConfigParser()

    def getAllState(self):
        url = self.config['Urls']['GetUrl']
        session = Http.getDaemonSession()
        header = {
            'Authorization': self.bearer
        }
        response = session.get(url, headers=header)
        # TODO: handle response and trasnform it
        return response.json().to_dict()

    def sendHistory(self, data):
        url = self.config['Urls']['PostUrl']
        session = Http.getDaemonSession()
        header = {
            'Authorization': self.bearer
        }
        response = session.post(url, headers=header, data=data)
        return response.json().to_dict()

    def loop(self):
        timestamp = time.time()
        while True:
            if time.time() - timestamp >= 600:
                timestamp = time.time()
                print("Daje roma!")
                # data = self.getData()
                # self.sendData(data)


if __name__ == '__main__':
    if not Account.userExist():
        Account.createCollector()
    bearer = Account.collectorLogin()

    collector = Collector(bearer)
    collector.loop()
