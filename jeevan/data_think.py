import requests

CONTEST_ID = 653099  # replace this

# Step 1: get standings
url = f"https://codeforces.com/api/contest.standings?contestId={CONTEST_ID}&from=1&count=100000"
data = requests.get(url).json()

handles = set()
for row in data["result"]["rows"]:
    for member in row["party"]["members"]:
        handles.add(member["handle"])

# Step 2: get user info
handles_str = ";".join(handles)
info_url = f"https://codeforces.com/api/user.info?handles={handles_str}"
users = requests.get(info_url).json()["result"]

# Step 3: print real names
for user in users:
    first = user.get("firstName", "")
    last = user.get("lastName", "")
    name = (first + " " + last).strip()
    if not name:
        name = "Not provided"
    print(f"{user['handle']} → {name}")