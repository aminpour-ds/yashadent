window.onload = about();


function clinic_info(outcome){   

    clinic_logo = "/static/yasha/img/favicon75.png";

    $('#site-header').html(`
    <div class="topbar">
        <div class="container">
            <div class="row">
                <div class="col-sm-8 text-sm">
                    <div class="site-info">
                        <a href="#" id="header-clinic-phone1"></a>
                        <span class="divider">|</span>
                        <a href="#" id="header-clinic-email"></a>
                    </div>
                </div>
                <div class="col-sm-4 text-right text-sm">
                    <div class="social-mini-button">
                        <a href="#"><span class="mai-logo-instagram"></span></a>
                        <a href="#"><span class="mai-logo-linkedin"></span></a>
                        <a href="#"><span class="mai-logo-whatsapp"></span></a>
                        <a href="#"><span class="mai-logo-telegram"></span></a>
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
            
            <a class="navbar-brand" href="/"><span class="text-primary">Yasha</span>-Dent</a>

            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupport" aria-controls="navbarSupport" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupport">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                    <a class="nav-link" href="/">HOME</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="/service/1">OUR SERVICES</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="/doctors">DOCTORS</a>
                    </li>
                    
                    <li class="nav-item">
                    <a class="nav-link" href="/insurance">INSURANCE INFO</a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link" href="/questions">YOUR QUESTIONS</a>
                    </li>
                    <li class="nav-item">
                    <a class="btn btn-primary ml-lg-3" href="/appointment">BOOK NOW</a>
                    </li>
                </ul>
            </div> 
        </div> 
    </nav>
    `); 

    $('#site-footer').html(`
    <div class="container">
      <div class="row px-md-3">
        <div class="col-sm-6 col-lg-4 py-3">
          <div class="footer-link-info">
            <h5>About The Clinic</h5>
            <ul class="footer-menu">
              <li><a href="#">Our Sitemap</a></li>
              <li><a href="#">Our Team</a></li>
              <li><a href="#">Our Partners</a></li>
              <li><a href="#">Hours</a></li>                                                                   
            </ul>
          </div>
        </div>
        <div class="col-sm-6 col-lg-4 py-3">
          <div class="footer-link-info">
            <h5>More</h5>
            <ul class="footer-menu">          
              <li><a href="#">Free Customer Services</a></li>  
              <li><a href="#">advices and Questions</a></li>                   
              <li><a href="#">Advertise</a></li>
              <li><a href="#">Join as Doctors</a></li>
            </ul>
          </div>
        </div>        
        <div class="col-sm-6 col-lg-4 py-3">
          <div class="footer-link-info">
            <h5>Contact Us</h5>  
            <ul class="footer-menu">  
              <li>                                           
                  <i class="mai-location"></i> Address : 
                  <a href="#" id="clinic-flat"></a>               
                  <br />
                  <a id="clinic-street"></a>
                  <br />
                  <a id="clinic-city"></a>              
                  <a id="clinic-country"></a>                         
              </li>   
              <li>               
                  <i class="mai-call"></i> Phone1 :
                  <a href="#" id="clinic-phone1"></a>                                
              </li>
              <li>                
                  <i class="mai-call"></i> Phone2 :                
                  <a href="#" id="clinic-phone2"></a>                
              </li>
              <li>                
                  <i class="mai-mail"></i> Email :
                  <a href="#" id="clinic-email"></a>                
              </li>
                
            </ul>
            <div class="footer-sosmed mt-3">
              <a href="#" target="_blank"><span class="mai-logo-instagram"></span></a>
              <a href="#" target="_blank"><span class="mai-logo-linkedin"></span></a>
              <a href="#" target="_blank"><span class="mai-logo-whatsapp"></span></a>
              <a href="#" target="_blank"><span class="mai-logo-telegram"></span></a>
            </div>
          </div>
        </div>
      </div>            
    </div>
    `);
 
    $('#header-clinic-phone1').html(`<span class="mai-call text-primary"></span> ${outcome.results[0].phone1}`);  
    $('#header-clinic-email').html(`<span class="mai-mail text-primary"></span> ${outcome.results[0].email}`);  

    $('#clinic-email').html(`${outcome.results[0].email}`);  
    $('#clinic-phone1').html(`${outcome.results[0].phone1}`);  
    $('#clinic-phone2').html(`${outcome.results[0].phone2}`);  
    $('#clinic-country').html(`${outcome.results[0].country}`);  
    $('#clinic-city').html(`${outcome.results[0].city} / `);  
    $('#clinic-street').html(`${outcome.results[0].street} ,`);  
    $('#clinic-flat').html(`${outcome.results[0].flat} ,`);  

    
}


function about(){              
    url = '/api/about/';    
    
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

