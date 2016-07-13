/**
 * Created by gua on 7/6/16 1:48:01
 */

// log
var log = function () {
    console.log(arguments);
};


// form 可以对一类的值进行处理与获取
var formFromKeys = function(keys, prefix) {
    var form = {};
    for(var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var tagid = prefix + key;
        var value = $('#' + tagid).val();
        if (value.length < 1) {
            // alert('字段不能为空');
            break;
        }
        form[key] = value;
    }
    return form;
};

// weibo API
var weibo = {};

var tweetForm = function () {
    var keys = [
        'content',
    ];
    var tweetPrefix = 'id-input-';
    var form = formFromKeys(keys, tweetPrefix);
    return form;
};

var tweet = function () {
    var form = tweetForm();
    var success = function (r) {
        log('r, ', r);
        if (r.success){
            log(r.message);
            var addContent = (`<div class="panel panel-default">
                                  <div class="panel-heading">
                                    <p class="panel-title">${r.username}
                                    <a class="btn pull-right"><i class="icon-remove" title="删除"></i></a>
                                     <br>${r.created_time}
                                    </p>
                                  </div>
                                  <div class="panel-body">
                                    ${r.content}
                                  </div>
                                  <table class="table">
                                  <tr>
                                  <td>
                                  <a class="btn">
                                  <i class=" icon-share-alt"></i>转发</a>
</td>
                                  <td>
                                  <a class="btn">
                                  <i class="icon-comment"></i>评论</a>
</td>
                                  <td>
                                  <a class="btn">
                                  <i class="icon-thumbs-up"></i>赞</a>
</td>
                                  </tr>
</table>
                                </div>`);

            var insertPlace = $('#id-div-insert');
            insertPlace.prepend(addContent);
        }else {
            alert('发布失败');  
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.tweet(form, success, error);
};

weibo.post = function(url, form, success, error) {
    var data = JSON.stringify(form);
    var request = {
        url: url,
        type: 'post',
        contentType: 'application/json',
        data: data,
        success: function (r) {
            log('post success', url, r);
            success(r);
        },
        error: function (err) {
            log('post err', url, err);
            error(err);
        }
    };
    $.ajax(request);
};

weibo.register = function(form, success, error) {
    var url = '/register';
    this.post(url, form, success, error);
};

weibo.login = function(form, success, error) {
    var url = '/login';
    this.post(url, form, success, error);
};

weibo.tweet = function (form, success, error) {
    var url = '/post/tweet/add';
    this.post(url, form, success, error);
};