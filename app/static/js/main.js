window.addEventListener('load', ()=>{

    var swiper = new Swiper(".mySwiper", {
        direction: "vertical",
        mousewheel: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
      });
});