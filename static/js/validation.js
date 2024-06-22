document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("contactForm");
    form.addEventListener("submit", function(event) {
        var nombre = document.getElementById("nombre").value;
        var email = document.getElementById("email").value;
        var mensaje = document.getElementById("mensaje").value;
        var motivo = document.getElementById("motivo").value;
        
        if (nombre === "" || email === "" || mensaje === "" || motivo === "" ) {
            alert("Por favor completa todos los campos obligatorios.");
            event.preventDefault();
        } 
        
            
    });
});
