$( document ).ready(function() {
    $('#position').hide();
    $('#label_position').hide();

    $("#grupo").change(function(){
        profile = $('#grupo').val();
        if ((profile == 1) || (profile == 2) || (profile == 3)){
            $('#position').show();
            $('#label_position').show();
            }
        if (profile == 5){
            $('#position').hide();
            $('#label_position').hide();
            }        
        });
    });
