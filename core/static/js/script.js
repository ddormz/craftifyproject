function globalDataTables() {
  var table = $(".tabla-datos").DataTable({
    "responsive": true,
    "lengthChange": false,
    "autoWidth": false,
    "language": {
      "url": '../../core/static/js/es-ES.json'
    },
    "dom": 'Bfrtip', // Esto habilita los botones en la parte superior
    "buttons": [
      {
        text: 'Exportar a PDF',
        extend: 'pdfHtml5'
      },
      {
        text: 'Visibilidad de Columnas',
        extend: 'colvis'
      }
    ]
  });

  // Mover los botones a la esquina superior derecha
  var buttonsContainer = table.buttons().container();
  buttonsContainer.appendTo($('#tarjetaTablas'));
  buttonsContainer.addClass('float-left');


};

document.addEventListener('DOMContentLoaded', globalDataTables);

// registro.js
$(document).ready(function() {
  $("#formAddTrab").on("submit", function(event) {
    event.preventDefault();
    var url = $(this).data("url"); // Obtén la URL del atributo data-url
    $.ajax({
      url: url,
      method: "POST",
      data: $(this).serialize(),
      success: function(data) {
        // Muestra una alerta de toast antes de recargar la página
        toastr.success('Registro exitoso', 'Éxito', {
          timeOut: 1000,
          closeButton: false,
          tapToDismiss: false,
          onHidden: function() {
            // La alerta se ocultó, ahora recarga la página
            location.reload(); // Esto recargará la página actual
          }
        });
      },
      error: function(data) {
        toastr.error('Error en el registro', 'Error', {
          timeOut: 1000,
          closeButton: false,
          tapToDismiss: false

        })
      }
    });
  });
});


