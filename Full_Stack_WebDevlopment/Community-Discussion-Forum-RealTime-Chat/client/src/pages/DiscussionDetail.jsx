import ChatWindow from "../components/ChatWindow";

function DiscussionDetail() {
  return (
    <div className="min-h-screen bg-slate-950 text-white p-8">
      <h1 className="text-4xl font-bold mb-4">MERN Roadmap Discussion</h1>

      <p className="text-gray-400 mb-8">Discuss everything related to MERN.</p>

      <ChatWindow />
    </div>
  );
}

export default DiscussionDetail;
