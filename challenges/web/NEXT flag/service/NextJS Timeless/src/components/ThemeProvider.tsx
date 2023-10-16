import React, { createContext, useEffect, useState } from 'react';


interface ThemeContextProps {
  theme: string;
  changeTheme: (newTheme: string) => void;
}

export const ThemeContext = createContext<ThemeContextProps>({
  theme: 'dark',
  changeTheme: () => {},
});

interface ThemeProviderProps {
  children: React.ReactNode;
}

export const ThemeProvider: React.FC<ThemeProviderProps> = ({ children }) => {
  const [theme, setTheme] = useState('dark');

  useEffect(() => {
    setTheme('dark');
  }, []);

  const changeTheme = (newTheme: string) => {
    setTheme(newTheme);
  };

  const clientTheme = theme || 'dark';

  return (
    <ThemeContext.Provider value={{ theme: clientTheme, changeTheme }}>
      <div data-theme={clientTheme}>{children}</div>
    </ThemeContext.Provider>
  );
};
