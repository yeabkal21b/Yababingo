import React from "react";
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import TransactionHistory from "./components/TransactionHistory";
// import other screens...

const nav = [
  { to: "/", label: "ዳሽቦርድ" },
  { to: "/create-game", label: "MTY Bingo" },
  { to: "/transactions", label: "የግብይት ታሪክ" },
];

export default function App() {
  return (
    <BrowserRouter>
      <div className="flex h-screen bg-[#1E1E1E] text-white">
        <aside className="w-60 bg-[#181818] p-6 flex flex-col">
          <div className="font-bold text-xl text-yellow-400 mb-8">Yaba ቢንጎ</div>
          <nav className="flex-1">
            {nav.map((n) => (
              <NavLink
                key={n.to}
                to={n.to}
                className={({ isActive }) =>
                  `block p-2 rounded hover:bg-blue-700 mb-1 ${
                    isActive ? "bg-blue-600" : ""
                  }`
                }
              >
                {n.label}
              </NavLink>
            ))}
          </nav>
        </aside>
        <main className="flex-1 overflow-auto p-8">
          <Routes>
            {/* <Route path="/" element={<Dashboard />} /> */}
            <Route path="/transactions" element={<TransactionHistory />} />
            {/* Add routes for other components */}
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}