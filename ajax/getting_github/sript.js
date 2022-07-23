var user_info = document.querySelector("#github_user");
function show(data) {
  var content = `<p>${data.name} has ${data.followers} followers</p>
                <p>Github address : ${data.html_url}</p>
                <img src="${data.avatar_url}" alt="${data.name}" />`;
  return content;
}

async function getCoderData() {
  var response = await fetch("https://api.github.com/users/adion81");
  var coderData = await response.json();
  console.log(coderData);
  user_info.innerHTML = show(coderData);
}

var userForm = document.querySelector(".userForm");
userForm.addEventListener("submit", function (e) {
  e.preventDefault();
  var userName = document.querySelector("#githubUser").value;
  console.log(userName);

  fetch(`https://api.github.com/users/${userName}`)
    .then((response) => response.json())
    .then((data) => {
      var userId = document.querySelector(".userId");
      var userImg = document.querySelector(".userImg");
      userId.textContent = data.login;
      userImg.innerHTML = `
      <img src="${data.avatar_url}" alt="user">
      `;
    })
    .catch((err) => console.log(err));
});
