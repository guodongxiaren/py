// 监听来自内容脚本的消息
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  if (message.action === 'download') {
    // 提取图片 URL 和文章标题
    var cdn_url = message.cdn_url;
    var title = message.title;

    console.log('CDN URL:', cdn_url);
    console.log('Title:', title);

    // 下载图片
    chrome.downloads.download({ url: cdn_url, filename: title + '.jpg' });
  }
});

// 监听用户点击插件按钮的事件
chrome.action.onClicked.addListener(function(tab) {
  // 向当前选项卡发送消息，请求执行下载插件的逻辑
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: function() {
      // 向内容脚本发送消息，请求提取图片 URL 和文章标题
      chrome.runtime.sendMessage({ action: 'extract' });
    }
  });
});
