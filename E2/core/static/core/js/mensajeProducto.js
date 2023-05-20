function deleteProducto(id){
    //console.log("ID PRODUCTO: "+id);
    Swal.fire({
      title: 'Eliminar',
      text: 'Desea eliminar los datos?',
      icon: 'info',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      cancelButtonText: 'Cancelar',
      confirmButtonText: 'Eliminar'
    }).then((result) => {
      if (result.isConfirmed) {
        swal.fire('Eliminado!','Producto eliminado correctamente', 'success').then(function(){
            window.location.href = "/deleteProducto/"+id+"/";
        })
      }
    })
}