function confirmarSuscripcion(id){
    //console.log("ID PRODUCTO: "+id);
    Swal.fire({
      title: 'Confirmar',
      text: '¿Desea confirmar su suscripcion?',
      icon: 'info',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      cancelButtonText: 'Cancelar',
      confirmButtonText: 'Confirmar'
    }).then((result) => {
      if (result.isConfirmed) {
        swal.fire('Gracias!','Suscripcion realizada correctamente', 'success').then(function(){
            window.location.href = "/addSuscripcion/"+id+"/";
        })
      }
    })
  }