(function ($) {
    $(document).ready(function () {
        // Función para actualizar los encuentros según la competición seleccionada
        function actualizarEncuentros() {
            var competicionId = $("#id_competicion_id").val();

            // Si no hay competición seleccionada, ocultar los encuentros
            if (!competicionId) {
                $("#id_encuentro_id option").remove();
                return;
            }

            // Obtener los encuentros filtrados por la competición
            $.ajax({
                url: "/appPartido/get_encuentros/",
                data: { competicion_id: competicionId },
                dataType: 'json',
                success: function (data) {
                    // Actualizar las opciones del campo de encuentro
                    $("#id_encuentro_id option").remove();
                    
                    // Agregar el primer ítem con -----------
                    $("#id_encuentro_id").append($('<option></option>').attr('value', '').text('-----------'));

                    $.each(data, function (key, value) {
                        $("#id_encuentro_id").append($('<option></option>').attr('value', key).text(value));
                    });
                    
                }
            });
        }

        function actualizarAlineaciones() {
            var encuentroId =  $("#id_encuentro_id").val();
           
            if (!encuentroId) {
                $("#id_alineacion1_id option").remove();
                $("#id_alineacion2_id option").remove();
                return;
            }
        
            $.ajax({
                url: "/appPartido/get_alineaciones/",
                data: { encuentro_id: encuentroId },
                dataType: 'json',
                success: function (data) {
                    $("#id_alineacion1_id option").remove();
                    $("#id_alineacion2_id option").remove();
        
                    // Agregar el primer ítem con -----------
                    $("#id_alineacion1_id").append($('<option></option>').attr('value', '').text('-----------'));
                    $("#id_alineacion2_id").append($('<option></option>').attr('value', '').text('-----------'));
                    
                    $.each(data.alineacion1, function (index, value) {
                        $("#id_alineacion1_id").append($('<option></option>').attr('value', value.id).text(value.jugador));
                    });
        
                    $.each(data.alineacion2, function (index, value) {
                        $("#id_alineacion2_id").append($('<option></option>').attr('value', value.id).text(value.jugador));
                    });
                }
            });
        }
        

        // Vincular la función al cambio en el campo de competición
        $("#id_competicion_id").change(actualizarEncuentros);

        // Llamar a la función al cargar la página para inicializar los encuentros
        actualizarEncuentros();

        // Vincular la función al cambio en el campo de competición
        $("#id_encuentro_id").change(actualizarAlineaciones);
        actualizarAlineaciones();
    });
})(django.jQuery);
