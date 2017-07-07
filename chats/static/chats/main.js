$(function() {
    // 定期処理
    var check = setInterval('updateMessage()', 3000);

    // メッセージ送信ボタンクリック処理
    $('#messageForm').submit(function(e) {
        $form = $('#messageForm');

        // ページ更新防止
        e.preventDefault();

        // 2重クリック防止
        var self = this;
        $(':submit', self).prop('disabled', true);
        setTimeout(function() {
            $(':submit', self).prop('disabled', false);
        }, 1000);
        console.log('clicked messageForm');
        console.log($form);

        // メッセージ送信
        $.ajax({
            url: $form.attr('action'),
            type: 'post',
            data: {
                board_id: board_id,
                user_id: user_id,
                text: $('#text').val(),
            },
            timeout: 10000,
            beforeSend: function(xhr, settings) {
                xhr.setRequestHeader('X-CSRFToken', $("input[name='csrfmiddlewaretoken']").val());
            },
        }).done(function(data, textStatus, jqXHR) {
            var $data = $(data);
            var $root = $('#contents');
            $root.empty();
            $root.append($data);
            updateMessage();
            $data.ready(function() {
            });
        }).fail(function(jqXHR, testStatus, errorThrown) {
            console.log('fail');
        });
    });
});

// メッセージ受信処理
function updateMessage() {
    console.log('updateMessage()');
    $form = $('#messageForm');
    $.ajax({
        url: window.location.href + 'get',
        type: 'post',
        dateType: 'JSON',
        cache: 'false',
        data: {latest_message_pub_date: latest_message_pub_date,
                latest_message_id: latest_message_id},
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader('X-CSRFToken', $("input[name='csrfmiddlewaretoken']").val());
        },
    }).done(function(res) {
        data = res.data;
        console.log(data);
        if (data.length > 0) {
            console.log('in', data);
            //var message_list = JSON.parse(data);
            var message_list = data;

            // 最新メッセージ情報の更新
            latest_message = message_list[message_list.length - 1];
            latest_message_pub_date = latest_message.pub_date
            latest_message_id = latest_message.id;

            // メッセージ要素の追加
            $.each(message_list, function(index, message) {
                console.log('index', index, 'val', message, 'pub_date', message.pub_date, 'message', message.message);

                // メッセージ要素を生成
                var messageDiv = $("<div></div>", {
                    'class': 'message'
                });
                messageDiv.append('<p>投稿時間 : ' + message.pub_date + '</p>').append('<p>メッセージ : ' + message.message + '</p>');

                // listのDOMに追加する
                $('#message_list').prepend(messageDiv);
            });
        }
    });
}
