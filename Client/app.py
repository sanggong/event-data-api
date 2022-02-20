from app.client import Client
from config import SERVER_URL

def main():
    print('Client Start....')
    client = Client(SERVER_URL)
    client.run()


if __name__=='__main__':
    main()