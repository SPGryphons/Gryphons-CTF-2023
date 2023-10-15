import React, { useState } from 'react';
import toast from 'react-hot-toast';
import nookies, { parseCookies } from 'nookies';
import Image from 'next/image'
import { useRouter } from 'next/router';
import { ThemeContext } from "../components/ThemeProvider";

const LoginPage: React.FC = () => {
  const router = useRouter();
  const { changeTheme } = React.useContext(ThemeContext);
  const [darkMode, setDarkMode] = useState(true);
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleThemeChange = () => {
    setDarkMode(!darkMode);
    const theme = darkMode ? 'light' : 'dark';
    changeTheme(theme);
  };

  const handleFormSubmission = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    //wait 5 seconds
    await new Promise((resolve) => setTimeout(resolve, 5000));

    const response = await fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, password }),
    });

    const data = await response.json()
    setLoading(false);

    if (data.error) {
      toast.error(data.error);
    } else {
      toast.success(data.msg);
      router.push('/flag')
    }

  };

  return (
    <div className={`min-h-screen flex items-center justify-center`}>
      {loading && (
        <div className="fixed inset-0 bg-gray-900 opacity-75 flex items-center justify-center z-50">
          <span className="loading loading-infinity loading-lg"></span>
        </div>
      )}
      <button
        onClick={handleThemeChange}
        className={`absolute top-4 right-4 btn`}
      >
        {darkMode ? 'Light Mode' : 'Dark Mode'}
      </button>

      <div className={`p-8 rounded-lg shadow-md w-full sm:w-96`}>
        <h1 className={`text-2xl font-semibold mb-4`}>Login</h1>
        <form className="space-y-4" onSubmit={handleFormSubmission}>
          <div className="space-y-2">
            <label
              htmlFor="name"
              className={`block text-sm font-medium`}
            >
              Name
            </label>
            <input
              id="name"
              name="name"
              type="name"
              className="input input-bordered w-full"
              onChange={(e) => setName(e.target.value)}
              required
            />
          </div>
          <div className="space-y-2">
            <label
              htmlFor="password"
              className={`block text-sm font-medium`}
            >
              Password
            </label>
            <input
              id="password"
              name="password"
              type="password"
              className="input input-bordered w-full"
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <div>
            <button type="submit" className="btn btn-primary w-full">
              Login
            </button>
          </div>
        </form>
        <div className="mt-52">
          <Image
            className=""
            src="/next.svg"
            alt="Next.js Logo"
            width={180}
            height={37}
            priority
          />
          
        </div>
      </div>

    </div>
  );
};

export default LoginPage;
