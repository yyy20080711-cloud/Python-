# CrawlLab

阿尧用来练习 Python 爬虫的本地测试站。页面里有稳定的 class / id / data-* 选择器，方便用浏览器 F12 对照元素后批量下载。

## 页面

- `/index.html` 首页与选择器提示
- `/photos.html` 12 张照片，选择器 `img.crawl-image`、`a.photo-download`
- `/videos.html` 5 个短视频，选择器 `video.crawl-video`、`a.video-download`
- `/audio.html` 9 段音频 + 资源表，选择器 `audio.crawl-audio`、`table.resource-table a`
- `/api/media.json` JSON 接口，适合练接口解析

## GitHub Pages 访问

仓库已推到 `main`。当前环境没有开启 Pages 的管理员权限，需要你在 GitHub 网页上点一次：

1. 打开 https://github.com/yyy20080711-cloud/Python-/settings/pages
2. Source 选 `Deploy from a branch`
3. Branch 选 `main`，目录选 `/ (root)`
4. 点 Save

几分钟后打开：

https://yyy20080711-cloud.github.io/Python-/

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
