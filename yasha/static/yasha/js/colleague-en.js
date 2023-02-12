
function colleagueCard(item) {
    
    return `<div class="col-md-6 col-lg-4 py-3 wow zoomIn">
            <div class="card-doctor">
                <div class="header">
                <img src=${item.images[0].image} alt="">
                </div>
                <div class="body">
                <p class="text-xl mb-0" style="text-align: center;">${item.first_name_en} ${item.last_name_en}</p>            
                <div class="text-xl mb-0">                                                        
                    <div style="text-align: center;">
                    <span class="text-sm text-grey">${item.professionalStatement_en}</span>
                    </div>
                </div>                        
                </div>
            </div>
            </div>`
}


let request = new XMLHttpRequest();
let colleague_itm = document.getElementById("colleague");
request.open("GET", "/api/colleague/", true);
request.send();
request.onload = () => {    
    if (request.status == 200) {
        response=JSON.parse(request.responseText);
        for (let index=0; index < response.results.length; index++){
            colleague_itm.innerHTML += colleagueCard(response.results[index]);      
        }
    }                                                      
}   