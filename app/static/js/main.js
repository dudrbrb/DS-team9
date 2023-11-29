window.addEventListener('load', ()=>{

    var mySwiper = new Swiper(".mySwiper", {
        direction: "vertical",
        mousewheel: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
      });

    var friendsSwiper = new Swiper(".friendsSwiper", {
        slidesPerView: 3.2,
        spaceBetween: 30,
      });
});