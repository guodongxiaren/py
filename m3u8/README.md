非加密m3u8视频下载
=======
下载完的ts文件直接合并成mp4可能卡顿，可以先合并成ffmpeg，再转码成mp4。
另外直接用cat命令合并效果并不理想，还推荐ffmpeg
```
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mkv
ffmpeg -i output.mkv output.mp4
```
list.txt内容为所有ts文件，格式如下：
```
file 000.ts
file 001.ts
file 002.ts
```
