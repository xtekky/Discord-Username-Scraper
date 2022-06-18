import os, requests, random, time

class Scraper:
    
    def __init__(self, channel_id, token, amount):
        self.token      = token
        self.channel_id = channel_id
        self.usernames  = []
        self.amount     = amount
        self.params     = {
                            'limit': 100,
                        }

    def get_usernames(self):
        while len(self.usernames) < self.amount:
            req = requests.get(
                url = f'https://discord.com/api/v9/channels/{self.channel_id}/messages', 
                params = self.params, 
                headers = {
                    'authority': 'discord.com',
                    'accept': '*/*',
                    'authorization': f"{self.token}",
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL21lZTYueHl6LyIsInJlZmVycmluZ19kb21haW4iOiJtZWU2Lnh5eiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzI4MzEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                }
            )
            
            for message in req.json():
                username = message['author']['username']
                if username not in self.usernames:
                    self.usernames.append(username)
                    print(username, len(self.usernames))

            self.params = {
                    'before': req.json()[-1]['id'],
                    'limit': 100
                }

        for username in self.usernames:
            try:
                if '�' not in username:
                    print(username, file = open('./usernames.txt', 'a'))
            except UnicodeEncodeError:
                pass

if __name__ == "__main__":
    scrapy = Scraper(
        channel_id = 'CHANNEL OF SERVER',
        token      = 'TOKEN IN SERVER',
        amount     = 1000 #amount of usernames to scrape
    )
    scrapy.get_usernames()
