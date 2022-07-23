var cookie = document.querySelector(".cookie");

function cookieDelete() {
  cookie.remove();
}

function cel(temp) {
  return Math.round((9 / 5) * temp + 32);
}

function fah(temp) {
  return Math.round((5 / 9) * (temp - 32));
}

function change(e) {
  console.log(e.value);
  for (i = 1; i < 9; i++) {
    var temp = document.querySelector("#temp" + i);
    var newTemp = parseInt(temp.innerText);
    console.log(newTemp);
    if (e.value === "°C") {
      temp.innerText = fah(newTemp);
    } else {
      temp.innerText = cel(newTemp);
    }
  }
}

// api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={cnt}&appid={API key}
