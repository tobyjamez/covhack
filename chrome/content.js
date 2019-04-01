//https://firebase.googleblog.com/2013/03/power-your-chrome-extension-with.html
//Use above on next update

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse){
    if (request.todo == "allIngredients"){
    	var s = document.getElementsByClassName("ingredients-list__item");
		Array.from(s).forEach((el) => {
		    // Do stuff here
		    console.log(el.textContent);
		});
    }
});