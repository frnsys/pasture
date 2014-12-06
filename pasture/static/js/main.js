require(['config'], function() {
    'use strict';

    require([
        'jquery',
        'socketio'
    ], function($, io) {
        var parts = location.pathname.split('/'),
            id = parts[parts.length - 1];

        // Load an existing script if there is one.
        if (localStorage.getItem('script_'+id)) {
            $('textarea').val(localStorage.getItem('script_'+id));
        }

        // Submit the script.
        $('form').on('submit', function(e) {
            e.preventDefault();

            var script = $('[name=script]').val();

            // Save the script to local storage, just in case.
            localStorage.setItem('script_'+id, script);

            // Running...
            $('button[type=submit]').prop('disabled', true).addClass('running').text('Running...');
            $.ajax({
                url: '/eval/'+id,
                type: 'POST',
                data: {
                    script: script
                },
                success: function(data) {
                    $('.output .data').text(data.out);
                    $('button[type=submit]').prop('disabled', false).removeClass('running').text('Run');

                    if (data.err) {
                        $('.errors').show();
                        $('.errors .data').text(data.err);
                    } else {
                        $('.errors').hide();
                    }

                }, error: function(xhr, status, err) {
                    alert(xhr.status.toString() + ' : ' + xhr.responseText);
                }
            });

            return false;
        });


        // Support 4space tabs in textareas.
        // http://stackoverflow.com/a/6637396/1097920
        $(document).delegate('textarea', 'keydown', function(e) {
            var keyCode = e.keyCode || e.which;

            if (keyCode == 9) {
                e.preventDefault();
                var start = $(this).get(0).selectionStart;
                var end = $(this).get(0).selectionEnd;

                // set textarea value to: text before caret + tab + text after caret
                $(this).val($(this).val().substring(0, start)
                        + "    "
                        + $(this).val().substring(end));
                // put caret at right position again
                $(this).get(0).selectionStart =
                $(this).get(0).selectionEnd = start + 4;
            }

            // Submit the form on enter + shift.
            if (keyCode == 13 && e.shiftKey) {
                e.preventDefault();
                $('form').submit();
            }
        });
    });

});
