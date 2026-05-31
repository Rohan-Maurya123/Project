import { useState, useEffect } from "react";

import socket from "../sockets/socket";

function ChatWindow() {
  const [message, setMessage] = useState("");

  const [messages, setMessages] = useState([]);

  useEffect(() => {
    socket.emit("joinRoom", "discussion-room");

    socket.on("receiveMessage", (data) => {
      setMessages((prev) => [...prev, data]);
    });

    return () => {
      socket.off("receiveMessage");
    };
  }, []);

  const sendMessage = () => {
    if (!message.trim()) return;

    const messageData = {
      room: "discussion-room",
      sender: "Rohan",
      message,
      time: new Date().toLocaleTimeString(),
    };

    socket.emit("sendMessage", messageData);

    setMessage("");
  };

  return (
    <div className="bg-slate-900 rounded-2xl p-6">
      <div className="h-96 overflow-y-auto mb-4">
        {messages.map((msg, index) => (
          <div key={index} className="mb-3">
            <strong>{msg.sender}</strong>

            <p>{msg.message}</p>
          </div>
        ))}
      </div>

      <div className="flex gap-3">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className="flex-1 p-3 rounded-xl bg-slate-800"
          placeholder="Type message..."
        />

        <button onClick={sendMessage} className="bg-cyan-500 px-6 rounded-xl">
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatWindow;
