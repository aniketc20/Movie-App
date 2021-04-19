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
    $('#parent').append("<div class='leftbox'>"+"<img src=https://image.tmdb.org/t/p/w185_and_h278_bestv2"+pageList[r]['pic']+" 'width='700' height='250'> </div>");
    if(pageList[r]['fav']=='No')
    {
        $("#parent").append("<div class='rightbox'>" + "<h3>"
         + pageList[r]['title'] + ' ('+ pageList[r]['release_date'] + ')' + "</h3>" + pageList[r]['overview'] + "<br><br> TMDB rating: <b>"+pageList[r]['vote_average']+
         "<input type=button name=Save onclick=fav_mov(id) type=submit id="+pageList[r]['movie_id']+" value=Save></input></div>");
    }
    else
    {
        $("#parent").append("<div class='rightbox'>" + "<h3>"
         + pageList[r]['title'] + ' ('+ pageList[r]['release_date'] + ')' + "</h3>" + pageList[r]['overview'] + "<br><br> TMDB rating: <b>"+pageList[r]['vote_average']+
         "<input type=button name=Rem onclick=rem_fav_mov(id) type=submit id="+pageList[r]['movie_id']+" value='Remove'></input></div>");
    }
}
}

function check() {
    document.getElementById("next").disabled = currentPage == numberOfPages ? true : false;
    document.getElementById("previous").disabled = currentPage == 1 ? true : false;
    document.getElementById("first").disabled = currentPage == 1 ? true : false;
    document.getElementById("last").disabled = currentPage == numberOfPages ? true : false;
}