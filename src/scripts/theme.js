const themeToggle = document.querySelector('.theme-toggle');

if (themeToggle instanceof HTMLButtonElement) {
  const sync = () => {
    const isLight = document.documentElement.dataset.theme === 'light';
    const label = `Switch to ${isLight ? 'dark' : 'light'} mode`;
    themeToggle.setAttribute('aria-checked', String(isLight));
    themeToggle.setAttribute('aria-label', label);
    themeToggle.title = label;
  };

  themeToggle.hidden = false;
  sync();
  themeToggle.addEventListener('click', () => {
    const theme = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    document.documentElement.dataset.theme = theme;
    try {
      localStorage.setItem('theme', theme);
    } catch (_) {}
    sync();
  });
}
