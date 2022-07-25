
function getUsers(){
    fetch('http://127.0.0.1:5000/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })

}
getUsers();

var myForm = document.querySelector('#myForm')
myForm.addEventListener(submit, function(e){
    e.preventDefault()
    var form = new FormData(myForm)
    fetch('http://127.0.0.1:5000/create/user', {
        method: 'post',
        body: form
    })
    .then(res =>  res.json())
    .then(data => {
        console.log(data)
    })
})

