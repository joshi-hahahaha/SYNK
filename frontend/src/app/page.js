"use client";
import { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

export default function Home() {
  const [userLocation, setUserLocation] = useState(null);
  const [dummyMarker, setDummyMarker] = useState(null);

  useEffect(() => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const lat = position.coords.latitude;
          const lng = position.coords.longitude;
          setUserLocation({ lat, lng });

          // Place a dummy marker nearby (~0.01 degree offset)
          setDummyMarker({ lat: lat + 0.01, lng: lng + 0.01 });
        },
        (error) => console.error("Error getting location:", error),
        { enableHighAccuracy: true }
      );
    }
  }, []);

  if (!userLocation) return <p>Fetching location...</p>;

  return (
    <MapContainer
      center={userLocation}
      zoom={15}
      style={{ height: "100vh", width: "100%" }}
      dragging={true} // Enable dragging
      scrollWheelZoom={true} // Allow zooming with scroll wheel
      zoomControl={true} // Show zoom controls
    >
      {/* OpenStreetMap tile layer */}
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {/* User's actual location */}
      <Marker
        position={userLocation}
        icon={
          new L.Icon({
            iconUrl: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
          })
        }
      >
        <Popup>Your Location</Popup>
      </Marker>

      {/* Dummy marker nearby */}
      {dummyMarker && (
        <Marker position={dummyMarker}>
          <Popup>Nearby Location</Popup>
        </Marker>
      )}
    </MapContainer>
  );
}
