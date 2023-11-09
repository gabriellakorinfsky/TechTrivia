let map;

function initMap() {
    var location = { lat: -8.051410980778142, lng: -34.903168898116604 }; // Coordenadas do local desejado -8.051410980778142, -34.903168898116604

    var map = new google.maps.Map(document.getElementById('map'), {
        center: location,
        zoom: 15 // Ajuste conforme necessário
    });

    var marker = new google.maps.Marker({
        position: location,
        map: map,
        title: 'Uninassau'
    });
}

initMap();