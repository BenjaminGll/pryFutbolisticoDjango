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

        // Cambia el orden de inserción de los botones
        guardarButton.before(cancelarContainer);

        // Utiliza display: inline-block y vertical-align: top para alinear correctamente los botones
        guardarButton.css('vertical-align', 'top');
        cancelarContainer.css({
            'display': 'inline-block',
            'vertical-align': 'top',
            'margin-right': '20px' // Ajusta el margen entre los botones según sea necesario
        });

        $(':submit[name="_addanother"]').css('display', 'none');

        // Ajustar anchos de campos de formulario, excluyendo los checkboxes
        $('form').find('input, select, textarea').each(function(){
            // Si es un campo de entrada o textarea, ajusta su ancho
            if ($(this).is('input[type!="button"][type!="submit"][type!="checkbox"], textarea')) {
                $(this).css({
                    'width': '1188px', // Establecer el ancho al 100%
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

         // Agregar botón "Editar" a cada fila de la tabla
        var editButtons = $('<input/>').attr({ type: 'button', name: '_edit', value: 'Editar' }).addClass('default');
        
        // Aplicar estilos al botón "Editar"
        editButtons.css({
            'background-color': '#337ab7', // Color de fondo
            'border': 'none', // Sin borde
            'border-radius': '5px', // Borde redondeado
            'height': '35px', // Altura
            'color': 'white', // Color del texto
            'font-family': fontFamily, // Tipo de letra
            'font-size': '14px', // Tamaño de fuente
            'font-weight': 'bold', // Peso de fuente
            'margin-right': '10px' // Margen derecho entre botones (ajusta según sea necesario)
        });

        // Manejar clic en el botón "Editar"
        editButtons.on('click', function(){
            // Obtener el ID de la fila actual
            var rowId = $(this).closest('tr').attr('id');
            
            // Redirigir a la página de edición correspondiente
            window.location.href = window.location.pathname + rowId + 'change/';
        });

        // Insertar el botón "Editar" después del botón "Cancelar"
        cancelarButton.after(editButtons);
    });
})(django.jQuery);
