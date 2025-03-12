import configparser

import file_action
from gui import get_server_selection

channels = {
    1 : {"cps": "hyp_mihoyo", "channel": 1}, # 天空岛 + 米哈游通行证
    2 : {"cps": "bilibili", "channel": 14}, # 世界树 + BiliBili账号
}

def override(to_be_overrides:dict, section:str = "General") -> None:
    config_file_path = os.path.join(os.getcwd(), "config.ini")
    if not os.path.exists(config_file_path):
        file_action.download_config_ini(download_path=config_file_path)

    config = configparser.ConfigParser()
    config.read(config_file_path)

    for key, value in to_be_overrides.items():
        if section in config and key in config[section]:
            config.set(section, key, str(value))
        else:
            print(f"Error: '{key}' not exist in [{section}] 部分")

    with open(config_file_path, "w") as configfile:
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