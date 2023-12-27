(function($){
    $(document).ready(function(){
        // Obtener la tabla que contiene las filas
        var table = $('table');

        // Agregar los encabezados para las nuevas columnas
        var headerEditCell = $('<th/>').text(''); // Columna para el botón de editar
        var headerDeleteCell = $('<th/>').text(''); // Columna para el botón de eliminar
        table.find('thead tr').append(headerEditCell, headerDeleteCell);

        // Establecer el estilo del borde inferior para las celdas del encabezado
        table.find('thead th').css('border-bottom', 'none');

        // Agregar los botones de editar y eliminar a cada fila
        table.find('tbody tr').each(function(){
            var row = $(this);
            var editUrl = row.find('th a').attr('href'); // Obtener el enlace de edición desde la primera celda (ID)
            var deletetUrl = row.find('th a').attr('href'); // Obtener el enlace de edición desde la primera celda (ID)
            // Crear el botón de editar con un ícono de lápiz de FontAwesome
            var editButton = $('<a/>').attr({ href: editUrl }).html('<i class="fas fa-pencil-alt"></i>'); // Ajusta la clase del ícono según FontAwesome
            var editCell = $('<td/>').append(editButton);

            // Crear el botón de eliminar con un ícono de basura de FontAwesome
            var deleteButton = $('<a/>').attr({ href: deletetUrl }).html('<i class="fas fa-trash"></i>'); // Ajusta la clase del ícono según FontAwesome
            var deleteCell = $('<td/>').append(deleteButton);

            // Agregar la celda de editar y eliminar a la fila
            row.append(editCell, deleteCell);

        });
    });
})(django.jQuery);
