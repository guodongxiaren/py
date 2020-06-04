# zhihu
知乎个人数据爬取

## curl测试
新的知乎好像有反扒功能。云主机可能失败。MacBook可以。
```
curl https://www.zhihu.com/api/v4/members/guodongxiaren?include=follower_count%2cvoteu
```
## MAC系统定时任务
```
sudo cp *.plist /Library/LaunchDaemons/
cd /Library/LaunchDaemons
launchctl load -w com.zhihu.run.plist
launchctl start -w com.zhihu.run.plist
launchctl load -w com.zhihu.commit.plist
launchctl start -w com.zhihu.run.plist
```
