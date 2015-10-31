$(document).ready(function(){



$("#submit_register").click(function(){
var name = $("#name").val();
var email = $("#email").val();
var phone = $("#phone").val();
var password = $("#pwd").val();

        $.post("/register",
        {
          name : name,
          email: email,
          phone: phone,
          password: password,
          csrfmiddlewaretoken : CSRF_TOKEN
        },
        function(data,status){
            alert("Data: " + data + "\nStatus: " + status);
        });








});


});