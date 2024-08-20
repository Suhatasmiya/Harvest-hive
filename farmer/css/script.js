
$(function () {
    // Get the canvas element and create the chart
    var ctx = document.getElementById('myChart').getContext('2d');
    // function myFunction() {
        var item = document.getElementsByTagName("li")
    // }
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [
                {
                    label: item[0].innerHTML,
                    data: [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],
                    borderColor: 'red',
                    fill: false
                },
                {
                  label: item[1].innerHTML,
                  data: [8, 9, 11, 12, 14, 10, 17, 18, 20, 21, 23, 25],
                  borderColor: 'blue',
                  fill: false
                },
                {
                  label: item[2].innerHTML,
                  data: [6, 7, 8, 9, 10, 12, 10, 14, 15, 16, 18, 20],
                  borderColor: 'green',
                  fill: false
                },
                {
                  label: item[3].innerHTML,
                  data: [6, 7, 8, 9, 10, 12, 13, 14,10, 16, 18, 20],
                  borderColor: 'black',
                  fill: false
                },
                {
                  label: item[4].innerHTML,
                  data: [6, 7, 8, 9, 10, 12, 13, 14, 15, 10, 18, 20],
                  borderColor: 'brown',
                  fill: false
                },
                {
                  label: item[5].innerHTML,
                  data: [6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 10, 20],
                  borderColor: 'yellow',
                  fill: false
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Price Trend in Market for Various Crops and Vegetables'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});
var x = document.getElementsByClassName("latitude");
var y = document.getElementsByClassName("longitude");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}