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

function k_c(e) {
  return Math.floor(e - 273);
}

function get_city_weather(event, city) {
  event.preventDefault();
  const locations = {
    burbank: { lat: "34.18", lon: "-118.30" },
    chicago: { lat: "41.87", lon: "-87.62" },
    dallas: { lat: "32.77", lon: "-96.79" },
  };
  const URL = `https://api.openweathermap.org/data/2.5/weather?lat=${locations[city].lat}&lon=${locations[city].lon}&appid=d36ac81c4e2b436c8b85b85016cfcdb6`;
  console.log(city, URL);
  fetch(URL)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      var forecast_today = document.querySelector(".forcast_today");
      var temp_max = `${data.main.temp_max}`;
      var temp_min = `${data.main.temp_min}`;
      forecast_today.innerHTML = `
      <div class="forecast-detail-today">
        <p>Today</p>
        <img src="./assets/some_rain.png" alt="some_rain" />
        <p>some rain</p>
        <p class="numberOfDegree">
          <span class="high" id="temp1">${k_c(temp_max)}°</span>
          <span class="low" id="temp2">${k_c(temp_min)}°</span>
        </p>
      </div>
      `;
    })
    .catch((err) => console.log(err));
}
