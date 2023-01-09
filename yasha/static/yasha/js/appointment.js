window.onload = site_appointment();

function site_appointment(){       

    $('#site-appointment').html(`
    <div class="container">
      <h1 class="text-center wow fadeInUp">Make an Appointment</h1>
      <form class="main-form">
        
       
        <div class="row mt-5 ">
          <div class="col-12 col-sm-6 py-2 wow fadeInLeft">
            <input type="text" class="form-control" placeholder="Full name" id="inputUsername">
          </div>        
          <div class="col-12 col-sm-6 py-2 wow fadeInRight" data-wow-delay="300ms">
            <select name="departement" id="departement" class="custom-select">
              <option value="general">General Health</option>
              <option value="cardiology">Cardiology</option>
              <option value="dental">Dental</option>
              <option value="neurology">Neurology</option>
              <option value="orthopaedics">Orthopaedics</option>
            </select>
          </div>
          <div class="col-12 py-2 wow fadeInUp" data-wow-delay="300ms">
            <input type="text" class="form-control" placeholder="Number.." id="userNumber">
          </div>
          <div class="col-12 py-2 wow fadeInUp" data-wow-delay="300ms">
            <textarea name="message" id="message" class="form-control" rows="6" placeholder="Enter message.."></textarea>
          </div>
        </div>
        <button type="submit" class="btn btn-primary mt-3 wow zoomIn" onclick=submitRequest()>Submit Request</button>
      </form>
    </div>
    `); 
}


function submitRequest() {
    const userinfo = {
        input_username : document.querySelector("#inputUsername"),
        input_departement : document.querySelector("#departement"),        
        input_UserNumber : document.querySelector("#userNumber"),         
        input_message : document.querySelector("#message")            
    };                          
    addEventListener("click", async (e) => {                
        e.preventDefault();
  
        await fetch('/api/AppointmentRequest/', {
            method: 'POST',
            headers: {
            Accept: "application/json, text/plain, */*",
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
            name: userinfo.input_username.value,
            your_problem: userinfo.input_departement.value,
            phone: userinfo.input_UserNumber.value,
            description: userinfo.input_message.value
            }),                
        })
        .then((res) => {
            if (res.status == 201) {
                return res.json();
            } else {
                throw Error(res.statusText);
            }
        })
        .then(data => {
            window.location.assign("/");
            alert('Your request has been registered, you will be contacted soon to set up an appointment time. thank you!');
        })
        .catch((err) => {                    
            console.log(err);
            alert('The entered information is not correct, try again!');
        });
    });            
}