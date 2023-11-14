import json
from typing import NoReturn


def replace_space(text: str):
    return text.replace('_', ' ')

def remove_key_from_json(key):
    key = replace_space(key)
    with open('./json_files/commands.json', 'r') as file:
        data = json.load(file)
    if key in data:
        del data[key]
    with open('./json_files/commands.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_key_value_to_json(key, value):
    key, value = replace_space(key), value.replace(' ', '_')
    with open('./json_files/commands.json', 'r') as file:
        data = json.load(file)
    data[key] = value
    with open('./json_files/commands.json', 'w') as file:
        json.dump(data, file, indent=4)

def json_save_one(value_name, key_name: str) -> NoReturn:
    with open('./json_files/ppid.json', encoding='utf-8') as file_json:
        data = json.load(file_json)
    data[key_name] = value_name
    with open('./json_files/ppid.json', 'w', encoding='utf-8') as file_json:
        json.dump(data, file_json, indent=4, ensure_ascii=False)

def json_upload_key(key_name: str) -> list:
    with open('./json_files/ppid.json', encoding='utf-8') as file_json:
        data = json.load(file_json)
    return data[key_name]

def read_json() -> dict:
    with open('./json_files/commands.json', 'r') as file:
        data = json.load(file)
    return data
