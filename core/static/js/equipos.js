var tblEquipo;

// diccionario con array de los trabajadores

var equipo = {
    items: {
        nombre_equipo: '',
        proyecto_id_proyecto: '',
        observaciones: '',
        trabajadores: []
    },

    // agregar trabajadores a la lista
    add: function (item) {
        this.items.trabajadores.push(item);
        this.list();
    },

    // listar 
    list: function () {
        tblEquipo = $('#tblEquipo').DataTable({
            responsive: true,
            autoWidth: true,
            pageLength: 5,
            destroy: true,
            language: {
                url: '../../core/static/js/es-ES.json'
            },
            lengthChange: false,
            data: this.items.trabajadores,
            columns: [
                {"data": "rut"},
                {"data": "rut"},
                {"data": "first_name"},
                {"data": "last_name"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
    },
};

// Equipos
$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });
    // buscador de Trabajadores

    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'buscar_trabajador',
                    'term': request.term,
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            equipo.add(ui.item);
            $(this).val('');
            console.log(equipo.items.trabajadores);
        },
        
        
    });

    $('.btnRemoveAll').on('click', function () {
        if(equipo.items.trabajadores.length === 0) return false;
        alert_action('Eliminar todo', '¿Desea eliminar todos los registros?', function () {
            equipo.items.trabajadores = [];
            tblEquipo.clear().draw();
            equipo.list();
        })

   
    });

        // evento eliminar
        $('#tblEquipo tbody').on('click', 'a[rel="remove"]', function () {
            var tr = tblEquipo.cell($(this).closest('td, li')).index();
            equipo.items.trabajadores.splice(tr.row, 1);
            tblEquipo.row(tr.row).remove().draw(false);
            equipo.list();
        });
    // evento submit 

        $('form').on('submit', function (e) {
            e.preventDefault();

            if (equipo.items.trabajadores.length === 0) {
                message_error('No hay trabajadores la lista');
                return false;
            }
            equipo.items.nombre_equipo = $('input[name="nombre_equipo"]').val();
            equipo.items.proyecto_id_proyecto = $('select[name="proyecto_id_proyecto"]').val();
            equipo.items.observaciones = $('textarea[name="observaciones"]').val();
            console.log(equipo.items);
            var parameters = new FormData();
            parameters.append('action', $('input[name="action"]').val());
            parameters.append('equipo', JSON.stringify(equipo.items));
            submit_with_ajax(window.location.pathname, 'Notificacion', '¿Estas seguro de realizar la siguiente accion?', parameters, function () {
            location.href = '/listarEquipos';
                
            })   
        });
    equipo.list();
});


// evento para reducir el tamaño del textarea 
document.addEventListener('DOMContentLoaded', function () {
    var textarea = document.querySelector('textarea[name="observaciones"]');
    if (textarea) {
        textarea.cols = 4;
        textarea.rows = 4;
        textarea.resize = 'none';
    }
});

