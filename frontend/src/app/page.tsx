"use client";

import ButtonMenu from "@/components/button/ButtonMenu";
import Header from "@/components/header/Header";

import dynamic from "next/dynamic";

const Map = dynamic(() => import("@/components/Map"), {
  ssr: false,
});

export default function Home() {
  return (
    <div className="w-screen h-screen relative">
      <Header />
      <Map />
      <ButtonMenu />
    </div>
  );
}
