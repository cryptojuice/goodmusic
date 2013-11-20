angular.module('goodmusic').config(['$urlRouterProvider', '$stateProvider', '$locationProvider', 
        function($urlRouterProvider, $stateProvider, $locationProvider) {

    $stateProvider.state('search', {
        url: '/search',
        templateUrl: 'partials/search.html',
        controller: 'SearchController'
    });
}]);



angular.module('SearchModule', []);

angular.module('SearchModule').controller('SearchController', [
        '$scope', '$http', '$resource', '$stateParams', function($scope,
            $http, $resource, $stateParams){

    $scope.submit = function() {
        $http.get('api/v1/search/artist='+ $scope.artist + '&limit=1')
        .success(function(data, status, headers, config) {
            $scope.artistResults = data.results.artistmatches.artist;
            $scope.name = $scope.artistResults.name;
            $scope.image = $scope.artistResults.image[2]['#text'];
        })
        .error(function(data, status, headers, config) {
            console.log("search failed");
        });
    };

}]);
