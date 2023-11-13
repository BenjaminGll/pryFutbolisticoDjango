(function($){
    $(document).ready(function(){
        $(':submit[name="_continue"]').remove();

        var cancelarButton = $('<input/>').attr({ type: 'button', name: '_cancel', value: 'Cancelar' }).addClass('success');
        var guardarButton = $(':submit[name="_save"]');
        
        // Obtener el tipo de letra del botón "Guardar"
        var fontFamily = guardarButton.css('font-family');

        cancelarButton.css({
            'background-color': '#e61610', 
            'border-radius': '5px',
            'height': '35px',
            'color': 'white',
            'font-family': fontFamily,  // Aplicar el mismo tipo de letra que el botón "Guardar"
            'font-size': '14px',       // Ajusta según sea necesario
            'font-weight': 'bold'
        });
        cancelarButton.on('click', function(){
            history.back();
        });

        var cancelarContainer = $('<div></div>').append(cancelarButton);

        // Utiliza display: inline-block y vertical-align: top para alinear correctamente los botones
        guardarButton.after(cancelarContainer);
        guardarButton.css('vertical-align', 'top');
        cancelarContainer.css({
            'display': 'inline-block',
            'vertical-align': 'top',
            'margin-right': '10px'
        });

        $(':submit[name="_addanother"]').css('display', 'none');

       // Ajustar anchos de campos de formulario, incluyendo los combobox
       $('form').find('input, select, textarea').each(function(){
        // Si es un campo de entrada o textarea, ajusta su ancho
        if ($(this).is('input, textarea')) {
            $(this).css({
                'width': '100%', // Establecer el ancho al 100%
                'box-sizing': 'border-box' // Considerar el padding y el borde en el ancho total
            });
        }

        // Si es un combobox (elemento select), también ajusta su ancho
        if ($(this).is('select')) {
            // Aplicar estilos directamente al elemento select
            $(this).css({
                'width': '1188px', // Establecer el ancho al 100%
                'box-sizing': 'border-box' // Considerar el padding y el borde en el ancho total
            });
        }
    });
});
})(django.jQuery);