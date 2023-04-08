// 监听页面加载完成的事件
window.addEventListener('load', function() {
  // 提取图片 URL 和文章标题
  var scripts = document.querySelectorAll('script');
  var cdn_url = '';
  var title = '';
  for (var i = 0; i < scripts.length; i++) {
    var script = scripts[i];
    if (script.textContent.indexOf('var cdn_url_235_1 = "') >= 0) {
      cdn_url = script.textContent.match(/var cdn_url_235_1 = "([^"]+)";/)[1];
    }
    if (script.textContent.indexOf('var msg_title') >= 0) {
      title = script.textContent.match(/var msg_title = '([^']+)'\.html\(false\);/)[1];
    }
  }

  // 向后台脚本发送消息，将图片 URL 和文章标题传递给后台脚本
  chrome.runtime.sendMessage({ action: 'download', cdn_url: cdn_url, title: title });
});
