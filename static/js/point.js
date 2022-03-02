$( document ).ready(function() {
    alert("fds");
});

function show_d1() {
    $('#d1').show()
    $('#d2').hide()
    $('#d3').hide()
    $('#d4').hide()
}

function show_d2() {
    $('#d1').hide()
    $('#d2').show()
    $('#d3').hide()
    $('#d4').hide()
}

function show_d3() {
    $('#d1').hide()
    $('#d2').hide()
    $('#d3').show()
    $('#d4').hide()
}

function show_d4() {
    $('#d1').hide()
    $('#d2').hide()
    $('#d3').hide()
    $('#d4').show()
}

