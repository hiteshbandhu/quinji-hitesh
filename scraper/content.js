chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.message === 'scrape') {
      var sourceCode = document.documentElement.outerHTML;
      sendResponse({ sourceCode: sourceCode });
    }
  });
  