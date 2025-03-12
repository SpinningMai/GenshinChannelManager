import configparser
import os

from gui import get_server_selection



section = "General"
channels = {
    1 : {("cps", "hyp_mihoyo"), ("channel", 1), ("_name_", "天空岛 + 米哈游通行证")},
    2 : {("cps", "bilibili"), ("channel", 14), ("_name_", "天空岛 + 米哈游通行证")},
}

def main():
    user_config = get_server_selection()
    if user_config == {}:
        return
    config_file = os.path.join(os.getcwd(), "config.ini")
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        print("Error: config.ini not exists!")
        exit()
    config.read(config_file)

    # if section in config and key in config[section]:
    #     current_value = config.getint(section, key)
    #     new_value = 1 if current_value == 14 else 14
    #     config.set(section, key, str(new_value))
    #
    #     with open(config_file, "w") as configfile:
    #         config.write(configfile)
    #
    #     print(f"已将 {key} 值修改为: {new_value}")
    # else:
    #     print(f"Error: '{key}' 不存在于 [{section}] 部分")

if __name__ == "__main__":
    main()