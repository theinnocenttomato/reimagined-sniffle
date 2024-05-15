const slider = document.getElementById("statamount");
const output = document.getElementById("statamount_output");

slider.oninput = function() {
  output.innerHTML = this.value;
  const value = (this.value - this.min) / (this.max - this.min) * 100;
};
