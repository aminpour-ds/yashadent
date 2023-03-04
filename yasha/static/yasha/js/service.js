window.onload = service_items();
const service_itm = document.getElementById("service-items");


function serviceCard(item){
    var img = item.images[0].image;   
    var id = item.id;
    if(document.documentElement.attributes.lang.value === "fa"){
        var name = item.name_fa;
        style = "direction: rtl; text-align: center;";
        href = '/service/';
    } else {
        var name = item.name_en;
        style = "text-align: center;";
        href = '/en/service/';
    }    
    
    return '<div class="col-lg-4 py-2 wow zoomIn"><div class="card-blog" style ="' + style + '"><div class="header">' +
           '<a href="' + href + id + '" class="post-thumb"><img src="' + img + '" alt=""></a></div><div class="body">' +
           '<h5 class="post-title"><a href="' + href + id + '">' + name + '</a></h5></div></div></div>';
}

function service_list(outcome){
    for (selitem=0; selitem<outcome.results.length; selitem++){
        service_itm.innerHTML += serviceCard(outcome.results[selitem]);      
    }     
}


function service_items(){              
    url = '/api/service/';    
    
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

    const ret_items = async () => {
        const a = await items;
        return a;
    };
    
    ret_items().then(function(outcome) {        
        service_list(outcome);
    });
}

