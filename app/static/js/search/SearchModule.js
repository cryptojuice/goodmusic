var searchModule = angular.module('SearchModule', []);

searchModule.controller('SearchController', ['$scope', '$http', '$resource', function($scope, $http, $resource){

    $scope.submit = function() {
        $http.get('api/v1/search/artist='+ $scope.artist)
        .success(function(data, status, headers, config) {
            $scope.artistResults = data.results.artistmatches.artist;
        })
        .error(function(data, status, headers, config) {
            console.log("search failed");
        });
    };
}]);
