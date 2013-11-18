var app = angular.module('goodmusic', [
        'ngRoute', 
        'ngStorage', 
        'LoginModule',
        'SearchModule'
        ]);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
    .when('/login', { templateUrl: 'partials/login.html', controller: 'LoginController'})
    .when('/search', { templateUrl: 'partials/search.html', controller: 'SearchController'})
    .otherwise({ redirectTo: '/login' });

    $locationProvider.html5Mode(true);
}]);

