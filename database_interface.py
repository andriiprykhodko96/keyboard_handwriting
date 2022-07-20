from json import load, dump

def read_json(filename):
    file = open(filename, "r")
    data = load(file)
    file.close()
    return data

def write_json(filename, data):
    file = open(filename, "w")
    dump(data, file, indent=4, separators=(",", ": "))
    file.close()

def check_user(user):
    data = read_json("users.json")
    return user in data

def get_user(user):
    data = read_json("users.json")
    return (data[user]["M"], data["user"]["D"])

def set_user(user, M, D):
    data = read_json("users.json")
    data[user] = {"M": M, "D": D}
    write_json("users.json", data)