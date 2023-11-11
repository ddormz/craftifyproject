



$(document).ready(function () {
    $('#btnCategoria').on('click', function (event) {
        $('#modalCategoria').modal('show');
    })
    $('#modalCategoria').on('hidden.bs.modal', function (e) {
        $('#formCategoria').trigger('reset');
    })
    $('.close').on('click', function() {
        $('#modalCategoria').modal('hide');
    
    });
    $('#formCategoria').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_cat');
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: parameters,
            dataType: 'json',
            processData: false,
            contentType: false,
        })
    });
})









