import requests

GITHUB_config_ini_URL = "https://raw.githubusercontent.com/SpinningMai/GenshinChannelManager/main/assets/config.ini"
GITHUB_PCGameSDK_dll_URL = "https://raw.githubusercontent.com/SpinningMai/GenshinChannelManager/main/assets/PCGameSDK.dll"

def download_file(url:str, download_path:str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(download_path, "wb") as file:
            file.write(response.content)

    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
        exit(1)

def download_config_ini(download_path:str) -> None:
    download_file(GITHUB_config_ini_URL, download_path)

def download_pcgamesdk_dll(download_path:str) -> None:
    download_file(GITHUB_PCGameSDK_dll_URL, download_path)