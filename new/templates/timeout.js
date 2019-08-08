var quiteTime = 2;
var currentTime = 0;


$(function () {

$("*").click(function () {
        currentTime = 0;
    });

    $('*').mouseover(function () {
         currentTime = 0;
    });

    setInterval(function () {
        currentTime++;
        if(currentTime>=quiteTime)
        {
            top.location.href = '/login/';
        }
    }, 1000);
})
