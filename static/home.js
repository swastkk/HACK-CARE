var Location = document.getElementById("Location");
navigator.geolocation.getCurrentPosition(showLocation);
  
function showLocation(position) {
    latt = position.coords.latitude;
    long = position.coords.longitude;
    var lattlong = new google.maps.LatLng(latt, long);
    var Options = {
        center: lattlong,
        zoom: 15,
        mapTypeControl: true,
        navigationControlOptions:
            { style: google.maps.NavigationControlStyle.SMALL }
    }
    var Mapmain = new google.maps.Map
        (document.getElementById("Map"), Options);
    var markerpos =
        new google.maps.Marker
            ({ position: lattlong, map: Mapmain });
    }
