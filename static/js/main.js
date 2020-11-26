
    var images = ['/static/images/rcb2.jpg', '/static/images/rcb3.jpg', '/static/images/rcb4.jpg', '/static/images/rcb5.jpg', '/static/images/rcb6.jpg','/static/images/rcb7.jpg'];
    var images1 = ['/static/images/mum2.jpg', '/static/images/mum3.jpg', '/static/images/mum4.jpg', '/static/images/mum5.jpg', '/static/images/mum6.jpg','/static/images/mum7.jpg'];
    var images2 = ['/static/images/csk2.jpg', '/static/images/csk3.jpg', '/static/images/csk4.jpg', '/static/images/csk5.jpg', '/static/images/csk6.jpg','/static/images/csk7.jpg'];
    var images3 = ['/static/images/srh2.jpg', '/static/images/srh3.jpg', '/static/images/srh4.jpg', '/static/images/srh5.jpg', '/static/images/srh6.jpg','/static/images/srh7.jpg'];
    var images4 = ['/static/images/ko2.jpg', '/static/images/ko3.jpg', '/static/images/ko4.jpg', '/static/images/ko5.jpg', '/static/images/ko6.jpg','/static/images/ko7.jpg'];
    var images5 = ['/static/images/raj2.jpg', '/static/images/raj3.jpg', '/static/images/raj4.jpg', '/static/images/raj5.jpg', '/static/images/raj6.jpg','/static/images/raj7.jpg'];
    var images6 = ['/static/images/del2.jpg', '/static/images/del3.jpg', '/static/images/del4.jpg', '/static/images/del5.jpg', '/static/images/del6.jpg','/static/images/del7.jpg'];
    var images7 = ['/static/images/k2.jpg', '/static/images/k3.jpg', '/static/images/k4.jpg', '/static/images/k5.jpg', '/static/images/k6.jpg','/static/images/k7.jpg'];

    var x = 0;
    var x1 = 0;
    var x2 = 0;
    var x3 = 0;
    var x4 = 0;
    var x5 = 0;
    var x6 = 0;
    var x7 = 0;

    var imgs = document.getElementById('img');
    var imgs1 = document.getElementById('img1');
    var imgs2 = document.getElementById('img2');
    var imgs3 = document.getElementById('img3');
    var imgs4 = document.getElementById('img4');
    var imgs5 = document.getElementById('img5');
    var imgs6 = document.getElementById('img6');
    var imgs7 = document.getElementById('img7');

    setInterval(container10, 1000);
    setInterval(container11, 1000);
    setInterval(container12, 1000);
    setInterval(container13, 1000);
    setInterval(container14, 1000);
    setInterval(container15, 1000);
    setInterval(container16, 1000);
    setInterval(container17, 1000);


    function container10() {

      if (x < images.length) {
        x = x + 1;
      } else {
        x = 1;
      }


      imgs.innerHTML = "<img src=" + images[x - 1] + ">";


    }
    function container11() {

      if (x1 < images1.length) {
        x1 = x1 + 1;
      } else {
        x1 = 1;
      }


      imgs1.innerHTML = "<img src=" + images1[x1 - 1] + ">";


    }
    function container12() {

      if (x2 < images2.length) {
        x2 = x2 + 1;
      } else {
        x2 = 1;
      }


      imgs2.innerHTML = "<img src=" + images2[x2 - 1] + ">";


    }
    function container13() {

      if (x3 < images3.length) {
        x3 = x3 + 1;
      } else {
        x3 = 1;
      }


      imgs3.innerHTML = "<img src=" + images3[x3 - 1] + ">";


    }
    function container14() {

      if (x4 < images4.length) {
        x4 = x4 + 1;
      } else {
        x4 = 1;
      }


      imgs4.innerHTML = "<img src=" + images4[x4 - 1] + ">";


    }
    function container15() {

      if (x5 < images5.length) {
        x5 = x5 + 1;
      } else {
        x5 = 1;
      }


      imgs5.innerHTML = "<img src=" + images5[x5 - 1] + ">";


    }
    function container16() {

      if (x6 < images6.length) {
        x6 = x6 + 1;
      } else {
        x6 = 1;
      }


      imgs6.innerHTML = "<img src=" + images6[x6 - 1] + ">";


    }
    function container17() {

      if (x7 < images7.length) {
        x7 = x7 + 1;
      } else {
        x7 = 1;
      }


      imgs7.innerHTML = "<img src=" + images7[x7 - 1] + ">";


    }