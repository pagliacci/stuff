alert(1);

var btn = document.createElement("BUTTON");        // Create a <button> element
var t = document.createTextNode("CLICK ME");       // Create a text node
var x = document.getElementsByClassName("blueBtn payBlueBtn")[0];
btn.appendChild(t);                                // Append the text to <button>
document.body.insertBefore(btn, x);
