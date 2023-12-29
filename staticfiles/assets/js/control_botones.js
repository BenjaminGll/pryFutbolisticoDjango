(function($){
    $(document).ready(function(){
                // Verificar si la URL contiene "add" o "change"
                var urlContainsAddOrChange = window.location.href.indexOf('add') !== -1 || window.location.href.indexOf('change') !== -1;

                // Salir del script si la URL no contiene "add" o "change"
                if (!urlContainsAddOrChange) {
                    return;
                }
        
        $(':submit[name="_continue"]').remove();
        $(':submit[name="_addanother"]').css('display', 'none');

        var cancelarButton = $('<input/>').attr({ type: 'button', name: '_cancel', value: 'Cancelar' }).addClass('btn btn-sm btn-warning');
        var guardarButton = $(':submit[name="_save"]');
       

        cancelarButton.on('click', function(){
            history.back();
        });

        var cancelarContainer = $('<div></div>').append(cancelarButton);

        // Cambia el orden de inserción de los botones
        guardarButton.before(cancelarContainer);

        // Utiliza display: inline-block y vertical-align: top para alinear correctamente los botones
        guardarButton.css({
            'vertical-align': 'top',
            'margin-right': '4.6px' // Ajusta el margen entre los botones "Guardar" y "Cancelar"
        });
        cancelarContainer.css({
            'display': 'inline-block',
            'vertical-align': 'top'
        });

        // $('.col-12.mb-4').removeClass('col-12 mb-4').addClass('col-md-6');

        // Restricciones al tamaño máximo
        function adjustStyles() {
        var maxWidth = $('.card-body').width(); // Obtener el ancho del card body

        // Ajustar anchos de campos de formulario, excluyendo los checkboxes
        $('form').find('input, select, textarea').each(function () {
            // Si es un campo de entrada o textarea, ajusta su ancho
            if ($(this).is('input[type!="button"][type!="submit"][type!="checkbox"], textarea')) {
                $(this).css({
                    'width': maxWidth + 'px', // Establecer el ancho al máximo del card body
                    'box-sizing': 'border-box' // Considerar el padding y el borde en el ancho total
                });
            }

            // Si es un combobox (elemento select), también ajusta su ancho
            if ($(this).is('select')) {
                // Aplicar estilos directamente al elemento select
                $(this).css({
                    'width': maxWidth + 'px', // Establecer el ancho al máximo del card body
                    'box-sizing': 'border-box' // Considerar el padding y el borde en el ancho total
                });
            }
        });
    }

            // Llamar a la función de ajuste de estilos al cargar la página y al cambiar el tamaño de la ventana
            adjustStyles();
            $(window).on('resize', adjustStyles);
            
        });

    })(django.jQuery);

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

            // Agregar estilo al botón de cerrar (color blanco)
            $('.mfp-close').css({
                'color': 'white', // Cambiar a tu color deseado
                'background-color': 'transparent', // Cambiar a tu color deseado
                'border': 'none'
            });

        }, 1); // Ajusta el tiempo de espera según sea necesario
    });
});

