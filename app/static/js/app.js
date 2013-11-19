angular.module('goodmusic', [
        'ui.router',
        'ngRoute', 
        'ngStorage', 
        'ngResource',
        'NavModule',
        'LoginModule',
        'SearchModule'
        ]);

angular.module('goodmusic').config(['$routeProvider', '$stateProvider', '$locationProvider', 
        function($routeProvider, $stateProvider, $locationProvider) {

    $stateProvider.state('home', {
        url: '/',
        template:"<h1>you are home</h1>"
    });
    $stateProvider.state('login', {
        url: '/login',
        templateUrl: 'partials/login.html',
        controller: 'LoginController'
    });
    $stateProvider.state('search', {
        url: '/search',
        templateUrl: 'partials/search.html',
        controller: 'SearchController'
    });

    $locationProvider.html5Mode(true);
}]);

