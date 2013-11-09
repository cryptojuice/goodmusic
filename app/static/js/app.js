var app = angular.module('goodmusic', ['ngRoute']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.when('/login', { templateUrl: 'partials/login.html', controller: 'LoginCtrl'});
    $routeProvider.otherwise({ redirectTo: '/login' });
    $locationProvider.html5Mode(true);
}]);

app.controller('LoginCtrl', ['$scope', '$http', 'LoginService', function($scope, $http){
    $scope.sayHello = "Hello from login";
}]);

app.factory('LoginService', [function() {
    var sdo = {
        isLogged: false,
        username: ''
    };
    return sdo;
}]);
