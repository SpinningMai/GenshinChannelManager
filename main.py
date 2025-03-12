import configparser

import file_action
from gui import get_server_selection

channels = {
    1 : {"cps": "hyp_mihoyo", "channel": 1}, # 天空岛 + 米哈游通行证
    2 : {"cps": "bilibili", "channel": 14}, # 世界树 + BiliBili账号
}

def override_config_ini(param:int, section:str = "General") -> None:
    to_be_overrides = channels[param]

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


def override_pcgamesdk_dll(param) -> None:
    pcgamesdk_dll_path = os.path.join(os.getcwd(), "YuanShen_Data", "Plugins", "PCGameSDK.dll")
    pcgamesdk_dll_disabled_path = pcgamesdk_dll_path + ".disableddll"

    is_pcgamesdk_dll_exists = os.path.exists(pcgamesdk_dll_path)
    is_pcgamesdk_dll_disabled_exists = os.path.exists(pcgamesdk_dll_disabled_path)

    if param == 1 and is_pcgamesdk_dll_exists:
            os.rename(pcgamesdk_dll_path, pcgamesdk_dll_disabled_path)

    elif param == 2:
        if not is_pcgamesdk_dll_exists:
            if is_pcgamesdk_dll_disabled_exists:
                os.rename(pcgamesdk_dll_disabled_path, pcgamesdk_dll_path)
            else:
                file_action.download_pcgamesdk_dll(download_path=pcgamesdk_dll_path)
    else:
        pass



def start_game():
    pass

def main() -> None:
    user_selection = get_server_selection()
    if user_selection == {}:
        return

    value_selected = user_selection["value"]
    override_config_ini(value_selected)
    override_pcgamesdk_dll(value_selected)

    start_game()

if __name__ == "__main__":
    import os
    main()