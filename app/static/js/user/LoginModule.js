angular.module('LoginModule', []);

angular.module('LoginModule').controller('LoginController', ['$scope', '$http', 'LoginService', '$sessionStorage', function($scope, $http, UserService, $sessionStorage){

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

angular.module('LoginModule').factory('LoginService', ['$sessionStorage', function($sessionStorage) {
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
