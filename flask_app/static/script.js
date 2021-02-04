// Called to display the answer of grandpy in the page application
var compteur = 0;
function grandpyAnswer(){
    var user_input = document.getElementById("user_input");
    var user_input_value = user_input.value;
    $("#chat ul").append('<li class="question"><div class="speech-bubble">' + user_input_value + '</div></li>');
    user_input.value = "";
    $("#chat").scrollTop($('#chat').prop("scrollHeight"));
    url = `api_google?user_raw_text=${user_input_value}`;

    $.get(url, function (data, status){
      // console.log(data)
      compteur++
      var extract = data.extract
      var pageid = data.pageid
      var id_map = "map_"+compteur
      var celcius = data.celcius
      var right_place = data.right_place
      var description_weather = data.description_weather
      $("#chat ul").append('<li class="answer"><div class="speech-bubble" style= maxheight="100px">' + extract + '</div></li>');
      $("#chat ul").append('<li class="answer"><div class="speech-bubble"><a href="https://fr.wikipedia.org/?curid=' + pageid + '" target="_blank">Voir plus directement sur Wikipedia</a></div></li>');
      $("#chat ul").append('<div class="answer"><div class="speech-bubble"><div id="' + id_map + '" style="width:400px;height:400px"></div></div></div>');
      $("#chat ul").append('<li class="answer"><div class="speech-bubble" style= maxheight="100px"> Il fait ' +" "+ celcius +" "+ 'degrés celcius  à' + " " + right_place + "  " + "et le temps est " + description_weather + " " + '</div></li>');
      console.log("Succès");
      // console.log(pageid);
      create_map(data["latitude"],data["longitude"],id_map)
    // })
    // .done(function(response){       
    //     $("#chat ul").append('<li class="answer"><div class="speech-bubble">Je ne me souviens plus</div></li>');
    //     $("#chat ul").append('<div class="answer"><div class="speech-bubble"><div id="map" style="width:400px;height:400px"></div></div></div>');
    //     console.log("Succès");
    }).fail(function() {
        $("#chat ul").append('<li class="answer"><div class="speech-bubble">Je ne me souviens plus de rien</div></li>');
        console.log("Echec");
        create_map(data["latitude"],data["longitude"],id_map)
    });

}
// init function for the google map api

function create_map(lat,lng,id) {
  var mylocation = {lat: lat, lng: lng};

  var map = new google.maps.Map(document.getElementById(id), {
    center: mylocation,
    zoom: 12,
  });
  var marker = new google.maps.Marker({
    position: mylocation,
    map: map
  });
}

