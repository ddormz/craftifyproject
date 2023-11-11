function avancesTable() {
    var avancesTbl = $(".tabla-avances").DataTable({
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
          'action': 'listarAv'
        },
        dataSrc: '',
      },
      columns: [
        {"data": "tarea.equipo_id_equipo.proyecto_id_proyecto.nombre_proyecto"},
        {"data": "tarea.equipo_id_equipo.nombre_equipo"},
        {"data": "tarea.tarea"},
        {"data": "comentario"},
        {"data": "fecha",
        "render": function (data, type, row) {
          return moment(data).format('DD-MM-YY - HH:mm:ss')
        }
        },
        {"data": "imagen",
        "render": function (data, type, row) {
            return '<a href="#" data-toggle="modal" data-target="#imagenModal"><img src="' + data + '" height="100" width="100" /></a>';
        }
        },
        {"data": "avance_id"},
      ],
      columnDefs: [
        {
          targets: [-1],
          class: 'text-center',
          orderable: false,
          render: function (data, type, row) {
            var buttons = '<a href="/editarAvance/' + row.avance_id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-pen"></i></a> ';
            buttons += '<a rel="remove" href="/eliminarAvance/' + row.avance_id + '/" class="btn btn-danger btn-xs btn-flat" id="botonEliminar"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
          }
        }
      ],
      initComplete: function (settings, json) {
        
      },
      
  });
  // Configura el evento clic para abrir el modal
  $('#imagenModal').on('show.bs.modal', function (event) {
    var imagenUrl = $(event.relatedTarget).find('img').attr('src');
    $(this).find('.modal-body img').attr('src', imagenUrl);
  });
  
}


document.addEventListener('DOMContentLoaded', avancesTable);