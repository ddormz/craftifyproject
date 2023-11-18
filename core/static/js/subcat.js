function subProdTable() {
    var table = $(".tabla-subprod").DataTable({
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
      ],
    });
  
    // Mover los botones a la esquina superior derecha
    var buttonsContainer = table.buttons().container();
    buttonsContainer.appendTo($('#tarjetaTablas'));
    buttonsContainer.addClass('float-left');
  
    // Editar Registro de la Tabla
  
    $('.tabla-datos tbody').on('click', '.botonEditar', function() {
      var data = table.row($(this).parents('tr')).data();
      
      console.log(data)
      

    // Agregar Registro 


    });


  // Agregar Registro Trabajador
$(document).ready(function() {
    $("#formSub").on("submit", function(event) {
      event.preventDefault();
      var url = $(this).data("url"); // Obtén la URL del atributo data-url
      $.ajax({
        url: url,
        method: "POST",
        data: $(this).serialize(),
        success: function(data) {
          // Muestra una alerta de toast antes de recargar la página
          toastr.success('Registro exitoso', 'Éxito', {
            timeOut: 500,
            closeButton: false,
            tapToDismiss: false,
            positionClass: "toast-top-center",
            preventDuplicates: true,
            onHidden: function() {
              // La alerta se ocultó, ahora recarga la página
              location.reload(); // Esto recargará la página actual
            }
          });
        },
        error: function(data) {
          toastr.error('Error al agregar  ', 'Error', {
            timeOut: 2000,
            closeButton: false,
            tapToDismiss: false,
            positionClass: "toast-top-center",
            preventDuplicates: true
          });
        }
      });
    });
  });

}   
  document.addEventListener('DOMContentLoaded', subProdTable);
  