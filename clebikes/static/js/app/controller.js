var bikeApp = angular.module('bikeApp', []);
var geocoder = new google.maps.Geocoder();
var mapOptions = {
    center: new google.maps.LatLng(41.486132, -81.705087),
    zoom: 13,
    mapTypeId: google.maps.MapTypeId.ROADMAP
};

function find_address(args){
    geocoder.geocode({"address":args.address}, function(results, status){
        console.log(args);
        if(!args.address){
            console.log('address is nothing returning');
            args.success({});
        }
        if(status == google.maps.GeocoderStatus.OK){
            if(results.length > 0){
                var latLng = results[0].geometry.location
                args.success({
                    latitude:latLng.lat(), 
                    longitude:latLng.lng(),
                });
            }else{
                args.failture("We couldn't find a location for this address");
            }
        }else{
            args.failture("something went wrong with the request to google");
        }
    });
}

bikeApp.controller('bikeAppCtrl', function($scope, $http, $q){

    $scope.map = new google.maps.Map( document.getElementById("da-map-canvus"), mapOptions);
    $scope.points = [];
    $scope.serachAddress = null;
    $scope.serachPosition = null;
    $scope.currentPosition = null;
    $scope.update = function(){
        find_address({
            address: $scope.searchAddress, 
            success: function(queryArgs){
                queryArgs.type = 'all';
                $http({method: 'GET', url: '/poi', responseType:'json', data:queryArgs }).
                    success(function(data, status, headers, config){
                        var counter = 0;
                        _.each($scope.points, function(point){
                            point.marker.setMap(null);
                        });
                        $scope.points = _.map(data.points, function(point){ 
                            counter++;
                            point.marker = new google.maps.Marker({
                                icon: "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld="+counter+"|00FF00|000000",
                                position: new google.maps.LatLng( point.location.latitude, point.location.longitude),
                                map: $scope.map, 
                                title: point.name,
                            })
                            return point;
                        });
                });
            },
            failture: function(errorMsg){}
        });
    };
    $scope.update();
})
