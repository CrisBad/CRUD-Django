(function(){

    const btnEliminar=document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn=>{
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Está seguro de eliminar el estudiante?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
    
})();