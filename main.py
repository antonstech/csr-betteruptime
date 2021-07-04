import requests
import configparser
import shutil

config = configparser.ConfigParser()
config.read("config/config.ini")

heartbeaturl = config["Webhook-Ping"]["url"]
api_token = config["API-Stuff"]["token"]
server_name = config["Device-Info"]["name"]
heartbeatid = config["API-Stuff"]["id"]
heartbeat_api = config["API-Stuff"]["heartbeat_url"]
stupdateurl = config["API-Stuff"]["statuspage_url"]
statuspage_id = config["API-Stuff"]["statuspage_id"]
resource_id = config["API-Stuff"]["resource_id"]

requests.get(heartbeaturl)

full_url = heartbeat_api + str(heartbeatid)
get_free_space = shutil.disk_usage("/")[2]
free_space = ("%d GB Frei" % (get_free_space // (2 ** 30)))
data = {"name" : f"{server_name} ({free_space})"}
headers = {"Authorization": f"Bearer {api_token}"}
response = requests.patch(full_url, data=data, headers=headers).json()
status_page_update_url = stupdateurl + statuspage_id + "/resources/" + resource_id
data = {"public_name" : f"{server_name} ({free_space})"}
response2 = requests.patch(status_page_update_url, data=data, headers=headers).json()


