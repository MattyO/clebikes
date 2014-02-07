var bikeApp = angular.module('bikeApp', []);
var geocoder = new google.maps.Geocoder();
var mapOptions = {
    center: new google.maps.LatLng(41.486132, -81.705087),
    zoom: 13,
    mapTypeId: google.maps.MapTypeId.ROADMAP
};


bikeApp.controller('bikeAppCtrl', function($scope, $http, $q){
    function find_address(address){
        var deferred = $q.defer();
        if(!address){
            deferred.resolve(null, null);
        }
        geocoder.geocode({"address":address}, function(results, status){
            if(status == google.maps.GeocoderStatus.OK){
                if(results.length > 0){
                    var latLng = results[0].geometry.location
                    deferred.resolve(latLng.lat(), latLng.lng())
                }else{
                    deferred.reject("We couldn't find a location for this address");
                }
            }else{
                deferred.reject("something went wrong with the request to google");
            }
        });
        return deferred.promise
    }

    $scope.map = new google.maps.Map( document.getElementById("da-map-canvus"), mapOptions);
    $scope.points = [];
    $scope.serachAddress = null;
    $scope.update = function(){
        find_address($scope.searchAddress).then(function(lat, lng){
                queryArgs = {
                    type: 'all',
                    latitude: lat,
                    longitude: lng
                }

                $http({method: 'GET', url: '/poi', responseType:'json', data:queryArgs })
                    .success(function(data, status, headers, config){
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
            });
    };
    $scope.update();
})
