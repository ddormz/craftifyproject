var tblProducts;

// diccionario con array de los productos 

var vents = {
    items: {
        cli: '',
        nombre_cotizacion: '',
        comentario: '',
        fecha_cotizacion: '',
        metodo_pago: '',
        subtotal: 0,
        iva: 0.00,
        total: 0.00,
        products: []
    },

    // calculos
    calculate_invoice: function () {
        var subtotal = 0;
        var iva = $('input[name="iva"]').val();
        $.each(this.items.products, function (pos, dict) {
            dict.subtotal = dict.cant * parseFloat(dict.precio_venta);
            subtotal+=dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva / 100;
        this.items.total = this.items.subtotal + this.items.iva;

        $('input[name="subtotal"]').val(this.items.subtotal.toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,}));
        $('input[name="ivacalc"]').val(this.items.iva.toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,  }));
        $('input[name="total"]').val(this.items.total.toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,}));
    },

    // agregar productos a la lista
    add: function (item) {
        this.items.products.push(item);
        this.list();
    },

    // listar 
    list: function () {
        this.calculate_invoice();

        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: true,
            pageLength: 7,
            destroy: true,
            language: {
                url: '../../core/static/js/es-ES.json'
            },
            lengthChange: false,
            data: this.items.products,
            columns: [
                {"data": "id_producto"},
                {"data": "nombre_producto"},
                {"data": "categoria.nombre_categoria"},
                {"data": "precio_venta"},
                {"data": "cant"},
                {"data": "subtotal"},

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
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,});
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cant + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,});
                    }
                },
            ],
            rowCallback(row) {
                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max: 100000000,
                    step: 1,
                })
            },
            initComplete: function (settings, json) {

            }
        });
    },
};

// parte Datos Cotizacion
$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#fecha_cotizacion').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    $("input[name='iva']").on('change', function () {
        vents.calculate_invoice();
    })
    .val(19);

    // buscador de productos

    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
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
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            vents.add(ui.item);
            $(this).val('');
            console.log(vents.items.products);
        }
    });

// evento cantidad

    $('#tblProducts tbody').on('change', 'input[name="cant"]', function () {
        console.clear();
        var cant = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        vents.items.products[tr.row].cant = cant;
        vents.calculate_invoice();
        $('td:eq(5)', tblProducts.row(tr.row).node()).html('$'+vents.items.products[tr.row].subtotal.toLocaleString('es-CL', { minimumFractionDigits: 0, maximumFractionDigits: 0,}));
    });



    // alerta antes de eliminar 

    $('.btnRemoveAll').on('click', function () {
        if(vents.items.products.length === 0) return false;
        alert_action('Eliminar todo', '¿Desea eliminar todos los registros?', function () {
            vents.items.products = [];
            tblProducts.clear().draw();
            vents.list();
        })

   
    });

        // evento eliminar
        $('#tblProducts tbody').on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            vents.items.products.splice(tr.row, 1);
            tblProducts.row(tr.row).remove().draw(false);
            vents.list();
        });
    
    // evento validador solo aceptar numeros en cantidad 
    $('#tblProducts tbody').on('keyup', 'input[name="cant"]', function () {
        
        var cant = parseInt($(this).val());
        if (cant == '0') {
            $(this).val(1);
        } else {
        if (isNaN(cant)) {
            $(this).val(1);
        }
        }
    });

    // evento submit 

    $('form').on('submit', function (e) {
        e.preventDefault();

        if(vents.items.products.length === 0) {
            message_error('No hay productos en la lista');
            return false;
        }

        vents.items.fecha_cotizacion = $('input[name="fecha_cotizacion"]').val();
        vents.items.cli = $('select[name="cliente"]').val();
        vents.items.nombre_cotizacion = $('input[name="nombre_cotizacion"]').val();
        vents.items.metodo_pago = $('select[name="metodopago"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificacion', '¿Estas seguro de realizar la siguiente accion?', parameters, function () {
           location.href = '/listarCotizaciones';
            
        })   
    });
    vents.list();
});


// evento para reducir el tamaño del textarea 
document.addEventListener('DOMContentLoaded', function () {
    var textarea = document.querySelector('textarea[name="comentario"]');
    if (textarea) {
        textarea.cols = 4;
        textarea.rows = 3;
        textarea.resize = 'none';
    }
});

