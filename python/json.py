import json

# 讀檔案
def read_json(path):
    with open(path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    return data
# 寫檔案
def save_json(path, dc={})
with open(path, "w", encoding="utf-8") as json_file:
    json.dump(dc, json_file)
