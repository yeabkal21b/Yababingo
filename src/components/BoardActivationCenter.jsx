import React, { useState } from "react";

export default function BoardActivationCenter({ total = 100, onActivate }) {
  const [active, setActive] = useState(Array(total).fill(false));
  function toggle(idx) {
    const updated = [...active];
    updated[idx] = !updated[idx];
    setActive(updated);
    onActivate && onActivate(updated);
  }
  return (
    <div className="grid grid-cols-10 gap-1">
      {Array(total)
        .fill(0)
        .map((_, idx) => (
          <button
            key={idx}
            className={`h-10 w-10 rounded ${
              active[idx] ? "bg-green-500" : "bg-gray-600"
            }`}
            onClick={() => toggle(idx)}
          >
            {idx + 1}
          </button>
        ))}
    </div>
  );
}