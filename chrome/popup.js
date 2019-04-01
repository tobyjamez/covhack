var listel = ["butter","sugar","eggs","vanilla extract","plain flour","regular cocoa powder","bicarbonate of soda","baking powder","buttermilk","red food colouring gel","butter","cream cheese","icing sugar"];

document.addEventListener('DOMContentLoaded', function() {

  var checkPageButton = document.getElementById('checkPage');

  checkPageButton.addEventListener('click', function() {
    chrome.tabs.query({active:true,currentWindow: true}, function(tabs){
      chrome.tabs.sendMessage(tabs[0].id, {todo: "allIngredients", clickedColor: "true" });
    });
/*
    d = document;
    var u = document.getElementById("obtained-ing");
    var url = "https://phrijj.herokuapp.com/add";
    for (var i = 0; i < listel.length; i++) {
    	var b = document.createElement('li');
    	b.innerHTML=listel[i];
    	u.append(b);
    	var params = "{name:"+listel[i]+"}";
	    var xhr = new XMLHttpRequest();
	    xhr.open("POST", url, true);
		//Send the proper header information along with the request
		//xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

		xhr.send(params);
      }

      */
  }, false);



}, false);