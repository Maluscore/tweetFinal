/**
 * Created by PGH on 2016/7/13.
 */
var tweetAct = function (icon, tweetID) {
    if (icon = 'icon-remove')
    {
        tweet_delete(tweetID);
    }
    else if (icon = 'icon-share-alt')
    {
        tweet_share(tweetID);
    }
    else if (icon = 'icon-comment')
    {
        tweet_comment(tweetID);
    }
    else if (icon = 'icon-thumbs-up')
    {
        tweet_thumbs_up(tweetID);
    }
};

var tweet_delete = function (tweetID) {
    var form = {
        id: "tweetID"
    };
    var success = function (r) {
        log('r, ', r);
        if (r.success) {
            log(r.message);
            $('#id-tweet-' + r.data.id).empty();
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