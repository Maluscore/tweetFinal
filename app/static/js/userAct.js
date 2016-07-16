
var log = function () {
    console.log(arguments);
};

// user API
var user = {
  data:{}
};

user.ajax = function(url, method, form, success, error) {
    if(method === 'post') {
        var data = JSON.stringify(form);
        request.data = data;
    }
    var request = {
        url: url,
        type: method,
        contentType: 'application/json',
        success: function (r) {
            log('user post success', url, r);
            success(r);
        },
        error: function (err) {
            r = {
                success: false,
                data: err
            };
            log('user post err', url, err);
            error(r);
        }
    };
    if(method === 'post') {
        var data = JSON.stringify(form);
        request.data = data;
    }
    $.ajax(request);
};

user.get = function(url, response) {
    var method = 'get';
    var form = {}
    this.ajax(url, method, form, response, response);
};

user.post = function(url, form, success, error) {
    var method = 'post';
    this.ajax(url, method, form, success, error);
};