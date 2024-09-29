import React from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const containerStyle = {
    width: '60%',
    height: '500px',
};

const center = {
    lat: 40.4406,
    lng: -79.9759,
};

const position = [
    { lat: 40.4406, lng: -79.9959 },
    { lat: 40.4449, lng: -79.9584 },
    { lat: 40.4290, lng: -79.9806 },
];

const Maps = () => {
    return (
        <LoadScript googleMapsApiKey="AIzaSyCvsLhLMJGwLju82scVJAV0ofnsFGr0dew">
            <GoogleMap
                mapContainerStyle={containerStyle}
                center={center}
                zoom={13}
                onLoad={() => console.log('Map loaded')}
            >

                {position.map((pos, index) => (
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