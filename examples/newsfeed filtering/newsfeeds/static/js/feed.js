require(['/js/config.js'], function() {
    'use strict';

    require([
        'jquery',
        'socketio'
    ], function($, io) {

        var socket = io.connect('http://' + document.domain + ':' + location.port);

        // Join the room for this id.
        socket.on('connect', function() {
            var parts = location.pathname.split('/'),
                id = parts[parts.length - 1];
            socket.emit('join', {room: id});
        });

        // This event is when the script has been executed and tweets have been filtered.
        socket.on('executed', function(msg) {
            $('.overlay').fadeOut();
            $('.feed ul').empty()
            $.each(msg.tweets, function(idx, tweet) {
                $('.feed ul').append('\
                    <li class="tweet">'+tweet.text+
                    '<div class="meta">'
                    +tweet.id+' | @'+tweet.user+' | ♻  '+tweet.retweet_count+' | ★ '+tweet.favorite_count
                    +'</div></li>');
            });
        });

        socket.on('updating', function() {
            $('.overlay').fadeIn();
        });
    });

});
