import React, { useState } from 'react'; 
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const containerStyle = {
    width: '60%',
    height: '500px',
};

const center = {
    lat: 40.4406,
    lng: -79.9759,  
};
/*
async function fetchStations()
{
    const response = await fetch('bikeStationLoc.csv');
    const text = await response.text();
    return text.split("\n");
}

const stations = await fetchStations();

for (int i = 1; i < station.length; i++) {
    var cols = station[i].split(',');
    var pos = new google.maps.LatLng(cols[4], cols[5]);
    station = new Marker(
        {
            map,
            position: pos
        }
    )
}
    */

const position = [
    { lat: 40.4526, lng: -80.0529 },
    { lat: 40.4381, lng: -79.9235 },
    { lat: 40.4344, lng: -79.9519 },
    { lat: 40.4416, lng: -79.9558 },
    { lat: 40.438, lng: -79.9537 },
    { lat: 40.439, lng: -79.9603},
    { lat: 40.4513, lng: -79.953 },
    
];

const Maps = () => {
    const [mapLoaded, setMapLoaded] = useState(false);
    return (
        <LoadScript googleMapsApiKey="AIzaSyCvsLhLMJGwLju82scVJAV0ofnsFGr0dew">
            

            <GoogleMap
                mapContainerStyle={containerStyle}
                center={center}
                zoom={13}
                onLoad={() => {
                    console.log('Map loaded');
                    setMapLoaded(true); 
                }}
            >

                {mapLoaded && position.map((pos, index) => (
                    <Marker
                        key={index}
                        position={pos}
                        onLoad={() => console.log(`Marker ${index} loaded`)}
                        onClick={() => alert(`Marker ${index} clicked at position: ${pos.lat}, ${pos.lng}`)}
                    />
                    
                ))}
                
            </GoogleMap>

        </LoadScript>
    );
};

export default Maps;

// import React from 'react';
// import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

// window.initMap = async function initMap()
// {
//     // script.src = 'https://maps.googleapis.com/maps/api/js?key=${AIzaSyCvsLhLMJGwLju82scVJAV0ofnsFGr0dew}&callback=initMap';
//     const { Map } = await google.maps.importLibrary("maps");
//     const { Marker } = await google.maps.importLibrary("marker");
//     const { AdvancedMarkerElement, PinElement } = await google.maps.importLibrary("marker");

//     const map = new Map(document.getElementById('map'),
//     {
//         center: new google.maps.LatLng('40.4406', '-79.9759'),
//         zoom: 13,
//     });

//     var bounds = new google.maps.LatLngBounds();

//         var pos = new google.maps.LatLng(40.4449, -79.9584);

//         station = new Marker(
//         {
//             map,
//             position: pos,
//         });
// }


