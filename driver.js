// defining global variables
var url;
var start;
var end;
var time;
// on focus trigger for tab
window.onfocus = function()
{
  url = window.location.origin;
  start = Math.floor(Date.now()/ 1000);
};

window.onblur = function()
{
  end = Math.floor(Date.now()/ 1000);
  time = end - start;
};
