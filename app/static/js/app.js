angular.module('goodmusic', [
        'ui.router',
        'ngStorage', 
        'ngResource',
        'NavModule',
        'UserModule',
        'SearchModule'
        ]);

angular.module('goodmusic').config(['$urlRouterProvider', '$stateProvider', '$locationProvider', 
        function($urlRouterProvider, $stateProvider, $locationProvider) {

    $stateProvider.state('home', {
        url: '/',
        template:"<h1>GoodMusic</h1>"
    });

    $urlRouterProvider.otherwise('/');

    $locationProvider.html5Mode(true);
}]);

