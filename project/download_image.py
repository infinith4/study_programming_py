import requests
import os
import sys

# 画像をダウンロードする
def download_image(url, timeout = 10):
    response = requests.get(url, allow_redirects=False, timeout=timeout)
    if response.status_code != 200:
        e = Exception("HTTP status: " + response.status_code)
        raise e

    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e

    return response.content

# 画像のファイル名を決める
def make_filename(base_dir, number, url):
    ext = os.path.splitext(url)[1] # 拡張子を取得
    filename = number + ext        # 番号に拡張子をつけてファイル名にする

    fullpath = os.path.join(base_dir, filename)
    return fullpath

# 画像を保存する
def save_image(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)

if __name__ == "__main__":
    image_url: str = "https://avatars3.githubusercontent.com/u/43472251?s=460&u=a62d5ea06cffd1acdbc0cdc997f468cd858d13b4&v=4"
    urls_txt = "input.txt"
    images_dir = "images"
    filename = "image.png"
    try:
        image = download_image(image_url)
        save_image(filename, image)
    except Exception as err:
        print(f"{err}")