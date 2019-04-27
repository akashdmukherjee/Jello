$( document ).ready(function() {
            var input = "Akash";
            $.ajax(
                        {
                                url: "/getData"
                            , type: 'POST'
                            , async: false
                            , data: {param: input}
                            , success: function(response) {
                                                    response = JSON.parse(response);
                                                    console.log(response.datakey);
                                    }

                        }
            );

            if(checkIfMobile()) {
                $(".landingpage-bullets").hide();
            }
});