
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
            description: userinfo.input_message.value || '-'
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