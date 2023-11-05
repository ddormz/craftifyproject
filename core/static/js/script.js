function equiposTable() {
  var tblEquipo = $(".tabla-equipos").DataTable({
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
    ajax: {
      url: window.location.pathname,
      type: 'POST',
      data: {
        'action': 'listarEq'
      },
      dataSrc: '',
    },
    columns: [
      {"data": "id_equipo"},
      {"data": "nombre_equipo"},
      {"data": "proyecto_id_proyecto.nombre_proyecto"},
      {"data": "observaciones"},
      {"data": "id_equipo"}, 
    ],
    columnDefs: [
      {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
          var buttons = '<a rel="remove" href="/eliminarEquipo/' + row.id_equipo + '/" class="btn btn-danger btn-xs btn-flat" id="botonEliminar"><i class="fas fa-trash-alt"></i></a>';
          buttons += '<a href="/editarEquipo/' + row.id_equipo + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-pen"></i></a> ';
          buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';  
          buttons += '<a href="/" class="btn btn-dark btn-xs btn-flat"><i class="fa-solid fa-list-check" style="color: white;"></i></a>';
          return buttons;
      }
      },  
    ],
    initComplete: function (settings, json) {
      
    },
    
});

  $('.tabla-equipos tbody')
    .on('click', 'a[rel="details"]', function () {
        var tr = tblEquipo.cell($(this).closest('td, li')).index();
        var data = tblEquipo.row(tr.row).data();
        console.log(data);
        
        $('#tblDetalleEquipo').DataTable({
          responsive: true,
          autoWidth: false,
          destroy: true,
          deferRender: true,
          lengthChange: false,
          language: {
              url: '../../core/static/js/es-ES.json'
          },
          ajax: {
              url: window.location.pathname,
              type: 'POST',
              data: {
                  'action': 'detalleEquipo',
                  'id_equipo': data.id_equipo
              },
              dataSrc: ""
          },
          columns: [
              {"data": "trabajador.rut"},
              {"data": "trabajador.first_name"},
              {"data": "trabajador.last_name"},
          ],
          initComplete: function (settings, json) {

          }
      });
      

      $('#ModalEquipo').modal('show');

      $('.close').on('click', function() {
        $('#ModalEquipo').modal('hide');
    });
    }); 
  }

function proyectosTable() {
  var table = $(".tabla-proyectos").DataTable({
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
    "columnDefs": [
      {
        "targets": [-3], // El índice de la columna "Status" (0-based)
        "render": function (data, type, row) {
          if (data === "Cotizado") {
            return '<div class="badge rounded-pill bg-primary" style="width:100%">' + data + '</div></div>';
          } else if (data === "Aceptado") {
            return '<div class="badge rounded-pill bg-success" style="width:100%">' + data + '</div></div>';
          } else if (data === "Producción") {
            return '<div class="badge rounded-pill bg-warning" style="width:100%">' + data + '</div></div>';
          } else if (data === "Por Instalar") {
            return '<div class="badge rounded-pill bg-danger" style="width:100%">' + data + '</div></div>';
          } else if (data === "Terminado") {
            return '<div class="badge rounded-pill bg-dark" style="width:100%">' + data + '</div></div>';
          }
          return data;
        },
        "data": "Status" // Nombre de la columna de datos "Status"
      },
      {
        "targets": [-2], // Columna "Tiempo Restante"
        "render": function (data, type, row) {
          // Utiliza una expresión regular para extraer solo el número
          var tiempoRestante = parseInt(data.match(/\d+/));
          var badgeClass = "";

          if (tiempoRestante > 15) {
            return '<div class="badge rounded-pill bg-success">' + tiempoRestante + ' días</div>';
          } else if (tiempoRestante > 7) {
            return '<div class="badge rounded-pill bg-warning">' + tiempoRestante + ' días</div>';
          } else if (tiempoRestante >= 0) {
            return '<div class="badge rounded-pill bg-danger">' + tiempoRestante + ' días</div>';
          } else {
            return '<div class="badge rounded-pill bg-danger">Vencido</div>';
          }
        },
        "targets": [-2]
      }
    ]
  });

  // Mover los botones a la esquina superior derecha
  var buttonsContainer = table.buttons().container();
  buttonsContainer.appendTo($('#tarjetaTablas'));
  buttonsContainer.addClass('float-left');
};




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
  var tblCot = $(".tabla-cotizaciones").DataTable({
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
    ajax: {
      url: window.location.pathname,
      type: 'POST',
      data: {
        'action': 'listarCot'
      },
      dataSrc: '',
    },
    columns: [
      {"data": "id_cotizacion"},
      {"data": "fecha_cotizacion"},
      {"data": "nombre_cotizacion"},
      {
        "data": "cliente.nombre",
        "render": function(data, type, row) {
          if (type === 'display') {
            // Concatenar nombre y apellido si el tipo de render es 'display'
            return row.cliente.nombre + ' ' + row.cliente.apellido;
          }
          // De lo contrario, muestra solo el nombre
          return data;
        }
      },
      {"data": "total"},
      {"data": "metodopago.nombre_metodo"},
      {"data": "id_cotizacion"},
    ],
    columnDefs: [
      {
          targets: [4],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
              return '$' + parseFloat(data).toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,});
          },  
      },
      {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
            var buttons = '<a rel="remove" href="/eliminarCotizaciones/' + row.id_cotizacion + '/" class="btn btn-danger btn-xs btn-flat" id="botonEliminar"><i class="fas fa-trash-alt"></i></a>';
            buttons += '<a href="/editarCotizaciones/' + row.id_cotizacion + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-pen"></i></a> ';
            buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';  
            buttons += '<a href="/cotpdf/' + row.id_cotizacion + '/" class="btn btn-dark btn-xs btn-flat"><i class="fa-solid fa-file-pdf" style="color: white;"></i></a>';
            return buttons;
        }
    },
    ],
    initComplete: function (settings, json) {
      
    },
    
});

// CONFIRMACION DE ELIMINAR EN COTIZACIONES 
 /* $(document).on('click', 'a[rel="remove"]', function (event) {
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
  })
  */



  $('.tabla-cotizaciones tbody')
  .on('click', 'a[rel="details"]', function () {
      var tr = tblCot.cell($(this).closest('td, li')).index();
      var data = tblCot.row(tr.row).data();
      console.log(data);
      
      $('#tblDetalle').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        lengthChange: false,
        language: {
            url: '../../core/static/js/es-ES.json'
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'detalleCot',
                'id_cotizacion': data.id_cotizacion
            },
            dataSrc: ""
        },
        columns: [
            {"data": "producto.nombre_producto"},
            {"data": "producto.categoria.nombre_categoria"},
            {"data": "producto.subcategoria.nombre_subcategoria"},
            {"data": "precio"},
            {"data": "cantidad"},
            {"data": "subtotal"},
        ],
        columnDefs: [
            {
            targets: [-1, -3],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '$' + parseFloat(data).toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,});
            }
            }
        ],
        initComplete: function (settings, json) {

        }
    });

    $('#ModalDetalle').modal('show');

    $('.close').on('click', function() {
      $('#ModalDetalle').modal('hide');
  });
  });


// ELIMINAR GLOBAL

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
document.addEventListener('DOMContentLoaded', proyectosTable);
document.addEventListener('DOMContentLoaded', equiposTable);