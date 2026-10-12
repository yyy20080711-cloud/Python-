# CrawlLab

阿尧用来练习 Python 爬虫的本地测试站。页面里有稳定的 class / id / data-* 选择器，方便用浏览器 F12 对照元素后批量下载。

## 页面

- `/index.html` 首页与选择器提示
- `/photos.html` 12 张照片，选择器 `img.crawl-image`、`a.photo-download`
- `/videos.html` 5 个短视频，选择器 `video.crawl-video`、`a.video-download`
- `/audio.html` 9 段音频 + 资源表，选择器 `audio.crawl-audio`、`table.resource-table a`
- `/api/media.json` JSON 接口，适合练接口解析

## 本地启动

```bash
# 在仓库根目录启动静态服务
python3 -m http.server 8000
```

浏览器打开 `http://127.0.0.1:8000`。

## 练习脚本

```bash
# 安装依赖
pip install --break-system-packages requests beautifulsoup4

# 下载照片墙全部图片
python3 examples/download_photos.py
```

F12 复制选择器后，把 `soup.select("...")` 换成你选中的规则即可改抓视频或音频。

## 素材来源

- 照片：Picsum Photos
- 视频：MDN CC0 / MDN learning-area / SampleLib
- 音频：MDN CC0 与本地生成的 WAV

仅用于个人爬虫学习，勿拿去抓未授权的真实站点。
