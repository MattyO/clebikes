function load_map() {
    var mapOptions = {
    center: new google.maps.LatLng(41.486132, -81.705087),
    zoom: 13,
    mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map( document.getElementById("da-map-canvus"), mapOptions);
}

function add_points_to_map(points){
            for(key in points ){
                var a_point = points[key];
                points_array.push(new google.maps.Marker({
                    icon: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|00FF00",
                    position: new google.maps.LatLng( a_point.location.latitude, a_point.location.longitude), 
                    map:map, 
                    title:a_point.name
                }));
            }
}

function remove_points_from_map(){
    for( key in points_array){
        points_array[key].setMap(null);
    }
    points_array = Array();
}

function get_points(args={}){
    $.ajax({
        url:"poi", 
        dataType:"json",
        mimeType:"json",
        data: args.queryData,
        success:function(data){
            args.success(data)
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

