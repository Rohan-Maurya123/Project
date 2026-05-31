import {
  FaHome,
  FaComments,
  FaPlusCircle,
  FaBell,
  FaUser,
} from "react-icons/fa";

import { Link } from "react-router-dom";

function Sidebar() {
  const menu = [
    {
      name: "Dashboard",
      icon: <FaHome />,
      path: "/dashboard",
    },
    {
      name: "Discussions",
      icon: <FaComments />,
      path: "/discussions",
    },
    {
      name: "Create",
      icon: <FaPlusCircle />,
      path: "/create-discussion",
    },
    {
      name: "Notifications",
      icon: <FaBell />,
      path: "/notifications",
    },
    {
      name: "Profile",
      icon: <FaUser />,
      path: "/profile",
    },
  ];

  return (
    <div className="w-72 min-h-screen bg-slate-900 border-r border-slate-800 p-6">
      <h1 className="text-3xl font-bold text-cyan-400 mb-10">CommunityHub</h1>

      <div className="space-y-3">
        {menu.map((item) => (
          <Link
            key={item.name}
            to={item.path}
            className="flex items-center gap-4 bg-slate-800 hover:bg-cyan-500 transition-all duration-300 p-4 rounded-xl"
          >
            {item.icon}
            <span>{item.name}</span>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default Sidebar;
