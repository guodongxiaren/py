# zhihu
知乎个人数据爬取

## curl测试
新的知乎好像有IP反扒功能。如果接口请求失败，请修改一下源IP。
```
curl --header "X-Forwarded-For: 1.2.3.4" https://www.zhihu.com/api/v4/members/guodongxiaren?include=follower_count%2cvoteu
```
修改1.2.3.4为一个其他的真实IP。
