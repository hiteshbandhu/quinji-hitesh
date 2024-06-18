document.addEventListener('DOMContentLoaded', function() {
    var scrapeButton = document.getElementById('scrapeButton');
  
    scrapeButton.addEventListener('click', function() {
      chrome.runtime.sendMessage({ message: 'popup_clicked' }, function(response) {
        if (chrome.runtime.lastError) {
          console.error(chrome.runtime.lastError.message);
          return;
        }
        console.log('Response from background.js:', response);
      });
    });
  });
  