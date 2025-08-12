import React, { useEffect, useState } from "react";
import { fetchTransactions } from "../services/api";

const TRANSLATE_TYPE = {
  ADMIN_CREDIT: "አስተዳዳሪ ብድር",
  GAME_LAUNCH_COST: "የጨዋታ ምስክር ወጪ",
};

export default function TransactionHistory() {
  const [transactions, setTransactions] = useState([]);
  useEffect(() => {
    fetchTransactions().then((resp) => setTransactions(resp.data));
  }, []);

  return (
    <div className="p-6 bg-[#1E1E1E] text-white rounded-lg shadow">
      <h2 className="text-2xl mb-4 font-bold text-yellow-400">የግብይት ታሪክ</h2>
      <table className="w-full text-sm">
        <thead>
          <tr className="bg-[#222]">
            <th className="p-2">ቀን</th>
            <th className="p-2">ዓይነት</th>
            <th className="p-2">መጠን</th>
            <th className="p-2">ቀሪ ሂሳብ</th>
            <th className="p-2">ማብራሪያ</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((tx, i) => (
            <tr key={i} className={i % 2 === 0 ? "bg-[#1E1E1E]" : "bg-[#232323]"}>
              <td className="p-2">{new Date(tx.timestamp).toLocaleString("am-ET")}</td>
              <td className="p-2">{TRANSLATE_TYPE[tx.transaction_type] || tx.transaction_type}</td>
              <td className={`p-2 ${tx.amount > 0 ? "text-green-400" : "text-red-400"}`}>
                {tx.amount > 0 ? "+" : ""}
                {tx.amount} ብር
              </td>
              <td className="p-2">{tx.balance_after_transaction} ብር</td>
              <td className="p-2">{tx.notes}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}