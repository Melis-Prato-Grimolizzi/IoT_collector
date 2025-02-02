import SessionHTTP as Http
import configparser

config = configparser.ConfigParser()


def userExist():
    session = Http.getSession()
    check_user_url = config['Urls']['CheckCollector']
    response = session.get(check_user_url)
    print(f"DEBUG: Response for server (Get user): {response.text}")
    if response.status_code == 200:
        return True
    return False


def createCollector():
    session = Http.getSession()
    create_collector_url = config['Urls']['CreateCollector']
    username = config['User']['username']
    password = config['User']['password']
    body = {
        'username': username,
        'password': password
    }
    response = session.post(create_collector_url, data=body)
    print(f"DEBUG: Response for server (Create user): {response.text}")


def collectorLogin():
    session = Http.getSession()
    login_collector_url = config['Urls']['LoginCollector']
    username = config['User']['username']
    password = config['User']['password']
    data = {
        'username': username,
        'password': password
    }
    response = session.post(login_collector_url, data=data)
    bearer = 'Bearer ' + response.text
    print(f"DEBUG: Response for server (Login): {response.text}")
    return bearer
