document.addEventListener('DOMContentLoaded', function () {
    const prevBtn = document.querySelector('.carousel-control-prev');
    const nextBtn = document.querySelector('.carousel-control-next');
    const carouselItems = document.querySelectorAll('.carousel-item');
    let currentSlide = 0;

    // Event listener para la flecha de anterior
    prevBtn.addEventListener('click', function () {
        currentSlide--;
        if (currentSlide < 0) {
            currentSlide = carouselItems.length - 1;
        }
        updateCarousel();
    });

    // Event listener para la flecha de siguiente
    nextBtn.addEventListener('click', function () {
        currentSlide++;
        if (currentSlide >= carouselItems.length) {
            currentSlide = 0;
        }
        updateCarousel();
    });

    // Función para actualizar el carrusel
    function updateCarousel() {
        carouselItems.forEach(function (item, index) {
            if (index === currentSlide) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }
});
