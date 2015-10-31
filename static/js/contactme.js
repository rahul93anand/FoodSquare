$(document).ready(function(){

$("#submit_contactme").click(function(){
var name = $("#name").val();
var email = $("#email").val();
var phone = $("#phone").val();
var message = $("#message").val();

        $.post("/contactme/",
        {
          name : name,
          email: email,
          phone: phone,
          message: message,
          csrfmiddlewaretoken : CSRF_TOKEN
        },
        function(data,status){
            alert("Data: " + data + "\nStatus: " + status);
        });



});

$("#register").click(function(){

window.location.href='/register_page';



});

});