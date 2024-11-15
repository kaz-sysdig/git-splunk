import requests
import yaml
import json

# Apply your settings here
splunk_host = "<Your Splunk IP address>"
hec_token = "<Your HEC Token>"
index = "<Your Index>"
sourcetype = "_json"

# GitHub URL to the raw YAML file
url = "https://raw.githubusercontent.com/kaz-sysdig/git-splunk/main/ns_owner.yaml"

# Fetch the YAML file from GitHub
response = requests.get(url)
yaml_data = response.text

# Convert YAML to JSON
yaml_dict = yaml.safe_load(yaml_data)
json_data = json.dumps(yaml_dict)

# HEC URL
hec_url = f"https://{splunk_host}:8088/services/collector"

# Create the payload
payload = {
    "event": json_data,
    "sourcetype": sourcetype,
    "index": index
}

# Send the data to Splunk HEC
headers = {
    "Authorization": f"Splunk {hec_token}",
    "Content-Type": "application/json"
}
response = requests.post(hec_url, json=payload, headers=headers, verify=False)

# Print the response
print(response.status_code)
print(response.text)
