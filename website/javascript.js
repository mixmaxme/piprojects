var slider_red = document.getElementById("color_r");
var output_red = document.getElementById("r_value");
var field_red = document.getElementById("rwert");
output_red.innerHTML = slider_red.value;
field_red.innerHTML = slider_red.value;
document.getElementById('rwert').value=slider_red.value

var slider_green = document.getElementById("color_g");
var output_green = document.getElementById("g_value");
var field_green = document.getElementById("gwert");
output_green.innerHTML = slider_green.value;  
field_green.innerHTML = slider_green.value;
document.getElementById('gwert').value=slider_green.value
  
var slider_blue = document.getElementById("color_b");
var output_blue = document.getElementById("b_value");
var field_blue = document.getElementById("bwert");
output_blue.innerHTML = slider_blue.value;  
field_blue.innerHTML = slider_blue.value;
document.getElementById('bwert').value=slider_blue.value;
  
var slider_bright = document.getElementById("brightness");
var output_bright = document.getElementById("bright_value");
var field_bright = document.getElementById("hwert");
output_bright.innerHTML = slider_bright.value;  
field_bright.innerHTML = slider_bright.value;
document.getElementById('hwert').value=slider_bright.value;

var slider_bright_2 = document.getElementById("brightness_2");
var output_bright_2 = document.getElementById("bright_value_all");
var field_bright_2 = document.getElementById("awert");
output_bright_2.innerHTML = slider_bright_2.value;  
field_bright_2.innerHTML = slider_bright_2.value;  
document.getElementById('awert').value=slider_bright_2.value;

var slider = document.getElementById("velocity");
var output = document.getElementById("v_value");
var field = document.getElementById("vwert");
output.innerHTML = slider.value;
field.innerHTML = slider.value;
document.getElementById('vwert').value=slider.value;

slider_red.oninput = function() {
  output_red.innerHTML = this.value;
  document.getElementById('rwert').value=slider_red.value;
  document.cookie = "redvalue=" + slider_red.value;
}
slider_green.oninput = function() {
  output_green.innerHTML = this.value;
  document.getElementById('gwert').value=slider_green.value;
  document.cookie = "greenvalue=" + slider_green.value;
}
slider_blue.oninput = function() {
  output_blue.innerHTML = this.value;
  document.getElementById('bwert').value=slider_blue.value;
}
slider_bright.oninput = function() {
  output_bright.innerHTML = this.value;
  document.getElementById('hwert').value=slider_bright.value;
}
slider_bright_2.oninput = function() {
  output_bright_2.innerHTML = this.value;
  document.getElementById('awert').value=slider_bright_2.value;
}
slider.oninput = function() {
  output.innerHTML = this.value;
  document.getElementById('vwert').value=slider.value;
}

function changeColor() {
  let red = document.getElementById('color_r').value;
  let green = document.getElementById('color_g').value;
  let blue = document.getElementById('color_b').value;
  let color = 'rgb(' + red + ',' + green + ',' + blue + ')';
  document.body.style.backgroundColor = color;
}

document.getElementById('color_r').addEventListener('input',changeColor);
document.getElementById('color_g').addEventListener('input',changeColor);
document.getElementById('color_b').addEventListener('input',changeColor);


var redvalue = document.cookie;
document.getElementById('color_r')=redvalue.value;