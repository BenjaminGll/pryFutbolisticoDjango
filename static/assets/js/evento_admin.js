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
                    $.each(data, function (key, value) {
                        $("#id_encuentro_id").append($('<option></option>').attr('value', key).text(value));
                    });

                    // Llamar a la función para obtener detalles de alineaciones cuando se selecciona un encuentro
                    $("#id_encuentro_id").change(function () {
                        var encuentroId = $(this).val();

                        // Obtener detalles de alineaciones para el encuentro seleccionado
                        $.ajax({
                            url: "/appPartido/get_alineaciones/",
                            data: { encuentro_id: encuentroId },
                            dataType: 'json',
                            success: function (alineaciones) {
                                // Actualizar las vistas de las alineaciones en el formulario
                                $("#id_alineacion1_id").val(alineaciones.alineacion_local);
                                $("#id_alineacion2_id").val(alineaciones.alineacion_visita);
                            }
                        });
                    });
                }
            });
        }

        // Vincular la función al cambio en el campo de competición
        $("#id_competicion_id").change(actualizarEncuentros);

        // Llamar a la función al cargar la página para inicializar los encuentros
        actualizarEncuentros();
    });
})(django.jQuery);
