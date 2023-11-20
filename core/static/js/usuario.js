$(function () {
   $('.select2').select2({
       theme: 'bootstrap4',
       language: 'es',
       dropdownParent: $('#modalAddTrab'),
       dropdownOrientation: 'bottom',
       placeholder: 'Seleccionar...'
   })
   $('#modalAddTrab').modal('handleUpdate')
})