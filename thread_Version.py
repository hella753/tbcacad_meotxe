import requests
import json
import threading

class ThreadVersion:
    def __init__(self, base_url):
        self.base_url = base_url
        self.lock = threading.Lock()
        self.init_file()

    @staticmethod
    def init_file():
        with open("data.json", "w") as start_file:
            json.dump([], start_file)

    def fetch_data(self, idx):
        url = f"{self.base_url}{idx}"
        response = requests.get(url)
        data = response.json()

        with self.lock:
            with open("data.json", "r") as outfile:
                data_list = json.load(outfile)

            data_list.append(data)

            with open("data.json", "w") as outfile:
                json.dump(data_list, outfile, indent=2)

    def run_threads(self):
        threads = []
        for i in range(1, 78):
            thread = threading.Thread(target=self.fetch_data, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()