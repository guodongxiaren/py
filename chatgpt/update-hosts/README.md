## prompt
```
在Mac上使用python启动一个http服务。这个服务接受两个GET参数，一个是domain，一个是ip。该服务收到这两个参数后，把它更新到本地的host文件中，使Mac可以通过这个domain来访问这个ip。如果这个domain在hosts中已经存在则要先删除，然后再更新 
```
gpt-3.5-turbo生成python脚本

## Mac上启动该脚本
```
sudo nohup python3 update-hosts.py &
```
假设Mac本机IP是192.168.1.195

## Ubuntu上
在Ubuntu上配置开机自动执行如下指令。来注册自己的ip
```
curl http://192.168.1.195:8080\?domain\=guodong.dev\&ip\=`hostname -i|awk '{print $1}'`
```
