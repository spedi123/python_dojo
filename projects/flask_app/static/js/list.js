
function get_cocktail_list(value) {
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?f=${value}`)
    
        .then(response => response.json() )
        .then((data) => {
            let card_list = document.querySelector('#card_list')
            card_list.innerHTML = ''
            let card_ingredient = document.querySelector('.card_ingredient')   
            // let ingredients = []
            for (const key in data.drinks) {
                let drink = data.drinks[key]
                let img = drink.strDrinkThumb
                let name = drink.strDrink
                let instruction = drink.strInstructions
                let ingredients = []
                    for (const key2 in drink) {
                        if (key2.includes('strIngredient')) {
                            ingredients.push(drink[key2])
                        }
                    }
                    console.log(ingredients)
                card_list.innerHTML += 
                `
                <div class="card" style="width: 18rem;">
                    <img src="${img}" class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">${name}</h5>
                    <p class="card-instruction">${instruction}</p>
                    <p class="card_ingredient">${ingredients} </p>
                    <a href="#" class="btn btn-primary">View</a>
                </div>
                `
            }
        })
        .catch(err => console.log(err) )   
}