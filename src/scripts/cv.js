(() => {
  const consolePalette = {
    surface: "#111827",
    badgeText: "#cbd5e1",
    identityAccent: "#67e8f9",
    identityRose: "#fb7185",
    muted: "#727985",
    accent: "#147d92",
    rose: "#d9466f",
    amber: "#a86f13",
    green: "#238636",
    violet: "#9b5de5"
  };
  const consoleFont = "font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;text-shadow:none;";
  const consoleIdentity = "JAMES WOLMAN\nHEAD OF DATA SCIENCE";
  const consoleStyles = {
    identity: `${consoleFont}color:${consolePalette.identityAccent};background:${consolePalette.surface};border-left:3px solid ${consolePalette.identityRose};font-size:13px;font-weight:800;letter-spacing:.04em;line-height:1.5;padding:8px 12px;border-radius:0 6px 6px 0;`,
    sectionMarker: `${consoleFont}color:${consolePalette.rose};font-weight:800;`,
    sectionHeading: `${consoleFont}font-weight:800;letter-spacing:.04em;`,
    sectionCount: `${consoleFont}color:${consolePalette.badgeText};background:${consolePalette.surface};font-weight:700;padding:2px 6px;border-radius:999px;`,
    indexRed: `${consoleFont}color:${consolePalette.rose};font-weight:800;`,
    indexAmber: `${consoleFont}color:${consolePalette.amber};font-weight:800;`,
    indexGreen: `${consoleFont}color:${consolePalette.green};font-weight:800;`,
    indexViolet: `${consoleFont}color:${consolePalette.violet};font-weight:800;`,
    indexCyan: `${consoleFont}color:${consolePalette.accent};font-weight:800;`,
    heading: `${consoleFont}font-weight:700;`,
    label: `${consoleFont}color:${consolePalette.muted};font-weight:700;letter-spacing:.03em;`,
    labelIntel: `${consoleFont}color:${consolePalette.violet};font-weight:700;letter-spacing:.03em;`,
    url: `${consoleFont}color:${consolePalette.accent};font-weight:500;`,
    signal: `${consoleFont}color:${consolePalette.green};font-weight:600;`,
    value: `${consoleFont}font-weight:400;`
  };
  console.log("%c" + consoleIdentity, consoleStyles.identity);
  console.groupCollapsed("%c◆%c  SIDE PROJECTS%c  5 BUILDS", consoleStyles.sectionMarker, consoleStyles.sectionHeading, consoleStyles.sectionCount);
  console.groupCollapsed("%c01%c  n8n Self-Hosting Repository", consoleStyles.indexRed, consoleStyles.heading);
  console.log("%c  URL   %c https://github.com/datawranglerai/self-host-n8n-on-gcr", consoleStyles.label, consoleStyles.url);
  console.log("%c  SIGNAL%c  600+ GitHub Stars", consoleStyles.label, consoleStyles.signal);
  console.log("%c  INTEL %c  Includes direct contributions from the Google Cloud Run team in Silicon Valley.", consoleStyles.labelIntel, consoleStyles.value);
  console.groupEnd();
  console.groupCollapsed("%c02%c  where was i?", consoleStyles.indexAmber, consoleStyles.heading);
  console.log("%c  URL   %c https://app.wherewasi.co.uk", consoleStyles.label, consoleStyles.url);
  console.log("%c  INTEL %c  Sophisticated RAG AI app that helps recap books up to a certain page without spoiling anything beyond the page read.", consoleStyles.labelIntel, consoleStyles.value);
  console.groupEnd();
  console.groupCollapsed("%c03%c  Talk Data To Me", consoleStyles.indexGreen, consoleStyles.heading);
  console.log("%c  URL   %c https://www.kaggle.com/competitions/google-gemma-3n-hackathon/writeups/talk-data-to-me#3250211", consoleStyles.label, consoleStyles.url);
  console.log("%c  INTEL %c  DeepMind Hackathon entry: a real-time audio commentary programme for advanced agentic AI workflows.", consoleStyles.labelIntel, consoleStyles.value);
  console.groupEnd();
  console.groupCollapsed("%c04%c  Mortgage Overpayment Calculator", consoleStyles.indexViolet, consoleStyles.heading);
  console.log("%c  URL   %c https://datawranglerai.github.io/overpayment-calculator/", consoleStyles.label, consoleStyles.url);
  console.log("%c  INTEL %c  A simple mortgage overpayment calculator created to help manage my personal finances.", consoleStyles.labelIntel, consoleStyles.value);
  console.groupEnd();
  console.groupCollapsed("%c05%c  Declassified Reclassified", consoleStyles.indexCyan, consoleStyles.heading);
  console.log("%c  URL   %c https://gist.github.com/datawranglerai/c293db77f456f2f1130874b3a5e0291e", consoleStyles.label, consoleStyles.url);
  console.log("%c  SIGNAL%c  20 evidence records with claim-level citations", consoleStyles.label, consoleStyles.signal);
  console.log("%c  INTEL %c  Provenance-first, skeptical Python pipeline that turns messy mixed-media UAP releases into auditable SQLite-backed analysis and reports.", consoleStyles.labelIntel, consoleStyles.value);
  console.groupEnd();
  console.groupEnd();

  const typeTarget = document.querySelector(".typing-line");
  const finalText = typeTarget?.dataset.typeText || "";
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!typeTarget) return;
  if (reduceMotion) {
    typeTarget.textContent = finalText;
    typeTarget.classList.add("done");
    return;
  }

  let index = 0;
  const typeNext = () => {
    typeTarget.textContent = finalText.slice(0, index);
    index += 1;
    if (index <= finalText.length) {
      window.setTimeout(typeNext, index < 5 ? 120 : 34);
    } else {
      typeTarget.classList.add("done");
    }
  };

  window.setTimeout(typeNext, 280);
})();
