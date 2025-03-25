"use client";
import { useEffect, useRef, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { Icon } from "leaflet";
import { EventObj } from "@/type";
import { URL_BASE } from "@/constants";
import { useLocation } from "@/context/LocationContext";
import { EventPopup } from "@/components/EventPopup";

const markerUserIcon = new Icon({
  iconUrl:
    "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
});

const eventIcon = new Icon({
  iconUrl:
    "https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
});

const Map = () => {
  // Utilises a Context - a cool thing in React that lets
  // you store "global" variables, states, functions, etc.

  // useLocation is the Context, and userLocation and setMap
  // is a state and function defined in useLocation

  // can look at the imports, but useLocation is from
  // LocationContext.tsx (take a read of it)
  const { userLocation, setMap } = useLocation();
  const mapRef = useRef(null);

  useEffect(() => {
    if (mapRef.current) {
      setMap(mapRef.current); // Store the map instance in context
    }
  }, [mapRef, setMap]);
  const [events, setEvents] = useState<EventObj[]>([]);

  useEffect(() => {
    if (!userLocation) return;

    const getData = async () => {
      try {
        const response = await fetch(
          `${URL_BASE}/events?latitude=${userLocation[0]}&longitude=${userLocation[1]}`
        );
        if (!response.ok) {
          console.log("error");
          return;
        }
        const json = await response.json();
        setEvents(json);
      } catch (error) {
        console.log(error);
      }
    };

    getData();
  }, [userLocation]);

  return (
    <div className="h-screen w-screen relative">
      {userLocation ? (
        <MapContainer
          center={userLocation}
          zoom={13}
          className="h-full w-full"
          ref={mapRef}
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
          <Marker position={userLocation} icon={markerUserIcon}>
            <Popup>{"You are here!"}</Popup>
          </Marker>
          {events.map((event) => (
            <Marker
              key={event.id}
              position={[event.latitude, event.longitude]}
              icon={eventIcon}
            >
              <Popup className="m-0 p-0">
                <EventPopup {...event} />
              </Popup>
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
