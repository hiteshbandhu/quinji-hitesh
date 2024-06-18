chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.message === 'popup_clicked') {
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { message: 'scrape' }, function(response) {
          if (chrome.runtime.lastError) {
            console.error(chrome.runtime.lastError.message);
            return;
          }
          sendResponse(response);
        });
      });
      return true; // Indicates that sendResponse will be called asynchronously
    }
  });
  