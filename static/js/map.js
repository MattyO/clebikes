function load_map() {
    var mapOptions = {
    center: new google.maps.LatLng(41.486132, -81.705087),
    zoom: 13,
    mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map( document.getElementById("da-map-canvus"), mapOptions);

}

function load_points(){
    $.ajax({
        url:"poi", 
        dataType:"json",
        mimeType:"json",
        success:function(data){
            alert(map);
            //data = JSON.parse(data);

            //var marker_image = new google.maps.Symbol({path:"http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|00FF00"});

            for(key in data.points ){
                var a_point = data.points[key];
                var maker = new google.maps.Marker({
                    icon: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|00FF00",
                    position: new google.maps.LatLng( a_point.location.latitude, a_point.location.longitude), 
                    map:map, 
                    title:a_point.name
                });
            }

        },
        error:function(request, text_status, error){
            alert(text_status);
        }

    });
}

function update_hidden_location_fields(mouse_event){
    $("#hdn-latitude").val(mouse_event.latLng.lat());
    $("#hdn-longitude").val(mouse_event.latLng.lng());
}

function place_current_location(){
}

