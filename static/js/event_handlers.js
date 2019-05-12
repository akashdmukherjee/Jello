$( document ).ready(function() {
    getPosts_fromServer("");
    


    $( ".topnav-searchbutton" ).click(function() {
        var user_search_string = $( ".topnav-searchbar" ).val();
        getPosts_fromServer(user_search_string);
    });

    $( ".card" ).click(function() {
        var post_id = 1;
        loadpage_posts(post_id);
    });    
      
});

