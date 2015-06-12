$(function() {
  $("#myform").submit(function(ev) {
    ev.preventDefault();
    action = $(this).attr("action");
    method = $(this).attr("method");

    $.ajax({
      url: action,
      type: method,
      data: $("#myform").serialize(),
      success: function(data) {
        data = JSON.parse(data);
        url = "http://" + window.location.host + "/" + data["slug"];
        $("#result").html("<a href=\"" + url + "\">" + url + "</a>");
      }
    });
  })
});
