window.addEventListener('load', async function() {
    let response = await fetch('http://localhost:8000/api/recipes/');
    let recipes = await response.json();
    for(let recipe of recipes){
        document.querySelector('#blog-section').innerHTML += `
        <div class="col-4">
                <div class="card">
                    <img src="${recipe.image}" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">${recipe.title}</h5>
                      <p class="card-text">${recipe['short_description']} ${recipe['category']['title']}</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
        `
    }
})