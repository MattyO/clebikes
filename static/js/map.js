function initialize() {
    var mapOptions = {
    center: new google.maps.LatLng(41.486132, -81.705087),
    zoom: 13,
    mapTypeId: google.maps.MapTypeId.ROADMAP
    };


    $.ajax({
        url:"poi", 
        dataType:"json",
        mimeType:"json",
        success:function(data){
            //data = JSON.parse(data);
            var map = new google.maps.Map(    document.getElementById("da-map-canvus"), mapOptions);

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

        }
    });
}

google.maps.event.addDomListener(window, 'load', initialize);

