document.getElementById("checkPage").addEventListener("click", myFunction);

var myMessage =document.getElementsByClassname("ingredient-list")[0].innerHTML;
chrome.extension.sendRequest({message: myMessage}, function(response){});

function myFunction() {
    chrome.tabs.executeScript(null, {file: "content_script.js"});
    document.getElementById("obtained--ing").innerHTML = myMessage;
    window.close();
}

chrome.extension.onRequest.addListener(
      function(request, sender, sendResponse) {
          if (request.message) {
          	document.getElementById("obtained-ing").innerHTML =request.myMessage;
          }
          sendResponse({});
      }
  );