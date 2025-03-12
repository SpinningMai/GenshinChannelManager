import configparser
from gui import get_server_selection

channels = {
    1 : {"cps": "hyp_mihoyo", "channel": 1}, # 天空岛 + 米哈游通行证
    2 : {"cps": "bilibili", "channel": 14}, # 世界树 + BiliBili账号
}

def override(to_be_overrides:dict, section:str = "General") -> None:
    config_file = os.path.join(os.getcwd(), "config.ini")
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        print("Error: config.ini not exists!")  # TODO: download one from github
        exit()
    config.read(config_file)

    for key, value in to_be_overrides.items():
        if section in config and key in config[section]:
            config.set(section, key, str(value))
        else:
            print(f"Error: '{key}' not exist in [{section}] 部分")

    with open(config_file, "w") as configfile:
        config.write(configfile)


def start_game():
    pass


def main() -> None:
    user_selection = get_server_selection()
    if user_selection == {}:
        return

    override(channels[user_selection["value"]])

    start_game()

if __name__ == "__main__":
    import os
    main()