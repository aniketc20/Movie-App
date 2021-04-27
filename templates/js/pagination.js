{% load static %}
var currentPage = 1;
var pageList = new Array();
var numberPerPage = 3;
var numberOfPages = 0;
    
numberOfPages = Math.ceil(list.length / numberPerPage);
function nextPage() {
    currentPage += 1;
    loadList();
}

function previousPage() {
    currentPage -= 1;
    loadList();
}

function firstPage() {
    currentPage = 1;
    loadList();
}

function lastPage() {
    currentPage = numberOfPages;
    loadList();
}

function loadList() {
    var begin = ((currentPage - 1) * numberPerPage);
    var end = begin + numberPerPage;

    pageList = list.slice(begin, end);
    drawList();
    check();
}
    
function drawList() {
    document.getElementById("parent").innerHTML = "";
    for (r = 0; r < pageList.length; r++) {
        $('#parent').append("<div class=a"+r+" id="+r+"></div>");
    $('#'+r).append("<br><div class='leftbox' relative>"+"<h3>"+pageList[r]['title']+' ('+ pageList[r]['release_date'] + ')'+"<a href='#'><img class=poster src=https://image.tmdb.org/t/p/w185_and_h278_bestv2"+pageList[r]['pic']+" > </a></div>");
    if(pageList[r]['fav']=='No')
    {
        $("#"+r).append("<div relative class=rightbox><h3><u>Overview" + "</u></h3>" 
        + pageList[r]['overview'] + "<div class=one><div><br>TMDB rating: <b>"+pageList[r]['vote_average']+
        "</b></div><div><br><img src={% static 'star.png' %} height=30/></div></div>"+
         "<a class=saveicon name=Save onclick=fav_mov(id) id="+pageList[r]['movie_id']+"><b>Add To favourites</b><img src={% static 'bookmark.png' %} height=35/></a><br><br><button onclick=cast(id) id="+pageList[r]['movie_id']+ ">Cast</button>: <br></div><br><br>");
    }
    else
    {
        $("#"+r).append("<div relative class=rightbox><h3><u>Overview" + "</u></h3>" 
        + pageList[r]['overview'] + "<br><br> TMDB rating: <b>"+pageList[r]['vote_average']+
         "<input type=button name=Save onclick=rem_fav_mov(id) type=submit id="+pageList[r]['movie_id']+" value=Remove><br><br>Cast: <br></input></div><br><br>");
    }
}
}

function check() {
    document.getElementById("next").disabled = currentPage == numberOfPages ? true : false;
    document.getElementById("previous").disabled = currentPage == 1 ? true : false;
    document.getElementById("first").disabled = currentPage == 1 ? true : false;
    document.getElementById("last").disabled = currentPage == numberOfPages ? true : false;
}