
    // Кастомный блок для ошибок и успешных действий
    function errors(message, status) {
        // 1 - ошибка, 2 - правильное
        if (status === 1) {
            notification_zag.innerText = 'Ошибка!';
            notification_zag.style.color = '#db152c';

            return error_notification.innerText = message;
        }
        notification_zag.innerText = 'Успешно!';
        return success_notification.innerText = message;
    }
