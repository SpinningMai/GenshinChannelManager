from gui import get_server_selection
from pdata import file_name_set
from utils import override_config_ini, edit_pcgamesdk_dll, start_game, get_file_group_id, ensure_shortcut


def main() -> None:
    # 启动GUI，供玩家选择启动项目
    user_selection = get_server_selection()
    if user_selection == {}:
        return

    # 定位选择的渠道 和 电脑文件夹名称类型
    server_id:int = user_selection["value"]
    name_set:dict = file_name_set[get_file_group_id()]

    # 复写config.ini和修改PCgameSDK.dll
    override_config_ini(server_id)
    edit_pcgamesdk_dll(server_id, name_set)
    ensure_shortcut(name_set)

    # 启动游戏
    if user_selection['autoStartGame']:
        start_game(name_set)

if __name__ == "__main__":
    import os
    main()

    # pyinstaller --onefile --noconsole --icon=C:\Users\im_mj\Documents\GitHub\GenshinChannelManager\assets\icon.ico GenshinChannelManager.py
    # pyinstaller GenshinChannelManager.spec