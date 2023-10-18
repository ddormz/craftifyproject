function showNotification(message, type) {
  var alertDiv = $("#notification-alert");
  var alertMessage = alertDiv.find(".alert-message");
  alertMessage.text(message);

  if (type === "success") {
    alertDiv.addClass('alert-success');
  } else if (type === "error") {
    alertDiv.addClass('alert-danger');
  }

  alertDiv.show();

  // Oculta la alerta después de 3 segundos (3000 milisegundos)
  setTimeout(function() {
    alertDiv.hide();
  }, 3000);
};

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

  $('#formAddTrab').on('submit', function(e) {
    e.preventDefault();
    var url = $(this).data("url");
    var form = $(this); // Obtén el formulario actual
    $.ajax({
      url: url,
      method: 'POST',
      data: form.serialize(),
      success: function(data) {
        if (data.success) {
          showNotification("Registro exitoso", "success");
          // Recarga la DataTable
          //table.ajax.reload(); // Esto recargará los datos de la tabla
          // Oculta el modal
          $('#modalAddTrab').modal('hide');
          // Puedes agregar aquí cualquier otro código que desees ejecutar después del éxito.
        } else {
          showNotification("Error al Agregar Trabajador", "error");
          // Puedes agregar aquí cualquier otro código que desees ejecutar en caso de error.
        }
      },
      error: function(data) {
        showNotification("Error al Agregar Trabajador", "error");
      }
    });
    
  });
  
}


document.addEventListener('DOMContentLoaded', globalDataTables);