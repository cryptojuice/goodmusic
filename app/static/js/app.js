var app = angular.module('goodmusic', ['ngRoute']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.when('/login', { templateUrl: 'partials/login.html', controller: 'LoginCtrl'});
    $routeProvider.when('/usertest', { templateUrl: 'partials/usertest.html', controller: 'TestCtrl'});
    $routeProvider.otherwise({ redirectTo: '/login' });
    $locationProvider.html5Mode(true);
}]);

app.controller('TestCtrl', ['$scope', '$http', 'UserService', function($scope, $http, UserService){
    var User = UserService;
    $scope.isAuthenticated = User;
}]);

app.controller('LoginCtrl', ['$scope', '$http', 'UserService', function($scope, $http, UserService){

    var User = UserService;

    $scope.email = ""; 
    $scope.password = "";

    $scope.login = function() {

        var xsrf = $.param({email:$scope.email, password:$scope.password});
        var config = { 
            method: "POST",
            url: "/api/v1/users/login",
            data: xsrf,
            headers: {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        };

        $http(config)
        .success(function(data, status, headers, config) {
            if (status == 200) {
                console.log('authenticated');
                User.isAuthenticated = true;
                User.username = data.username;
            }
            else {
                User.isAuthenticated = false;
            }
        })
        .error(function(data, status, headers, config) {
            console.log("failed");
            User.isAuthenticated = false;
            User.username = '';
        });
    };
}]);

app.factory('UserService', [function() {
    var sdo = {
        isAuthenticated: false,
        username: ''
    };
    return sdo;
}]);
