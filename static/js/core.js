// search box
searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () =>{
    searchForm.classList.toggle('active');
}


// close notification 
arlet = document.querySelector('.alert');

document.querySelector('#close-btn').onclick = () =>{
    arlet.classList.toggle('hide');
}

// user open dropdown 
dropdown = document.querySelector('.dropdown-content');

document.querySelector('#login-btn').onclick = () =>{
  dropdown.classList.toggle('show');
}



// keep navbar
window.onscroll = () =>{

    searchForm.classList.remove('active');

    if(window.scrollY > 80){
        document.querySelector('.header .header-2').classList.add('active');
    }else{
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

window.onload = () =>{

    if(window.scrollY > 80){
        document.querySelector('.header .header-2').classList.add('active');
    }else{
        document.querySelector('.header .header-2').classList.remove('active');
    }
}







// swiper books
var swiper = new Swiper(".books-slider", {
    loop:true,
    centeredSlides:true,
    autoplay:{
        delay:9500,
        disableOnInteraction:false,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });





//   featured
var swiper = new Swiper(".featured-slider", {
    loop:true,
    spaceBetween:10,
    centeredSlides:true,
    autoplay:{
        delay:9500,
        disableOnInteraction:false,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      450: {
        slidesPerView: 2,
      },
      768: {
        slidesPerView: 3,
      },
      1024: {
        slidesPerView: 4,
      },
    },
  });





  // arrivals
  var swiper = new Swiper(".arrivals-slider", {
    loop:true,
    spaceBetween:10,
    centeredSlides:true,
    autoplay:{
        delay:9500,
        disableOnInteraction:false,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });



  // reviews
  var swiper = new Swiper(".reviews-slider", {
    loop:true,
    spaceBetween:10,
    grabCursor:true,
    centeredSlides:true,
    autoplay:{
        delay:9500,
        disableOnInteraction:false,
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
  });  

