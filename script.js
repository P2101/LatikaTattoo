function iniciarMap(){
    var coord = {lat:40.0052431 ,lng: 3.8491911};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 14,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}