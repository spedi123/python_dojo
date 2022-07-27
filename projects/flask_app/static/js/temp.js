
function get_cocktail_list(value) {
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?f=${value}`)
    
        .then(response => response.json() )
        .then((data) => {
            console.log(data)
            var card_list = document.querySelector('#card_list')
            // var card_ingredient = document.querySelector('.card-ingredient')
            card_list.innerHTML = ''
            for (var i=0; i <data.drinks.length; i++) {
                var img = data.drinks[i].strDrinkThumb
                var name = data.drinks[i].strDrink
                let ingredients = []
                for (const key in data.drinks) {
                    let drink = data.drinks[key]
                    for (const key2 in drink) {
                        if (key2.includes('strIngredient')) {
                            ingredients.push(drink[key2])
                        }
                        
                    }
                    console.log(ingredients)
                }
                // for (var j=0; j<7; j++) {
                //     if (ingredient_list == null){
                //         break
                //     }
                //     var ingredient_list = data.drinks[i].strIngredient[j]
                //     card_ingredient.innerHTML += 
                //     `<p calss="card_ingredient">${ingredient_list}</p>`
                // }
                var instruction = data.drinks[i].strInstructions 
                var ingredient1 = data.drinks[i].strIngredient1
                var ingredient2 = data.drinks[i].strIngredient2
                var ingredient3 = data.drinks[i].strIngredient3
                var ingredient4 = data.drinks[i].strIngredient4
            card_list.innerHTML += `
            <div class="card" style="width: 18rem;">
                <img src="${img}" class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">${name}</h5>
                <p class="card-instruction">${instruction}</p>
                <p class="card_ingredient">${ingredient1}, ${ingredient2}, ${ingredient3}, ${ingredient4} </p>
                <a href="#" class="btn btn-primary">View</a>
            </div>`
            
            }
            // for (var j=0; j<7; j++) {
            //     if (data.drinks[j].strIngredient[j] == null){
            //         break
            //     }
            //     var ingredient_list = data.drinks[j].strIngredient[j]
            //     card_ingredient.innerHTML += 
            //     `<p calss="card_ingredient">${ingredient_list}</p>`
            // }

        })
        .catch(err => console.log(err) )   
}