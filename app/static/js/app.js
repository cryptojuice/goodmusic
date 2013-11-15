var app = angular.module('goodmusic', ['ngRoute', 'ngStorage']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.when('/login', { templateUrl: 'partials/login.html', controller: 'LoginCtrl'});
    $routeProvider.when('/usertest', { templateUrl: 'partials/usertest.html', controller: 'TestCtrl'});
    $routeProvider.otherwise({ redirectTo: '/login' });
    $locationProvider.html5Mode(true);
}]);

app.controller('TestCtrl', ['$scope', '$http', 'UserService', '$sessionStorage', function($scope, $http, UserService, $sessionStorage){
    $scope.user = UserService
    $scope.$storage = $sessionStorage;
    console.log($sessionStorage.inAuthenticated);
}]);

app.controller('LoginCtrl', ['$scope', '$http', 'UserService', '$sessionStorage', function($scope, $http, UserService, $sessionStorage){

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
                $sessionStorage.isAuthenticated = true;
                $sessionStorage.username = data.username;
            }
            else {
                $sessionStorage.isAuthenticated = false;
            }
        })
        .error(function(data, status, headers, config) {
            $sessionStorage.isAuthenticated = false;
            $sessionStorage.username = '';
        });
    };
}]);

app.factory('UserService', ['$sessionStorage', function($sessionStorage) {
    if($sessionStorage.isAuthenticated){
        console.log('session is authenticated');
        return {
            isAuthenticated: true,
            username: $sessionStorage.username
        };
    } else {
        console.log('session is not authenticated');
    }
    
    return {
        isAuthenticated: false,
        username: ''
    };
}]);
