var geocoder = new google.maps.Geocoder();

function find_address(address_string, success, failture){
    geocoder.geocode({"address":address_string}, function(results, status){
        if(status == google.maps.GeocoderStatus.OK){
            if(results.length > 0){
                success(results[0].geometry.location);
            }else{
                failture("We couldn't find a location for this address");
            }
        }else{
            failture("something went wrong with the request to google");
        }
    });
}
