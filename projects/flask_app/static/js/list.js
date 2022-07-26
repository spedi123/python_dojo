


function get_cocktail_list() {

    fetch("https://api.github.com/users/adion81")
        .then(response => response.json() )
        .then(data => console.log(data) )
        .catch(err => console.log(err) )
    
}
