$(document).ready( function () {
    $('#newTabletsTable').DataTable( {
        "columnDefs": [
          { "orderable": false, "targets": [4,5,6] }
        ]
    });
    $('#oldTabletsTable').DataTable( {
        "columnDefs": [
          { "orderable": false, "targets": [4,5,6] }
        ]
    });
    $('#brandsTable').DataTable( {
        "columnDefs": [
          { "orderable": false, "targets": [0] }
        ]
    });
});

$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});

setTimeout(function() {
    $('#notification').hide(1000);
}, 2000); 

$(function () {
    $('[data-toggle="popover"]').popover()
})