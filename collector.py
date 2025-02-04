import configparser
import time
import SessionHTTP as Http
import account as Account
import pandas as pd


class Collector:
    def __init__(self, bearer):
        self.bearer = bearer
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.base_url = self.config.get('Urls', 'BaseUrl')
        self.data = pd.read_csv('data/time_series.csv')
        self.index = 0

    def updateParkingHistory(self):
        url_trigger = self.config.get('Urls', 'UpdateParkingHistory')
        url_trigger = self.base_url + url_trigger
        update_state = self.config.get('Urls', 'UpdateSlot')
        url_update_state = self.base_url + update_state
        session = Http.getDaemonSession()
        header = {
            'Authorization': self.bearer
        }
        for i in range(3, 200):
            state = self.data[self.data['id'] == i]['y'].values[self.index]
            response = session.post(url_update_state, headers=header, data={'parking_id': i+1, 'state': state})
            print("DEBUG: Response for server (Update State Manual): ", response.text)

        response = session.post(url_trigger, headers=header)
        print("DEBUG: Response for server (Update Parking History): ", response.text)
        self.index += 1
        if self.index >= (len(self.data[self.data['id'] == 1]) - 1):
            self.index = 0

    def loop(self):
        timestamp = time.time()
        try:
            while True:
                if time.time() - timestamp >= 3600:
                    timestamp = time.time()
                    print("Aridaje!")
                    self.updateParkingHistory()
        except KeyboardInterrupt:
            print("Collector exiting...")



if __name__ == '__main__':
    bearer = Account.collectorLogin()

    collector = Collector(bearer)
    collector.loop()
    exit(0)
