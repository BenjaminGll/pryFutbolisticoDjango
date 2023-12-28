$(document).ready(function () {
    $('a.related-widget-wrapper-link').on('click', function (e) {
        var windowWidth = $(window).width();
        var windowHeight = $(window).height();
        var modalWidth = windowWidth / 1.1;
        var modalHeight = windowHeight / 1.1;
        console.log('si ejecuta 1');

        // Agregar un retraso para asegurar que el modal esté completamente abierto
        setTimeout(function () {
            // Buscar el iframe dentro del div con la clase 'related-modal-iframe-container'
            $('div.related-modal-iframe-container').find('iframe').each(function () {
                // Modificar el tamaño y la posición del iframe
                $(this).css({
                    'width': modalWidth + 'px',
                    'height': modalHeight + 'px',
                    'margin-left': (windowWidth - modalWidth) / 2.2 + 'px'
                });
                console.log('si ejecuta 2');
            });
        }, 1); // Ajusta el tiempo de espera según sea necesario
    });
});
