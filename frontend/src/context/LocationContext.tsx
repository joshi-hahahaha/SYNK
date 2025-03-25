"use client";
import { createContext, useContext, useEffect, useState } from "react";
import { Map } from "leaflet";

type LocationContextType = {
  userLocation: [number, number] | null;
  setUserLocation: (location: [number, number]) => void;
  map: Map | null;
  setMap: (map: Map) => void;
};

const LocationContext = createContext<LocationContextType | undefined>(
  undefined
);

// Essentially this Context stores the a reference to the map globally so that
// the component doesnt need to strictly be under MapContainer
export const LocationProvider = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const [userLocation, setUserLocation] = useState<[number, number] | null>(
    null
  );
  const [map, setMap] = useState<Map | null>(null); // Store the Leaflet map instance

  useEffect(() => {
    const successCallback = (position: GeolocationPosition) => {
      setUserLocation([position.coords.latitude, position.coords.longitude]);
    };

    const watchId = navigator.geolocation.watchPosition(successCallback, null, {
      enableHighAccuracy: true,
      maximumAge: 1000,
      timeout: 1000,
    });

    return () => navigator.geolocation.clearWatch(watchId);
  }, []);

  return (
    <LocationContext.Provider
      value={{ userLocation, setUserLocation, map, setMap }}
    >
      {children}
    </LocationContext.Provider>
  );
};

export const useLocation = () => {
  const context = useContext(LocationContext);
  if (!context) {
    throw new Error("useLocation must be used within a LocationProvider");
  }
  return context;
};
