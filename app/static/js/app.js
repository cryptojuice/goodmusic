var app = angular.module('goodmusic', ['ngRoute']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.when('/login', { templateUrl: 'partials/login.html', controller: 'LoginCtrl'});
    $routeProvider.otherwise({ redirectTo: '/login' });
    $locationProvider.html5Mode(true);
}]);

app.controller('LoginCtrl', ['$scope', '$http', 'LoginService', function($scope, $http, LoginService){
    $scope.sayHello = "Hello from login";

    var User = LoginService;

    $scope.login = function() {
        var xsrf = $.param({email:"example@example.com", password:"default"});
        var config = { 
            method: "POST",
            url: "/api/v1/users/login",
            data: xsrf,
            headers: {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        };

        $http(config)
        .success(function(data, status, headers, config) {
            if (status == 200) {
                console.log(data);
                User.isAuthenticated = true;
                User.username = data.username;
            }
            else {
                User.isAuthenticated = false;
            }
        })
        .error(function(data, status, headers, config) {
            User.isAuthenticated = false;
            User.username = '';
        });
    };
}]);

app.factory('LoginService', [function() {
    var sdo = {
        isAuthenticated: false,
        username: ''
    };
    return sdo;
}]);
