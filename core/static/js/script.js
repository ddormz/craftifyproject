$(function(){
    
    modal_title = $('.modal-title');

    getData();

    $('.btnAdd').on('click', function() {})

    $('#data tbody').on('click', 'a', function() {
        alert('xd')
    })


    
})


$(function (DataTable) {
    $("#example1").DataTable({
      "responsive": true, "lengthChange": false, "autoWidth": false,
      "buttons": ["pdf","colvis"]
    }).buttons().container().appendTo('#example1_wrapper .col-md-6:eq(0)');

  });
