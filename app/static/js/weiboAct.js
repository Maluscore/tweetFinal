/**
 * Created by PGH on 2016/7/13.
 */
var tweet_selected = function ($self) {
    //推荐使用.data('id')去接data-id的值
    var tweetID = $self.parentsUntil('#id-div-insert').last().data('id');
    log('tweetID, ', tweetID);
    var form = {};
    form['id'] = tweetID;
    return form;
};


// 换一种方式去得到所选中的tweet
var tweet_chosen = function ($self) {
    var tweetSelf = $self.closest('.panel');
    return tweetSelf
};


// 展开评论区
var comment_open = function ($self) {
    var tweetSelf = tweet_chosen($self);
    // log('tweetSelf', tweetSelf.data('id'));
    var form = {
        id: tweetSelf.data('id')
    };
    log('form是：', form.id);
    var success = function (r) {
        log('成功后返回的r为：', r);
        if (r.success) {
            log('r.message: ', r.message);
            $self.html('收起评论');
            var comment_zone = $(`<div class="list-group" id="id-div-comment"></div>`);
            var comment_item;
            for (var i=0; i<r.data.length; i++) {
                comment_item = (`<i class="list-group-item"><h4>${r.data[i].sender_name}<small>${r.data[i].created_time}</small></h4><p>${r.data[i].content}</p></i>`);
                comment_zone.append(comment_item);
            }
            log('拼凑成功', comment_zone);
            var comment_form = (`    <div class="input-group">
                    <input type="text" class="form-control" placeholder="评论..." id="id-input-comment">
                    <span class="input-group-btn">
                        <button class="btn" id="id-btn-comment" style="background: #EEEEEE;">评论</button>
                    </span>
            </div>`);
            comment_zone.prepend(comment_form);
            tweetSelf.after(comment_zone);
        } else {
            alert('展开评论区失败')
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.comment_open(form, success, error);
};


// 关闭评论区
var comment_close = function ($self) {
    var tweetSelf = tweet_chosen($self);
    var form = {
        id: tweetSelf.data('id')
    };
    var comment_zone = tweetSelf.next();
    var success = function (r) {
        if (r.success) {
            log('r.message :', r.message);
            var count = r.data.com_count;
            $self.html('评论' + count);
            comment_zone.remove();
        } else {
            log(r.message);
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.comment_close(form, success, error);
};


// 获得评论内容
var commentForm = function ($self) {
    var commentForm = $('#id-input-comment');
    var commentContent = commentForm.val();
    commentForm.val('');
    var formSelf = $self.closest('.list-group');
    var tweetID = formSelf.prev().data('id');
    log('tweetID', tweetID);
    var form = {
        content: commentContent,
        id: tweetID
    };
    log('content is:', form.content);
    return form;
};


// 组装发送评论的函数
var add_comment = function ($self) {
    var form = commentForm($self);
    var formSelf = $self.closest('.list-group');
    var success = function (r) {
        if (r.success) {
            log('r.message:', r.message);
            var added = (`<i class="list-group-item"><h4>${r.data.sender_name}<small>${r.data.created_time}</small></h4><p>${r.data.content}</p></i>`)
            formSelf.append(added);
            var count = $('#id-span-count');
            var num = count.val();
            log('num', num);
            count.val(num + 1);
        }else {
            alert('评论失败！');
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.tweet_comment(form, success, error);
};


// 删除
var tweet_delete = function ($self) {
    var form = tweet_selected($self);
    log('form, ', form);
    var success = function (r) {
        log('r, ', r);
        if (r.success) {
            log(r.message);
            var tweetForm = $self.parentsUntil('#id-div-insert').last();
            var next_div = tweetForm.next();
            log(next_div.attr('id'));
            tweetForm.remove();
            // 删除没有收起评论的部分，必须是双引号。。。
            if (next_div.attr('id') === "id-div-comment"){
                next_div.remove();
            }
        } else {
            alert('删除失败！')
        }
    };
    var error = function (err) {
        log('reg, ', err);
    };
    weibo.tweet_delete(form, success, error);
};

// 转发
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

// // 评论
// var tweet_comment = function () {
//     var form = {
//         id: "tweetID"
//     };
//     var success = function (r) {
//         log('r, ', r);
//         if (r.success) {
//             log(r.message);
//             // $('#id-tweet-' + r.data.id).empty();
//         } else {
//             alert('删除失败！')
//         }
//     };
//     var error = function (err) {
//         log('reg, ', err);
//     };
//     weibo.tweet_delete(form, success, error);
// };

// 点赞
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

weibo.comment_open = function (form, success, error) {
    url = '/api/comment/open';
    weibo.post(url, form, success, error);
};

weibo.comment_close = function (form, success, error) {
    url = '/api/comment/close';
    weibo.post(url, form, success, error);
};

weibo.tweet_thumbs_up = function (form, success, error) {
    url = '/api/tweet/thumbs_up';
    weibo.post(url, form, success, error);
};

// TODO:
// 增加api，绑定动作