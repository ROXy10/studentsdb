/**
 * Created by roxy on 19.05.16.
 */
var num = 8;
$(window).scroll(function() {
    if($(window).scrollTop() + $(window).height() == $(document).height()) {
    $.ajax({
        url: '', 
        type: 'get',
        dataType: 'html',
        cache: false,
        data: {'num': num},  
        success: function (data) {
            if (data != 0) {
                var html = $(data), lastTableTr;
                lastTableTr = $(document).find('tbody tr').last().find('td:first').text();
                html.find('tbody tr td:first').text(+ lastTableTr + 1);
                $('tbody').append(html.find('tbody').html());
                num = num + 1;
            }
        },
        error: function () {
            alert('Помилка на сервері. Спробуйте будь-ласка пізніше');
            return false;
        }
    });
    }
});