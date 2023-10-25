// Tabla Trabajadores
function trabajadoresTable() {
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
    
});

};



// Agregar Registro Trabajador

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
        toastr.error('Error al agregar trabajador ', 'Error', {
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

// Tabla Cotizaciones
function cotizacionesTable() {
  var table = $(".tabla-cotizaciones").DataTable({
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
    columnDefs: [
      {
          targets: [-2],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
              return '$' + parseFloat(data).toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,});
          },  
      },
    ]
  });
  
  $('.botonEliminar').on('click', function(event) {
    event.preventDefault(); // Evita que el enlace se siga inmediatamente

    var url = $(this).attr('href'); // Obtén la URL desde el atributo href

    $.confirm({
        theme: 'material',
        icon: 'fa fa-info',
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        title: 'Confirmar acción',
        content: '¿Estás seguro de que deseas eliminar este registro?',
        buttons: {
          info: {
              text: "Si",
              btnClass: 'btn-primary',
              action: function () {
                window.location = url;
              }
          },
          danger: {
              text: "No",
              btnClass: 'btn-red',
              action: function () {

              }
          },
      }
    });
});






};
document.addEventListener('DOMContentLoaded', cotizacionesTable);
document.addEventListener('DOMContentLoaded', trabajadoresTable);