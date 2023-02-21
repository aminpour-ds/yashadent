import { switch_page } from './switchpage.js';

window.onload = about();


function clinic_info(outcome){

    let clinic_logo = "/static/yasha/img/favicon.png";

    $('#site-header').html(`
    <div class="topbar">
        <div class="container">
            <div class="row">
                <div class="col-sm-9 text-sm">
                    <div class="site-info">
                        <a id="header-clinic-phone1" class="fa" style="direction: ltr; text-align: right;"></a>                        
                        <span class="divider">|</span>
                        <a id="header-clinic-email"></a>
                    </div>
                </div>
                <div class="col-sm-2 text-right text-sm">
                    <div class="social-mini-button">                   
                        <a id="instagram-header" target="_blank"><span class="mai-logo-instagram"></span></a>
                        <a id="linkedin-header" target="_blank"><span class="mai-logo-linkedin"></span></a>
                        <a id="whatsapp-header" target="_blank"><span class="mai-logo-whatsapp"></span></a>
                        <a id="telegram-header" target="_blank"><span class="mai-logo-telegram"></span></a>
                    </div>
                </div>
                <div class="col-sm-1 text-center text-sm">
                    <div class="language-info">    
                        <a class="lan" id="language2">فارسی</a>
                        <span class="divider">|</span>
                        <a class="lan" id="language1">انگلیسی</a>
                    </div>
                </div>
            </div> 
        </div> 
    </div>

    <nav class="navbar navbar-expand-lg navbar-light shadow-sm">
        <div class="container">    
            <div class="navbar-header">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar-menu" aria-controls="navbars-rs-food" aria-expanded="false" aria-label="Toggle navigation">
                    <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand" href="/">                    
                    <img src=${clinic_logo} class="logo" alt="" />
                </a>
            </div>
            
            <a class="navbar-brand" href="/"><span class="text-primary">یاشا</span>-دنت</a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupport" aria-controls="navbarSupport" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupport">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                    <a class="nav-link" href="/">صفحه اصلی</a>
                    </li>
                    <li class="nav-itemsite-header">
                    <a class="nav-link" href="/service/1/">خدمات</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="/doctors/">پزشکان</a>
                    </li>
                    
                    <li class="nav-item">
                    <a class="nav-link" href="/partners/">بیمه ها و شرکا</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="/samples/">نمونه کارها</a>
                    </li>
                    <li class="nav-item">
                    <a class="btn btn-primary ml-lg-3" href="/appointment">تعیین وقت</a>
                    </li>
                </ul>
            </div> 
        </div> 
    </nav>
    `); 


    switch_page();

    
    $('#site-footer').html(`
    <div class="container">
      <div class="row px-md-3">
        <div class="col-sm-6 col-lg-4 py-3" style="direction: rtl; text-align: right;">
          <div class="footer-link-info">
            <h5>درباره یاشادنت</h5>
            <ul class="footer-menu footer-menu-fa">
              <li><a href="/about">درباره ما</a></li>              
              <li><a href="/partners">بیمه ها و شرکا</a></li>     
              <li><a href="/appointment">خدمات رایگان</a></li>                                                                             
            </ul>
          </div>
        </div>
        <div class="col-sm-6 col-lg-4 py-3" style="direction: rtl; text-align: right;">
          <div class="footer-link-info">
            <h5>بیشتر</h5>
            <ul class="footer-menu footer-menu-fa">                        
              <li><a href="/samples">نمونه کارها</a></li>                   
              <li><a href="/">تبلیغات</a></li>
              <li><a href="/appointment">درخواست همکاری با ما</a></li>
            </ul>
          </div>
        </div>        
        <div class="col-sm-6 col-lg-4 py-3" style="direction: rtl; text-align: right;">
          <div class="footer-link-info">
            <h5>ارتباط با ما</h5>  
            <ul class="footer-menu footer-menu-fa">  
              <li>                                           
                  <i class="mai-location"></i> آدرس :                   
                  <a id="clinic-country"></a>                                             
                  <a id="clinic-flat"></a>               
              </li>   
              <li>               
                  <i class="mai-call"></i>
                  <lable class="fa">
                  تلفن 1 :
                  </lable>
                  <a id="clinic-phone1" class="fa" style="direction: ltr; text-align: right;"></a>                                
              </li>
              <li>                
                  <i class="mai-call"></i>
                  <lable class="fa">
                  تلفن 2 :            
                  </lable>    
                  <a id="clinic-phone2" class="fa" style="direction: ltr; text-align: right;"></a>                
              </li>
              <li>                
                  <i class="mai-mail"></i> ایمیل :  
                  <a id="clinic-email"></a>                
              </li>
                
            </ul>
            <div class="footer-sosmed mt-3">
                <a id="instagram-footer" target="_blank"><span class="mai-logo-instagram"></span></a>
                <a id="linkedin-footer" target="_blank"><span class="mai-logo-linkedin"></span></a>
                <a id="whatsapp-footer" target="_blank"><span class="mai-logo-whatsapp"></span></a>
                <a id="telegram-footer" target="_blank"><span class="mai-logo-telegram"></span></a>
            </div>
          </div>
        </div>
      </div>  

      <hr>
      <p id="copyright">Copyright &copy; 2023 <a href="https://t.me/PointCast" target="_blank">Point Cast</a>. All right reserved</p>          
    </div>
    `);

    document.getElementById('instagram-header').href= `https://instagram.com/${outcome.results[0].instagram}`
    document.getElementById('linkedin-header').href= `https://www.linkedin.com/in/${outcome.results[0].linkedin}`
    document.getElementById('whatsapp-header').href= `https://whatsapp.com/${outcome.results[0].whatsapp}`
    document.getElementById('telegram-header').href= `https://t.me/${outcome.results[0].telegram}`

    document.getElementById('instagram-footer').href= `https://instagram.com/${outcome.results[0].instagram}`
    document.getElementById('linkedin-footer').href= `https://www.linkedin.com/in/${outcome.results[0].linkedin}`
    document.getElementById('whatsapp-footer').href= `https://whatsapp.com/${outcome.results[0].whatsapp}`
    document.getElementById('telegram-footer').href= `https://t.me/${outcome.results[0].telegram}`

    $('#header-clinic-phone1').html(`<span class="mai-call text-primary"></span> ${outcome.results[0].phone1}`);  
    $('#header-clinic-email').html(`<span class="mai-mail text-primary"></span> ${outcome.results[0].email}`);  
    
    $('#clinic-email').html(`${outcome.results[0].email}`);  
    $('#clinic-phone1').html(`${outcome.results[0].phone1}`);  
    $('#clinic-phone2').html(`${outcome.results[0].phone2}`);  
    $('#clinic-country').html(`${outcome.results[0].country_fa} - ${outcome.results[0].city_fa} - ${outcome.results[0].street_fa} - `);    
    $('#clinic-flat').html(`${outcome.results[0].flat_fa}`);       

    // page-banner photo
    $('#video-welcome').html(`<source type="video/mp4" src=${outcome.results[0].videos[0].video}>`);       
    
    for (let index=0; index < outcome.results[0].images.length; index++){
        if(outcome.results[0].images[index].name == "تعیین وقت" && document.getElementById('image-appointment') != null){
            document.getElementById('image-appointment').style.backgroundImage= `url(${outcome.results[0].images[index].image})`;
        } else if(outcome.results[0].images[index].name == "درباره ما" && document.getElementById('image-about') != null){
            document.getElementById('image-about').style.backgroundImage= `url(${outcome.results[0].images[index].image})`;
        } else if(outcome.results[0].images[index].name == "نمونه کارها" && document.getElementById('image-sample') != null){
            document.getElementById('image-sample').style.backgroundImage= `url(${outcome.results[0].images[index].image})`;
        } else if(outcome.results[0].images[index].name == "پزشکان" && document.getElementById('image-doctor') != null){
            document.getElementById('image-doctor').style.backgroundImage= `url(${outcome.results[0].images[index].image})`;
        } else if(outcome.results[0].images[index].name == "خدمات" && document.getElementById('image-service') != null){
            document.getElementById('image-service').style.backgroundImage= `url(${outcome.results[0].images[index].image})`;
        } else if(outcome.results[0].images[index].name == "بیمه ها و شرکا" && document.getElementById('image-partners') != null){
            document.getElementById('image-partners').style.backgroundImage= `url(${outcome.results[0].images[index].image})`;
        }
    }

    $('.fa').text(toPersian);
}


function about(){              
    let url = '/api/about/';    
    
    const items = fetch(url, {
        method: 'GET',
        headers: {
        Accept: "application/json, text/plain, */*",
        "Content-Type": "application/json",      
        },                
    })
    .then((res) => {
        if (res.status == 200) {
            return res.json();
        } else {
            throw Error(res.statusText);
        }
    })
    .catch((err) => {                    
        console.log(err);
    });

    const info = async () => {
        const a = await items;
        return a;
    };
    
    info().then(function(outcome) {        
        clinic_info(outcome);
    });
}

function toPersian(i,digit){
    if(digit.length<1)
        return;
        
    let e={0:'۰',
        1:'۱',
        2:'۲',
        3:'۳',
        4:'۴',
        5:'۵',
        6:'۶',
        7:'۷',
        8:'۸',
        9:'۹'};

    for ( i=0;i<10;i++)
        digit=digit.replaceAll(i.toString(),e[i]);
    return digit;
}

$(document).ready(function() {$('.fa').text(toPersian)});