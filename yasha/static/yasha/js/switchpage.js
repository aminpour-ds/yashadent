
function switch_page(){
   let lanItem1=document.getElementById('language1');    
   let lanItem2=document.getElementById('language2');  
   let restUrl = '';
   if(document.documentElement.attributes.lang.value === "en"){
       lanItem1.className += " active";
       lanItem2.className = lanItem2.className.replace(" active", "");
       restUrl = document.location.href.split("/en")[1];
       lanItem1.href = document.location.href;
       lanItem2.href = restUrl;
   }
   if(document.documentElement.attributes.lang.value === "fa"){
       lanItem2.className += " active";
       lanItem1.className = lanItem1.className.replace(" active", "");
       restUrl = document.location.href.split(document.location.host)[1];
       lanItem2.href = document.location.href;
       lanItem1.href = '/en' + restUrl;
   }


   let navItems=document.getElementsByClassName('nav-link');
   for (let i=0; i < navItems.length; i++){
       if(navItems[i].href === document.location.href){
           navItems[i].className += " active";
       }
       else
           navItems[i].className = navItems[i].className.replace(" active", "");
   }
}

export { switch_page };