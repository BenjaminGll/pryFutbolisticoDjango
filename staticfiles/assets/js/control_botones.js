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

        var modalContainer = $('.related-widget-wrapper-link').closest('.related-widget-wrapper').find('.related-modal-iframe-container');

        // Ajustar el tamaño después de que se carga el iframe
        var iframe = modalContainer.find('iframe');
        iframe.on('load', function() {
            modalContainer.css({
                'width': '800px', // Ajusta el ancho según tus necesidades
                'height': '600px' // Ajusta la altura según tus necesidades
            });
        });



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

       // Restricciones al tamaño máximo
       var maxWidth = $('.card-body').width(); // Obtener el ancho del card body

       // Ajustar anchos de campos de formulario, excluyendo los checkboxes
       $('form').find('input, select, textarea').each(function(){
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
});
})(django.jQuery);
