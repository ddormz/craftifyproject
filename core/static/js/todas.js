function todasProdTable() {
    var table = $(".tabla-todas").DataTable({
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
  

}   
  document.addEventListener('DOMContentLoaded', todasProdTable);
  