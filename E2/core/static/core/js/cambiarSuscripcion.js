function cambiarSuscripcion(id){
    //console.log("ID PRODUCTO: "+id);
    Swal.fire({
      title: 'Cambiar',
      text: '¿Desea cambiar su suscripcion?',
      icon: 'info',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      cancelButtonText: 'No',
      confirmButtonText: 'Si'
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "/updateSuscripcion/"+id+"/";
      }
    })
}