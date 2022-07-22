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
