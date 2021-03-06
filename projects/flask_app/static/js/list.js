let value = 'a'
get_cocktail_list(value)

function get_cocktail_list(value) {
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?f=${value}`)
    
        .then(response => response.json() )
        .then((data) => {
            let card_list = document.querySelector('#card_list')
            card_list.innerHTML = ''
            for (const key in data.drinks) {
                let drink = data.drinks[key]
                let img_url = drink.strDrinkThumb
                let name = drink.strDrink
                let instruction = drink.strInstructions
                let ingredients = []
                    for (const key2 in drink) {
                        if (key2.includes('strIngredient')) {
                            ingredients.push(drink[key2])
                        }
                    }
                card_list.innerHTML += 
                `
                <div class="card" style="width: 18rem;">
                    <img src="${img_url}" class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">${name}</h5>
                    <p class="card-instruction">${instruction}</p>
                    <p class="card_ingredient">${ingredients} </p>
                    <div id="view_button">
                    <form action="/api/cocktail/create" method="post" id="cocktail_form">          
                        <input type="hidden" name="name" value=${name} />
                        <input type="hidden" name="instruction" value=${instruction}/>
                        <input type="hidden" name="ingredient" value=${ingredients}/>
                        <input type="hidden" name="img_url" value=${img_url}/>
                        <button class="btn btn-success">Save My list</button>
                    </form>
                    </div>
                </div>
                `
            }
        })
        .catch(err => console.log(err) )   
}

var search_form = document.querySelector('.search_form')

search_form.addEventListener('submit', function(e){
    e.preventDefault()
    let search_bar = document.querySelector('#search_bar').value
    
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${search_bar}`)
    .then(response => response.json() )
    .then((data) =>{
        console.log(data)
        var card_show = document.querySelector('.card_show')
        for (const key in data.drinks) {
            let drink = data.drinks[key]
            let img_url = drink.strDrinkThumb
            let name = drink.strDrink
            let instruction = drink.strInstructions
            let ingredients = []
                for (const key2 in drink) {
                    if (key2.includes('strIngredient')) {
                        ingredients.push(drink[key2])
                    }
                }
        card_show.innerHTML += 
        `
            <div class="card" style="width: 18rem;">
                <img src="${img_url}" class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">${name}</h5>
                <p class="card-instruction">${instruction}</p>
                <p class="card_ingredient">${ingredients} </p>
                <div id="view_button">
                <form action="/api/cocktail/create" method="post" id="cocktail_form1">          
                    <input type="hidden" name="name" value=${name} />
                    <input type="hidden" name="instruction" value=${instruction}/>
                    <input type="hidden" name="ingredient" value=${ingredients}/>
                    <input type="hidden" name="img_url" value=${img_url}/>
                    <button class="btn btn-success">Save My list</button>
                </form>
                </div>
            </div>`
        }
        })
    .catch(err => console.log(err) )   

})