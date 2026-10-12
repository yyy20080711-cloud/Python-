"""CrawlLab 练习脚本：批量下载照片墙里的图片。

用法：
    python3 examples/download_photos.py
"""

from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://127.0.0.1:8000"
PAGE_URL = urljoin(BASE_URL, "/photos.html")
SAVE_DIR = Path("downloads/photos")


def main() -> None:
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
    html = requests.get(PAGE_URL, timeout=15).text
    soup = BeautifulSoup(html, "html.parser")

    images = soup.select("img.crawl-image")
    print(f"找到 {len(images)} 张照片")

    for img in images:
        src = img.get("src")
        filename = img.get("data-filename") or Path(src).name
        url = urljoin(BASE_URL, src)
        dest = SAVE_DIR / filename
        print(f"下载 {url} -> {dest}")
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        dest.write_bytes(resp.content)

    print("完成")


if __name__ == "__main__":
    main()
