// -
function expand() {
  $(".search_form").toggleClass("close");
  $(".input_form").toggleClass("square");
  if ($('.search_form').hasClass('close')) {
    $('input_form').focus();
  } else {
    $('input_form').blur();
  }
}
$('button').on('click', expand);

copyright('');