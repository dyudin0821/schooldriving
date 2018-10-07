// document.addEventListener('DOMContentLoaded', function (evt) {
//     // $(".alert").hide();
//
// });
$('#add-order').submit(function (event) {
    event.preventDefault();
    var form = this;

    $.ajax({
        url: $(this).attr('action'),
        type: "POST",
        data: $(form).serialize(),
        success: function (response) {

            form.reset();
            $(".alert").slideDown();
            setTimeout(function () {
                $(".alert").slideUp();
            }, 3000);


        },
        error: function (response) {
            console.log(response);
            // bootbox.alert('Error, server cant be appended')
            // alert(response.responseJSON.error);
        },
    });

});