window.onload = questions();

document.getElementById('question-pagination').style.backgroundImage= `url(${outcome.results[0].images[2].image})`;


$('#question-pagination').html(`
                <li class="page-item disabled">
                  <a class="page-link" href={{previous}} tabindex="-1" aria-disabled="true">Previous</a>                    
                  </li>
                  <li class="page-item active" aria-current="page">
                    <a class="page-link" href="/questions/">1 <span class="sr-only">(current)</span></a>
                  </li>
                  <li class="page-item">
                    <a class="page-link" href="/questions/?page=2">2</a>
                  </li>                  
                  <li class="page-item">
                    <a class="page-link" href={{next}} >Next</a>                   
                  </li>
                  `);