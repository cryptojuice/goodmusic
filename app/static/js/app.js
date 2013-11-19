angular.module('goodmusic', [
        'ngRoute', 
        'ngStorage', 
        'ngResource',
        'LoginModule',
        'SearchModule'
        ]);

angular.module('goodmusic').config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
    .when('/login', { templateUrl: 'partials/login.html', controller: 'LoginController'})
    .when('/search', { templateUrl: 'partials/search.html', controller: 'SearchController'})
    .otherwise({ redirectTo: '/' });

    $locationProvider.html5Mode(true);
}]);

