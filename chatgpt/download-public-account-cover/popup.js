// 监听用户点击下载按钮的事件
document.getElementById('download-button').addEventListener('click', function() {
  // 向当前选项卡发送消息，请求执行下载插件的逻辑
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'download' });
  });
});
