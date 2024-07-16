var tblTareas;

function productosTable() {
  var tblProductos = $(".tabla-productos").DataTable({
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
        'action': 'listarProductos',
        'id_producto': 'id_producto'
      },
      dataSrc: '',
    },
    columns: [
      {"data": "id_producto"},
      {
        "data": "imagen",
        render: function (data, type, row) {
            if (data) {
              return '<img src="' + data + '" alt="Imagen" style="max-width: 100px; max-height: 100px; cursor: pointer;" data-toggle="modal" data-target="#imagenModal" />';
            } else {
                // Si no hay imagen, mostrar la imagen por defecto o en blanco
                return '<img src="{{ url_for("static", filename="img/default.jpg") }}" alt="Sin imagen" style="max-width: 100px; max-height: 100px;" />';
            }
        }
    },
      {"data": "nombre_producto"},
      {"data": "descripcion"},
      {"data": "categoria.nombre_categoria"},
      {"data": "subcategoria.nombre_subcategoria"},
      {"data": "marca.nombre_marca"},
      {"data": "precio_compra"},
      {"data": "precio_venta"},
      {"data": "stock"},
      {"data": "variante",},
      {"data": "id_producto"},
    ],
    columnDefs: [
      {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
          var buttons = '<a rel="remove" href="/eliminarProductos/' + row.id_producto + '/" class="btn btn-danger btn-xs btn-flat" id="botonEliminar"><i class="fas fa-trash-alt"></i></a>';
          buttons += '<a href="/editarProductos/' + row.id_producto + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-pen"></i></a> ';  
          return buttons;
      },
    },
      {
        targets: [-4,-5],
        class: 'text-center',
        render: function (data, type, row) {
          return '$' + parseFloat(data).toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0, });
        }

      },
      {
        targets: [-3],
        class: 'text-center',
        render: function (data, type, row) {
          if (data >= 1) {
            if (data > 7) {
              return '<div class="badge bg-success" style="width:100%">' + 'Existencia: ' + data + '</div>';
            } else {
              return '<div class="badge bg-warning" style="width:100%">' + 'Existencia: ' + data + '</div>';
            }
          } else {
            return '<span class="badge bg-danger">Agotado</span>';
          }
        }
        

      },
    ],
    initComplete: function (settings, json) {
    }
  })
}



$(document).ready(function () {
  $('#formProd').on('submit', function (event) {
    event.preventDefault(); // Prevenir el envío automático del formulario

    var formData = new FormData(this);

    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // Mostrar notificación de éxito
        $('#toast').text('Registro exitoso del producto').removeClass('alert-danger').addClass('alert-success').show();
        setTimeout(function () {
          $('#toast').hide();
        }, 3000); // Ocultar la notificación después de 3 segundos
        
        // Restablecer el formulario
        $('#formProd')[0].reset();
      },
      error: function (xhr, errmsg, err) {
        // Mostrar notificación de error
        $('#toast').text('Registro fallido').removeClass('alert-success').addClass('alert-danger').show();
        setTimeout(function () {
          $('#toast').hide();
        }, 2000);
        console.log(xhr.status + ": " + xhr.responseText); // Mostrar detalles del error en la consola
        // Ocultar la notificación después de 3 segundos
      }
    });
  });
});


$(document).ready(function () {
  $('#formEditProd').on('submit', function (event) {
    event.preventDefault(); // Prevenir el envío automático del formulario
    var formData = new FormData(this);

    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // Mostrar notificación de éxito
        $('#toast').text('Actualizacion exitoso del producto').removeClass('alert-danger').addClass('alert-success').show();
        setTimeout(function () {
          $('#toast').hide();
          window.location.href = '/listarProductos'; // Reemplaza con la URL correcta
  }, 1500); // Ocultar la notificación después de 2 segundos        
      },
      error: function (xhr, errmsg, err) {
        // Mostrar notificación de error
        $('#toast').text('Registro fallido').removeClass('alert-success').addClass('alert-danger').show();
        setTimeout(function () {
          $('#toast').hide();
        }, 2000); // Ocultar la notificación después de 3 segundos
      }
    });
  });
});

$(document).ready(function () {
  $('#formProyecto').on('submit', function (event) {
    event.preventDefault(); // Prevenir el envío automático del formulario
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      success: function (response) {
        // Mostrar notificación de éxito
        $('#toast').text('Proyecto Agregado Exitosamente').removeClass('alert-danger').addClass('alert-success').show();
        setTimeout(function () {
          $('#toast').hide();
          window.location.href = '/verproyectos'; // Reemplaza con la URL correcta
  }, 1500); // Ocultar la notificación después de 2 segundos        
      },
      error: function (xhr, errmsg, err) {
        // Mostrar notificación de error
        $('#toast').text('Proyecto no puede ser agregado, verifique los campos').removeClass('alert-success').addClass('alert-danger').show();
        setTimeout(function () {
          $('#toast').hide();
        }, 2000); // Ocultar la notificación después de 3 segundos
      }
    });
  });
});

$(function () {
  $('.select2').select2({
      theme: "bootstrap4",
      language: 'es'
  });

});


$(document).ready(function () {
  $('#formEditProyecto').on('submit', function (event) {
    event.preventDefault(); // Prevenir el envío automático del formulario
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      success: function (response) {
        // Mostrar notificación de éxito
        $('#toast').text('Proyecto Actualizado Exitosamente').removeClass('alert-danger').addClass('alert-success').show();
        setTimeout(function () {
          $('#toast').hide();
          window.location.href = '/verproyectos'; // Reemplaza con la URL correcta
  }, 1500); // Ocultar la notificación después de 2 segundos        
      },
      error: function (xhr, errmsg, err) {
        // Mostrar notificación de error
        $('#toast').text('Proyecto no puede ser actualizado, verifique los campos').removeClass('alert-success').addClass('alert-danger').show();
        setTimeout(function () {
          $('#toast').hide();
        }, 2000); // Ocultar la notificación después de 3 segundos
      }
    });
  });
});


function tareasTable() {
   tblTareas = $(".tabla-tareas").DataTable({
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
        'action': 'listarTareas'
      },
      dataSrc: '',
    },
    columns: [
      {"data": "tarea_id"},
      {"data": "equipo_id_equipo.nombre_equipo"},
      {"data": "equipo_id_equipo.proyecto_id_proyecto.nombre_proyecto"},
      {"data": "tarea"},
      {"data": "trabajador.first_name"},
      {"data": "fecha_asignacion"},
      {"data": "fecha_termino"},
      {"data": "status_tarea.nombre_status"},
      {"data": "tarea_id"},

    ],
    columnDefs: [
      {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
          var buttons = '<a rel="remove" href="/eliminarTareas/' + row.tarea_id + '/" class="btn btn-danger btn-xs btn-flat" id="botonizar"><i class="fas fa-trash-alt"></i></a>';
          buttons += '<a href="/editarTareas/' + row.tarea_id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-pen"></i></a> ';
          return buttons;
        }
      }
      

    ],
    initComplete: function (settings, json) {
      var selectEquipo = $('#filtroEquipo');
      var selectProyecto = $('#filtroProyecto');
    
      // Obtener una lista única de nombres de equipos y proyectos
      var equipos = tblTareas.column(1).data().unique().toArray();
      var proyectos = tblTareas.column(2).data().unique().toArray();
    
      // Llenar los elementos <select> con las opciones
      equipos.forEach(function (equipo) {
        selectEquipo.append('<option value="' + equipo + '">' + equipo + '</option>');
      });
    
      proyectos.forEach(function (proyecto) {
        selectProyecto.append('<option value="' + proyecto + '">' + proyecto + '</option>');
      });
    
      // Agregar eventos de cambio a los filtros
      selectEquipo.on('change', function () {
        var equipoSeleccionado = $(this).val();
        tblTareas.column(1).search(equipoSeleccionado).draw();
      });
    
      selectProyecto.on('change', function () {
        var proyectoSeleccionado = $(this).val();
        tblTareas.column(2).search(proyectoSeleccionado).draw();
      });
    },
  });
}

$(document).ready(function() {
  var tablaTareas = $('.tabla-tareas').DataTable();

  // Manejar el envío del formulario de filtro
  $('#filtroForm').submit(function(e) {
    e.preventDefault();
    var fechaInicio = $('#fechaInicio').val();
    var fechaFin = $('#fechaFin').val();

    // Aplicar el filtro de fecha de creación
    tablaTareas.column(5).search(fechaInicio + ' to ' + fechaFin).draw();
  });
});
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
          buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';  
          buttons += '<a href="/listarTareas" class="btn btn-dark btn-xs btn-flat tareaID"><i class="fa-solid fa-list-check" style="color: white;"></i></a>';
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
    



    
  };
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
          } else if (tiempoRestante > 0) {
            return '<div class="badge rounded-pill bg-warning">' + tiempoRestante + ' días</div>';
          } else {
            return '<div class="badge rounded-pill bg-danger">Vencido</div>';
          }
        },
      },
      {
        "targets": [5],
        "render": function (data, type, row) {
          if (data == "True") {
            return '<div class="badge rounded-pill bg-success">Si</div>';
          } else {
            return '<div class="badge rounded-pill bg-danger">No</div>';
          }
          }
        }
    ],
    

  });

  
  $(document).ready(function() {
    var tablaProyectos = $('.tabla-proyectos').DataTable();
  
    // Función para extraer el año de una fecha en formato "26 de Junio de 2024"
    function extraerAnio(fecha) {
      return new Date(fecha.replace(/de /g, "").replace(/ /g, "-")).getFullYear();
    }
  
    // Obtener los años únicos de la columna de fechas
    var años = new Set();
    tablaProyectos.column(6).data().each(function(value, index) {
      años.add(extraerAnio(value));
    });
  
    // Convertir el Set a un array y ordenarlo
    años = Array.from(años).sort();
  
    // Añadir los años como opciones al select
    var anioFiltro = $('#anioFiltro');
    años.forEach(function(anio) {
      anioFiltro.append(new Option(anio, anio));
    });
  
    // Obtener los clientes únicos de la columna de clientes
    var clientes = new Set();
    tablaProyectos.column(2).data().each(function(value, index) {
      clientes.add(value);
    });
  
    // Convertir el Set a un array y ordenarlo
    clientes = Array.from(clientes).sort();
  
    // Añadir los clientes como opciones al select
    var clienteFiltro = $('#ClienteFiltro');
    clientes.forEach(function(cliente) {
      clienteFiltro.append(new Option(cliente, cliente));
    });
  
    // Filtro personalizado para DataTables
    $.fn.dataTable.ext.search.push(
      function(settings, data, dataIndex) {
        var anioSeleccionado = $('#anioFiltro').val();
        var clienteSeleccionado = $('#ClienteFiltro').val();
        var fechaTabla = data[6]; // La columna que contiene las fechas
        var clienteTabla = data[2]; // La columna que contiene los clientes
  
        // Filtrar por año
        if (anioSeleccionado !== "") {
          var anioTabla = extraerAnio(fechaTabla);
          if (anioSeleccionado != anioTabla) {
            return false;
          }
        }
  
        // Filtrar por cliente
        if (clienteSeleccionado !== "" && clienteSeleccionado != clienteTabla) {
          return false;
        }
  
        return true;
      }
    );
  
    // Redibujar la tabla cuando se selecciona un año o cliente
    $('#anioFiltro, #ClienteFiltro').change(function() {
      tablaProyectos.draw();
    });
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
        toastr.error('Error al agregar trabajador, verifica los campos.', 'Error', {
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
  let minDate, maxDate;
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
    {"data": "fecha_cotizacion",
        "render": function(data, type, row) {
            if (type === 'display' || type === 'filter') {
                // Convertir la fecha al formato dd-mm-yyyy
                var date = new Date(data);
                var day = date.getDate();
                var month = date.getMonth() + 1;
                var year = date.getFullYear();
                // Asegurarse de que el día y el mes tengan dos dígitos
                if (day < 10) {
                    day = '0' + day;
                }
                if (month < 10) {
                    month = '0' + month;
                }
                return day + '-' + month + '-' + year;
            }
            return data;
        }
    },
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
      {"data": "formapago.nombre_formapago"},
      {"data": "status.nombre_status"},
      {
        "data": "generado_por",  // Esta debe ser la propiedad que contiene el nombre completo
        "render": function(data, type, row) {
            // Aquí puedes formatear el nombre completo utilizando los datos disponibles
            return row.generado_por.first_name + ' ' + row.generado_por.last_name;
        }
    },
      {"data": "abono"}, 
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
            buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';  
            buttons += '<a href="/cotpdf/' + row.id_cotizacion + '/" class="btn btn-dark btn-xs btn-flat"><i class="fa-solid fa-file-pdf" style="color: white;"></i></a>';
            return buttons;
        }
    },
    ],
    initComplete: function (settings, json) {
      // Crear inputs de fecha
      minDate = new DateTime('#min', {
        format: 'MMMM Do YYYY'
      });
      maxDate = new DateTime('#max', {
        format: 'MMMM Do YYYY'
      });

      // Refiltrar la tabla
      document.querySelectorAll('#min, #max').forEach((el) => {
        el.addEventListener('change', () => {
          tblCot.draw();
        });
      });

      // Extensión de búsqueda personalizada para el rango de fecha
      $.fn.dataTable.ext.search.push(function (settings, data, dataIndex) {
        let min = minDate.val();
        let max = maxDate.val();
        let date = new Date(data[1]); // Índice 1 es la columna de fecha

        if (
          (min === null && max === null) ||
          (min === null && date <= max) ||
          (min <= date && max === null) ||
          (min <= date && date <= max)
        ) {
          return true;
        }
        return false;
      });
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
document.addEventListener('DOMContentLoaded', tareasTable);
document.addEventListener('DOMContentLoaded', productosTable);