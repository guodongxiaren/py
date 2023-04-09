```
在Mac上使用python启动一个http服务。这个服务接受两个GET参数，一个是domain，一个是ip。该服务收到这两个参数后，把它更新到本地的host文件中，使Mac可以通过这个domain来访问这个ip。如果这个domain在hosts中已经存在则要先删除，然后再更新 
```
gpt-3.5-turbo
