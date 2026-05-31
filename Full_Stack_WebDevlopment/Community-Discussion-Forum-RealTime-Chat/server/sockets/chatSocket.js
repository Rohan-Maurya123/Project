const { Server } =
  require("socket.io");

function setupSocket(server) {
  const io = new Server(server, {
    cors: {
      origin:
        "http://localhost:5173",
      methods: ["GET", "POST"],
    },
  });

  io.on(
    "connection",
    (socket) => {
      console.log(
        "User Connected:",
        socket.id
      );

      socket.on(
        "joinRoom",
        (roomId) => {
          socket.join(roomId);

          console.log(
            `Joined Room ${roomId}`
          );
        }
      );

      socket.on(
        "sendMessage",
        (messageData) => {
          io.to(
            messageData.room
          ).emit(
            "receiveMessage",
            messageData
          );
        }
      );

      socket.on(
        "typing",
        (roomId) => {
          socket
            .to(roomId)
            .emit("userTyping");
        }
      );

      socket.on(
        "disconnect",
        () => {
          console.log(
            "User Disconnected"
          );
        }
      );
    }
  );
}

module.exports = setupSocket;