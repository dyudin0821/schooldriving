let map;
$(document).ready(function () {
    map = new GMaps({
        el: '#map',
        // lat: 59.939002,
        lat: 59.939024,
        lng: 30.315733,
        zoom: 9

    });
    map.addMarker({
        lat: 59.882427,
        lng: 29.890062,
        title: 'автошкола "Альтернатива"',
        infoWindow: {
            content: '<p>Aвтошкола "Альтернатива"<br> Обучение водителей категорий "А" и "В"<br>Санкт-Петербургский пр., д.60, оф. №431 <br><a href="tel://404-7000">тел.:404-7000</a> </p>'
        }
    });
    map.addMarker({
        lat: 59.7895611,
        lng: 30.148093,
        title: 'автошкола "Альтернатива"',
        infoWindow: {
            content: '<p>автошкола "Альтернатива"<br> Обучение водителей категорий "А" и "В"<br> Красносельское ш., д.50 <br><a href="tel://404-7000">тел.:404-7000</a></p>'
        }
    });
    map.addMarker({
        lat: 60.073194,
        lng: 30.342617,
        title: 'автошкола "Альтернатива"',
        infoWindow: {
            content: '<p>автошкола "Альтернатива"<br> Обучение водителей категорий "А" и "В"<br> 4-й Верхний пер. д.19, секция: 37. 2 этаж <br><a href="tel://+7 (812) 925-6068">тел.:+7 (812) 925-60680</a></p>'
        }
    });
    map.addMarker({
        lat: 60.051998,
        lng: 30.335406,
        title: 'автошкола "Альтернатива"',
        infoWindow: {
            content: '<p>автошкола "Альтернатива"<br> Обучение водителей категорий "А" и "В"<br> пр.Энгельса 139, секция: 68 <br><a href="tel://+7 (812) 920-0410">тел.:+7 (812) 920-0410</a></p>'
        }
    });
});