$( document ).ready(function() {
    getPosts_fromServer("");
    


    $( ".topnav-searchbutton" ).click(function() {
        var user_search_string = $( ".topnav-searchbar" ).val();
        console.log("----");
        console.log(user_search_string);
        console.log("----");
        getPosts_fromServer(user_search_string);
    });
      
});

