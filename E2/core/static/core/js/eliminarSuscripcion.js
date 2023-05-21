function eliminarSuscripcion(id){
    //console.log("ID PRODUCTO: "+id);
    Swal.fire({
      title: 'Cancelar',
      text: '¿Desea cancelar su suscripcion?',
      icon: 'info',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      cancelButtonText: 'No',
      confirmButtonText: 'Si'
    }).then((result) => {
      if (result.isConfirmed) {
        swal.fire('No hay problema!','Suscripcion cancelada correctamente', 'success').then(function(){
            window.location.href = "/deleteSuscripcion/"+id+"/";
        })
      }
    })
}