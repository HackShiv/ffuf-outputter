import json

CYAN = '\033[96m'
END_COLOR = '\033[0m'

with open(r'/home/hackershiv/ffuf.json', 'r') as file:
    #json_data = file.read()
    #print(json_data)
    final_data = json.load(file)

data = final_data['results']

with open('ffuf.txt', 'w') as outfile:
    for item in data:
        url = item['url']
        status_code = item['status']
        print(f"{url} - {CYAN}{status_code}{END_COLOR}")
        outfile.write(f"{url} - {status_code}\n")
