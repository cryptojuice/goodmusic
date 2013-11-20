angular.module('goodmusic').config(['$urlRouterProvider', '$stateProvider', '$locationProvider', 
        function($urlRouterProvider, $stateProvider, $locationProvider) {

    $stateProvider.state('navSearch', {
        url: '/search/:searchText',
        templateUrl: 'partials/search.html',
        resolve: {
            searchData: function($http, $stateParams){
                return $http.get('api/v1/search/artist=' + $stateParams.searchText +
                    '&limit=1');
            }
        },
        controller: 'NavSearchController'
    });
}]);


angular.module('NavModule', []);

angular.module('NavModule').controller('NavController', ['$scope', 
        '$sessionStorage', '$location', function($scope, $sessionStorage, $location){


    $scope.searchText = '';

    $scope.$watch(function(){
        $scope.authenticated = $sessionStorage.isAuthenticated;
    });

    $scope.logout = function(){
        $sessionStorage.isAuthenticated = false;
        $sessionStorage.username = "";
    };

    $scope.submit = function(){
        console.log('submit');
        $location.path('/search/' + $scope.searchText);
    };
}]).controller('NavSearchController', ['$scope', 'searchData', function($scope, searchData){
    $scope.artistResults = searchData.data.results.artistmatches.artist;
    $scope.name = $scope.artistResults.name;
    $scope.image = $scope.artistResults.image[2]['#text'];
}]);

