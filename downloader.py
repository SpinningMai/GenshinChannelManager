import os
import zipfile
import requests
import shutil
from urllib.parse import urlparse
from requests import RequestException

GITHUB_config_ini_URL = "https://cdn.jsdelivr.net/gh/SpinningMai/GenshinChannelManager@main/assets/config.ini"
GITHUB_PCGameSDK_dll_URL = "https://cdn.jsdelivr.net/gh/SpinningMai/GenshinChannelManager@main/assets/PCGameSDK.dll"
GITHUB_sdk_pkg_version_URL = "https://cdn.jsdelivr.net/gh/SpinningMai/GenshinChannelManager@main/assets/sdk_pkg_version"
GITHUB_BLPlatform64_zip_URL = "https://cdn.jsdelivr.net/gh/SpinningMai/GenshinChannelManager@main/assets/BLPlatform64.zip"

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
    download_file(GITHUB_sdk_pkg_version_URL, download_path)

def download_and_extract_BLPlatform64_zip(download_path: str):

    # 临时ZIP文件路径
    temp_zip = os.path.join(download_path, "temp_repo.zip")

    try:
        response = requests.get(GITHUB_BLPlatform64_zip_URL, stream=True)
        response.raise_for_status()

        with open(temp_zip, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # 解压ZIP文件
        with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
            # 解压所有文件（会自动创建子目录）
            zip_ref.extractall(download_path)

            # GitHub的ZIP包会包含"repo-main"这样的顶层目录，可以移动文件
            # extracted_dir = os.path.join(download_path, f"{repo}-main")
            # if os.path.exists(extracted_dir):
            #     for item in os.listdir(extracted_dir):
            #         shutil.move(os.path.join(extracted_dir, item), download_path)
            #     os.rmdir(extracted_dir)

    finally:
        if os.path.exists(temp_zip):
            os.remove(temp_zip)