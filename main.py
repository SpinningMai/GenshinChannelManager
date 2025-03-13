import configparser
import subprocess

import file_action
from gui import get_server_selection

channels = {
    1 : {"cps": "hyp_mihoyo", "channel": 1, "sub_channel": 0,
         "uapc": '{"hk4e_cn":{"uapc":""},"hyp":{"uapc":""}}'}, # 天空岛 + 米哈游通行证
    2 : {"cps": "bilibili", "channel": 14, "sub_channel": 1,
         "uapc": '{"hk4e_cn":{"uapc":""},"hyp":{"uapc":""}}'}, # 世界树 + BiliBili账号
    3 : {"cps": "hoyoverse", "channel": 1, "sub_channel": 0,
         "uapc": '{"hk4e_global":{"uapc":"f8a4a729f5bd_"},"hyp":{"uapc":"f8a4a729f5bd_"}}'}, # TW/HK/MO + HoYoverse通行证
}

file_name_set ={
    0 : {"_Data_folder": "YuanShen_Data", "game.exe": "YuanShen.exe"},
    1 : {"_Data_folder": "GenshinImpact_Data", "game.exe": "GenshinImpact.exe"},
}

def override_config_ini(param:int, section:str = "General") -> None:
    to_be_overrides = channels[param]

    config_file_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game", "config.ini")
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


def override_pcgamesdk_dll(param, name_set) -> None:
    pcgamesdk_dll_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game",
                                      name_set["_Data_folder"], "Plugins", "PCGameSDK.dll")
    pcgamesdk_dll_disabled_path = pcgamesdk_dll_path + ".disableddll"

    is_pcgamesdk_dll_exists = os.path.exists(pcgamesdk_dll_path)
    is_pcgamesdk_dll_disabled_exists = os.path.exists(pcgamesdk_dll_disabled_path)

    if (param == 1 or param == 3) and is_pcgamesdk_dll_exists:
            os.rename(pcgamesdk_dll_path, pcgamesdk_dll_disabled_path)

    elif param == 2:
        if not is_pcgamesdk_dll_exists:
            if is_pcgamesdk_dll_disabled_exists:
                os.rename(pcgamesdk_dll_disabled_path, pcgamesdk_dll_path)
            else:
                file_action.download_pcgamesdk_dll(download_path=pcgamesdk_dll_path)
    else:
        pass


def start_game(name_set):
    game_name = name_set["game.exe"]
    exe_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game", game_name)
    if os.path.exists(exe_path):
        subprocess.Popen(exe_path, shell=True)
    else:
        raise FileNotFoundError(f"未找到 {game_name}，请检查文件是否存在于当前目录。或请把此执行文件exe放在与游戏启动器exe相同目录下。")


def main() -> None:
    user_selection = get_server_selection()
    if user_selection == {}:
        return

    server_selected = user_selection["value"]
    file_group_num = 0
    while True:
        check_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game",
                                  file_name_set[file_group_num]["_Data_folder"])
        if os.path.exists(check_path):
            break
        elif file_group_num > 2:
            raise EOFError("Unknown Type Of Launcher")
        file_group_num += 1

    override_config_ini(server_selected)
    override_pcgamesdk_dll(server_selected, file_name_set[file_group_num])

    if user_selection['autoStartGame']:
        start_game(file_name_set[file_group_num])

if __name__ == "__main__":
    import os
    main()

    # pyinstaller --onefile --noconsole main.py
    # pyinstaller main.spec