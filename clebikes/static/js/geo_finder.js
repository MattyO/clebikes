var geocoder = new google.maps.Geocoder();

function find_address(args){
    geocoder.geocode({"address":args.address}, function(results, status){
        if(status == google.maps.GeocoderStatus.OK){
            if(results.length > 0){
                args.success(results[0].geometry.location);
            }else{
                args.failture("We couldn't find a location for this address");
            }
        }else{
            args.failture("something went wrong with the request to google");
        }
    });
}
