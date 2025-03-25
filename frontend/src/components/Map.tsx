"use client";
import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { Icon } from "leaflet";
import { EventObj } from "@/type";
import { URL_BASE } from "@/constants";

const RecenterMap = ({ center }: { center: [number, number] }) => {
  const map = useMap();
  useEffect(() => {
    map.flyTo(center, 13);
  }, [center, map]);

  return null;
};

const markerUserIcon = new Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
})

const eventIcon = new Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
})

const Map = () => {
  const [userLocation, setUserLocation] = useState<[number, number] | null>(null);
  const [events, setEvents] = useState<EventObj[]>([]);

  const successCallback = (position: GeolocationPosition) => {
    setUserLocation([position.coords.latitude, position.coords.longitude]);
  };

  useEffect(() => {
    const watchId = navigator.geolocation.watchPosition(successCallback, null, {
      enableHighAccuracy: true,
      maximumAge: 1000,
      timeout: 1000,
    });
    return () => navigator.geolocation.clearWatch(watchId);
  }, []);

  useEffect(() => {
    const getData = async () => {
      const latitude = userLocation ? userLocation[0] : 0
      const longitude = userLocation ? userLocation[1] : 0
      try {
        const response = await fetch(`${URL_BASE}/events?latitude=${latitude}&longitude=${longitude}`)
        if (!response.ok) {
          console.log("error")
          return
        }
        const json = await response.json()
        setEvents(json)
      }
      catch (error) {
        console.log(error)
      }
    }
    getData()
  }, [userLocation])

  return (
    <div className="h-screen w-screen relative">
      {userLocation &&
        <button
        className="absolute bottom-4 left-4 bg-blue-500 text-white px-4 py-2 rounded-lg z-1000 cursor-pointer"
        onClick={() => setUserLocation([...userLocation])}>
        Recentre</button>
      }
      {userLocation ? (
        <MapContainer center={userLocation} zoom={13} className="h-full w-full">
        <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        <Marker position={userLocation} icon={markerUserIcon}>
        <Popup>{"You are here!"}</Popup>
        </Marker>
        <RecenterMap center={userLocation} />
        {events.map((event) => (
          <Marker key={event.id} position={[event.latitude, event.longitude]} icon={eventIcon}>
            <Popup>
              <h2><b>{event.name}</b></h2>
              <p>{event.description}</p>
              <i>{event.isPublic ? "Open" : "Closed"}</i></Popup>
          </Marker>
          ))}
        </MapContainer>
      ) : (
        <p className="text-center mt-10">Fetching location...</p>
      )}
    </div>
  );
};

export default Map;
