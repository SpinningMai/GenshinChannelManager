import requests

from requests import RequestException

GITHUB_config_ini_URL = "https://cdn.jsdelivr.net/gh/SpinningMai/GenshinChannelManager@main/assets/config.ini"
GITHUB_PCGameSDK_dll_URL = "https://cdn.jsdelivr.net/gh/SpinningMai/GenshinChannelManager@main/assets/PCGameSDK.dll"
GITHUB_sdk_pkg_version = "https://cdn.jsdelivr.net/gh/SpinningMai/GenshinChannelManager@main/assets/sdk_pkg_version"

def download_file(url:str, download_path:str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(download_path, "wb") as file:
            file.write(response.content)

    except requests.exceptions.RequestException as e:
        raise RequestException(f"下载失败，请稍后重试: {e}")

def download_config_ini(download_path:str) -> None:
    download_file(GITHUB_config_ini_URL, download_path)

def download_pcgamesdk_dll(download_path:str) -> None:
    download_file(GITHUB_PCGameSDK_dll_URL, download_path)

def download_sdk_pkg_version(download_path:str) -> None:
    download_file(GITHUB_sdk_pkg_version, download_path)