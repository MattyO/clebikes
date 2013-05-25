function load_points(data){
    $.ajax({
        url:"poi", 
        dataType:"json",
        mimeType:"json",
        data: data,
        success:function(data){
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
