/**
 * Created by PGH on 2016/7/13.
 */
var tweet_selected = function ($self) {
    var tweetID = $self.parentsUntil('#id-div-insert').last().attr('data-id');
    log('tweetID, ', tweetID);
    var form = {};
    form['id'] = tweetID;
    return form;
};

var tweet_delete = function ($self) {
    var form = tweet_selected($self);
    log('form, ', form);
    var success = function (r) {
        log('r, ', r);
        if (r.success) {
            log(r.message);
            var tweetForm = $self.parentsUntil('#id-div-insert').last();
            tweetForm.remove();
        } else {
            alert('删除失败！')
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.tweet_delete(form, success, error);
};

var tweet_share = function (tweetID) {
    var form = {
        id: "tweetID"
    };
    var success = function (r) {
        log('r, ', r);
        if (r.success) {
            log(r.message);
            // $('#id-tweet-' + r.data.id).empty();
        } else {
            alert('删除失败！')
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.tweet_delete(form, success, error);
};

var tweet_comment = function (tweetID) {
    var form = {
        id: "tweetID"
    };
    var success = function (r) {
        log('r, ', r);
        if (r.success) {
            log(r.message);
            // $('#id-tweet-' + r.data.id).empty();
        } else {
            alert('删除失败！')
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.tweet_delete(form, success, error);
};

var tweet_thumbs_up = function (tweetID) {
    var form = {
        id: "tweetID"
    };
    var success = function (r) {
        log('r, ', r);
        if (r.success) {
            log(r.message);
            // $('#id-tweet-' + r.data.id).empty();
        } else {
            alert('删除失败！')
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.tweet_delete(form, success, error);
};

weibo.tweet_delete = function (form, success, error) {
    url = '/api/tweet/delete';
    weibo.post(url, form, success, error);
};

weibo.tweet_share = function (form, success, error) {
    url = '/api/tweet/share';
    weibo.post(url, form, success, error);
};

weibo.tweet_comment = function (form, success, error) {
    url = '/api/tweet/comment';
    weibo.post(url, form, success, error);
};

weibo.tweet_thumbs_up = function (form, success, error) {
    url = '/api/tweet/thumbs_up';
    weibo.post(url, form, success, error);
};

// TODO:
// 增加api，绑定动作