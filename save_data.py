import json

DATA_PATH = "persistent/"

def get_user_total_messages(user):
    stat_dict = read_all("statistics.json")
    return stat_dict[user]

def update_msgs_sent(user):
    stat_dict = read_all("statistics.json")
    stat_dict[user] += 1
    write(stat_dict, "statistics.json")
    return stat_dict[user]

def write(dict_obj, file):
    with open(DATA_PATH+file, 'w') as f:
        json_string = json.dumps(dict_obj)
        f.write(json_string)
        f.close()

def read_all(file):
    with open(DATA_PATH+file, 'r') as f:
        raw = f.read()
        json_obj = json.loads(raw)
        return json_obj
        f.close()