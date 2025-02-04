import SessionHTTP as Http
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def createCollector():
    session = Http.getSession()
    base = config.get('Urls', 'BaseUrl')
    create_collector_url = config.get('Urls', 'CreateCollector')
    url = base + create_collector_url
    username = config.get('Account', 'username')
    password = config.get('Account', 'password')
    body = {
        'username': username,
        'password': password
    }
    response = session.post(url, data=body)
    print(f"DEBUG: Response for server (Create user): {response.text}")


def collectorLogin():
    session = Http.getSession()
    base = config.get('Urls', 'BaseUrl')
    login_collector_url = config.get('Urls', 'Login')
    url = base + login_collector_url
    username = config.get('Account', 'username')
    password = config.get('Account', 'password')
    data = {
        'username': username,
        'password': password
    }
    response = session.post(url, data=data)
    bearer = 'Bearer ' + response.text
    print(f"DEBUG: Response for server (Login): {response.text}")
    return bearer
