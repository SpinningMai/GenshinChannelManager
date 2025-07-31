import configparser
import os
import subprocess
from win32com.client import Dispatch

import downloader
from pdata import channels, file_name_set
from pstruct import GameState


def override_config_ini(server_id:int, section:str = "General") -> None:
    """
    To override the config_ini file according to the server_id selected.
    :param server_id: the id of server/channel selected.
    :param section: part of content to edit
    """
    to_be_overrides = channels[server_id]

    config_file_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game", "config.ini")
    if not os.path.exists(config_file_path):
        downloader.download_config_ini(download_path=config_file_path)

    config = configparser.ConfigParser()
    config.read(config_file_path)

    for key, value in to_be_overrides.items():
        if section in config and key in config[section]:
            config.set(section, key, str(value))
        else:
            print(f"Error: '{key}' not exist in [{section}] 部分")

    with open(config_file_path, "w") as configfile:
        config.write(configfile)

def edit_pcgamesdk_dll(server_id:int, name_set:dict) -> None:
    """
    To enable or disable the PCgameSDK.dll according to the server_id selected.
    :param server_id: the id of server/channel selected.
    :param name_set: the string names of the local folders
    """
    pcgamesdk_dll_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game",
                                      name_set["_Data_folder"], "Plugins", "PCGameSDK.dll")
    pcgamesdk_dll_disabled_path = pcgamesdk_dll_path + ".disableddll"

    is_pcgamesdk_dll_exists = os.path.exists(pcgamesdk_dll_path)
    is_pcgamesdk_dll_disabled_exists = os.path.exists(pcgamesdk_dll_disabled_path)

    if (server_id == 1) and is_pcgamesdk_dll_exists:
            os.rename(pcgamesdk_dll_path, pcgamesdk_dll_disabled_path)

    elif server_id == 2:
        if not is_pcgamesdk_dll_exists:
            if is_pcgamesdk_dll_disabled_exists:
                os.rename(pcgamesdk_dll_disabled_path, pcgamesdk_dll_path)
            else:
                downloader.download_pcgamesdk_dll(download_path=pcgamesdk_dll_path)
    else:
        pass

def edit_sdk_pkg_version(server_id:int, name_set:dict) -> None:
    sdk_pkg_version_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game", "sdk_pkg_version")

    is_sdk_pkg_version_exists = os.path.exists(sdk_pkg_version_path)

    if (server_id == 1) and is_sdk_pkg_version_exists:
        pass

    elif server_id == 2:
        if not is_sdk_pkg_version_exists:
            downloader.download_sdk_pkg_version(download_path=sdk_pkg_version_path)
    else:
        pass

def edit_blplatform64_zip(server_id:int, name_set:dict) -> None:
    blplatform64_folder_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game",
                                      name_set["_Data_folder"], "Plugins")

    is_blplatform64_folder_exists = os.path.exists(os.path.join(blplatform64_folder_path, "BLPlatform64"))

    if (server_id == 1) and is_blplatform64_folder_exists:
        pass

    elif server_id == 2:
        if not is_blplatform64_folder_exists:
            downloader.download_and_extract_BLPlatform64_zip(download_path=blplatform64_folder_path)
    else:
        pass

def ensure_shortcut(name_set:dict) -> None:
    """
    To ensure that the shortcut of game.exe exists.
    :param name_set: the string names of the local folders
    """
    shortcut_path = os.path.join(os.getcwd(), name_set["game.exe.lnk"])

    if os.path.exists(shortcut_path):
        return
    else:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        game_exe_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game", name_set["game.exe"])
        shortcut.Targetpath = game_exe_path
        shortcut.WorkingDirectory = os.path.dirname(game_exe_path)
        shortcut.save()

def start_game(name_set:dict) -> None:
    """
    To start the game after the program has finished.
    :param name_set: the string names of the local folders
    """
    exe_path = os.path.join(os.getcwd(), name_set["game.exe.lnk"])
    if os.path.exists(exe_path):
        subprocess.Popen(exe_path, shell=True)
    else:
        raise FileNotFoundError(f"未找到 {name_set["game.exe"]}，请检查文件是否存在于当前目录。或请把此执行文件exe放在与游戏启动器exe相同目录下。")


def get_file_group_id() -> int:
    """
    To check and return the proper id of file_group_set
    :return: the file group id
    """
    file_group_id = 0
    while True:
        check_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game",
                                  file_name_set[file_group_id]["_Data_folder"])
        if os.path.exists(check_path):
            break
        elif file_group_id > 2:
            raise EOFError("Unknown Type Of Launcher")
        file_group_id += 1
    return file_group_id

def get_server_id() -> int:

    config_file_path = os.path.join(os.getcwd(), "games", "Genshin Impact Game", "config.ini")
    if not os.path.exists(config_file_path):
        downloader.download_config_ini(download_path=config_file_path)

    config = configparser.ConfigParser()
    config.read(config_file_path)

    s = config.get("General", 'cps')

    if s == channels[1]["cps"]:
        return 0
    else:
        return 1

def get_current_state() -> GameState:
    current_state = GameState()
    current_state.channel_idx = get_server_id()
    current_state.file_name_set_idx = get_file_group_id()
    return current_state