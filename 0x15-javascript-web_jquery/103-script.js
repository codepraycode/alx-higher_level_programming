const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    showHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    // ENTER key is of keycode 13
    if (event.keyCode === 13) {
      showHello();
    }
  });
};

function showHello () {
  const lan = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
}
