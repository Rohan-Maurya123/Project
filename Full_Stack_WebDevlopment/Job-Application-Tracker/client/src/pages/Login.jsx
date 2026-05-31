import { useNavigate } from "react-router-dom";

export default function Login() {
  const navigate = useNavigate();

  return (
    <div className="h-screen flex items-center justify-center bg-gradient-to-r from-purple-900 to-black">
      <div className="bg-white/10 p-8 rounded-xl w-96 text-white backdrop-blur-lg">
        <h1 className="text-2xl mb-4">Login</h1>

        <input className="w-full p-2 mb-3 text-black" placeholder="Email" />
        <input className="w-full p-2 mb-3 text-black" placeholder="Password" />

        <button
          onClick={() => navigate("/dashboard")}
          className="w-full bg-purple-600 p-2 rounded"
        >
          Login
        </button>
      </div>
    </div>
  );
}
