# builder/app_css.py

APP_CSS = """
:root {
  --bg: #f4f6fa;
  --card: #ffffff;
  --card-subtle: #f8fafc;
  --ink: #1e293b;
  --mut: #64748b;
  --pri: #2563eb;
  --priL: #dbeafe;
  --priHover: #1d4ed8;
  --ok: #16a34a;
  --okL: #dcfce7;
  --okBorder: #86efac;
  --bad: #dc2626;
  --badL: #fee2e2;
  --badBorder: #fca5a5;
  --line: #e2e8f0;
  --warn: #d97706;
  --warnL: #fef3c7;
  --purple: #7c3aed;
  --purpleL: #ede9fe;
  --maxw: 1000px;
  --font-size: 16px;
  --card-pad: 20px;
  --radius: 12px;
  --shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
}

:root[data-theme="dark"] {
  --bg: #0b1017;
  --card: #151d28;
  --card-subtle: #1a2332;
  --ink: #f1f5f9;
  --mut: #94a3b8;
  --pri: #3b82f6;
  --priL: #1e2d42;
  --priHover: #60a5fa;
  --ok: #22c55e;
  --okL: #132f1e;
  --okBorder: #166534;
  --bad: #ef4444;
  --badL: #3b1717;
  --badBorder: #991b1b;
  --line: #243142;
  --warn: #f59e0b;
  --warnL: #362912;
  --purple: #a855f7;
  --purpleL: #2e1d44;
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

:root[data-theme="forest"] {
  --bg: #091811; --card: #11261c; --card-subtle: #173326; --ink: #e8f5ee; --mut: #8eb39d;
  --pri: #10b981; --priL: #163e2c; --priHover: #34d399; --ok: #22c55e; --okL: #132f1e;
  --bad: #f87171; --badL: #3b1717; --line: #1c422f; --warn: #fbbf24;
}

:root[data-theme="dragon"] {
  --bg: #140d12; --card: #22141e; --card-subtle: #2d1b28; --ink: #fde8ef; --mut: #b88da0;
  --pri: #f43f5e; --priL: #3d1724; --priHover: #fb7185; --ok: #10b981; --okL: #132f1e;
  --bad: #ff3344; --badL: #451216; --line: #3d2335; --warn: #fbbf24;
}

:root[data-theme="ocean"] {
  --bg: #071924; --card: #0e2738; --card-subtle: #13334a; --ink: #e0f2fe; --mut: #7dd3fc;
  --pri: #0284c7; --priL: #133e5c; --priHover: #38bdf8; --ok: #14b8a6; --okL: #0d332f;
  --bad: #f43f5e; --badL: #3d1724; --line: #194663; --warn: #f59e0b;
}

:root[data-theme="wizard"] {
  --bg: #0d0b1a; --card: #17132e; --card-subtle: #201b40; --ink: #f3e8ff; --mut: #c084fc;
  --pri: #9333ea; --priL: #2c164a; --priHover: #c084fc; --ok: #10b981; --okL: #132f1e;
  --bad: #f43f5e; --badL: #3d1724; --line: #31285e; --warn: #fbbf24;
}

:root[data-theme="fairy"] {
  --bg: #fdf2f8; --card: #ffffff; --card-subtle: #fce7f3; --ink: #3b0764; --mut: #86198f;
  --pri: #c026d3; --priL: #fae8ff; --priHover: #e879f9; --ok: #16a34a; --okL: #dcfce7;
  --bad: #dc2626; --badL: #fee2e2; --line: #f5d0fe; --warn: #d97706;
}

:root[data-theme="royal"] {
  --bg: #fcf9f2; --card: #ffffff; --card-subtle: #f7f0e3; --ink: #451a03; --mut: #78350f;
  --pri: #b45309; --priL: #fef3c7; --priHover: #d97706; --ok: #15803d; --okL: #dcfce7;
  --bad: #b91c1c; --badL: #fee2e2; --line: #fde68a; --warn: #b45309;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: var(--font-size);
  line-height: 1.55;
  transition: background 0.2s, color 0.2s;
  overflow-x: hidden;
}

/* TOPBAR */
header.topbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--card);
  border-bottom: 1px solid var(--line);
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
}
.topbar-left {
  display: flex;
  align-items: center;
  gap: 14px;
}
.three-dot-btn {
  background: transparent;
  border: 1px solid var(--line);
  border-radius: 8px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: var(--ink);
  cursor: pointer;
  transition: all 0.2s;
}
.three-dot-btn:hover {
  background: var(--priL);
  color: var(--pri);
  border-color: var(--pri);
}
.brand-title {
  font-weight: 800;
  font-size: 1.25rem;
  letter-spacing: -0.02em;
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}
.brand-title span.badge {
  font-size: 0.72rem;
  padding: 3px 8px;
  border-radius: 99px;
  background: var(--okL);
  color: var(--ok);
  font-weight: 700;
  border: 1px solid var(--okBorder);
}
.topbar-right {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.btn {
  background: var(--card);
  color: var(--ink);
  border: 1px solid var(--line);
  padding: 7px 14px;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s;
  user-select: none;
}
.btn:hover {
  background: var(--priL);
  color: var(--pri);
  border-color: var(--pri);
}
.btn.active, .btn-primary {
  background: var(--pri);
  color: #ffffff;
  border-color: var(--pri);
}
.btn.active:hover, .btn-primary:hover {
  background: var(--priHover);
}
.btn-sm {
  padding: 4px 10px;
  font-size: 0.8rem;
}
.user-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 10px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: var(--card-subtle);
  cursor: pointer;
  font-weight: 600;
  font-size: 0.88rem;
}
.user-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--pri);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
}

/* SIDEBAR DRAWER */
#sidebar-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(2px);
  z-index: 150;
  display: none;
}
#sidebar-backdrop.open { display: block; }
#sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 360px;
  max-width: 85vw;
  background: var(--card);
  border-right: 1px solid var(--line);
  z-index: 200;
  transform: translateX(-100%);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  box-shadow: 4px 0 24px rgba(0,0,0,0.15);
}
#sidebar.open { transform: translateX(0); }
.sidebar-header {
  padding: 16px;
  border-bottom: 1px solid var(--line);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.sidebar-search {
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
}
.search-input {
  width: 100%;
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: var(--bg);
  color: var(--ink);
  font-size: 0.9rem;
}
.sidebar-nav {
  padding: 10px 16px;
  border-bottom: 1px solid var(--line);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}
.sidebar-topic-list {
  flex: 1;
  overflow-y: auto;
  padding: 8px 12px;
}
.topic-tree-group {
  margin-bottom: 12px;
}
.topic-tree-group h4 {
  margin: 8px 6px 4px 6px;
  font-size: 0.78rem;
  text-transform: uppercase;
  color: var(--mut);
  letter-spacing: 0.05em;
}
.topic-nav-item {
  padding: 8px 10px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.88rem;
  color: var(--ink);
  text-decoration: none;
  cursor: pointer;
  transition: background 0.15s;
}
.topic-nav-item:hover, .topic-nav-item.active {
  background: var(--priL);
  color: var(--pri);
  font-weight: 600;
}

/* MAIN LAYOUT */
main.container {
  max-width: var(--maxw);
  margin: 24px auto;
  padding: 0 16px 80px 16px;
}

/* SECTION TABS (Category Switcher) */
.category-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  overflow-x: auto;
  padding-bottom: 4px;
}
.cat-tab-btn {
  padding: 10px 18px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--mut);
  font-weight: 700;
  font-size: 0.95rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
  transition: all 0.2s;
}
.cat-tab-btn:hover {
  color: var(--ink);
  border-color: var(--pri);
}
.cat-tab-btn.active {
  background: var(--pri);
  color: white;
  border-color: var(--pri);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
}

/* TOPIC CATALOG GRID */
.topic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
  gap: 16px;
  margin-top: 16px;
}
.topic-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 12px;
  box-shadow: var(--shadow);
  transition: transform 0.15s, border-color 0.15s;
}
.topic-card:hover {
  transform: translateY(-2px);
  border-color: var(--pri);
}
.topic-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 8px;
}
.topic-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--ink);
  margin: 0;
}
.topic-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  font-size: 0.8rem;
  color: var(--mut);
}
.diff-pill {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
}
.diff-pill.hard { background: var(--badL); color: var(--bad); }
.diff-pill.med { background: var(--warnL); color: var(--warn); }
.diff-pill.easy { background: var(--okL); color: var(--ok); }
.topic-actions {
  display: flex;
  gap: 8px;
  margin-top: 4px;
}

/* QUESTION CARD (PRACTICE & TEST) */
.q-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: var(--card-pad);
  box-shadow: var(--shadow);
  margin-bottom: 20px;
}
.q-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--line);
}
.q-badges {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.q-statement {
  font-size: 1.15rem;
  font-weight: 600;
  line-height: 1.6;
  margin-bottom: 20px;
}
.q-code-block {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.92rem;
  overflow-x: auto;
  margin: 12px 0 20px 0;
  line-height: 1.45;
}

/* OPTIONS LIST */
.options-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}
.option-item {
  background: var(--card);
  border: 2px solid var(--line);
  border-radius: 10px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  transition: all 0.15s ease-out;
  position: relative;
  user-select: none;
}
.option-item:hover {
  background: var(--card-subtle);
  border-color: var(--pri);
}
.option-item.focused {
  outline: 2px solid var(--pri);
  background: var(--priL);
}
.option-badge {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: var(--bg);
  border: 1px solid var(--line);
  color: var(--mut);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
  flex-shrink: 0;
  transition: all 0.15s;
}
.option-text {
  flex: 1;
  font-size: 1rem;
}

/* INSTANT FEEDBACK STATES (PRACTICE MODE) */
.option-item.is-correct {
  background: var(--okL) !important;
  border-color: var(--ok) !important;
  color: var(--ink) !important;
}
.option-item.is-correct .option-badge {
  background: var(--ok);
  color: white;
  border-color: var(--ok);
}
.option-item.is-wrong {
  background: var(--badL) !important;
  border-color: var(--bad) !important;
  color: var(--ink) !important;
}
.option-item.is-wrong .option-badge {
  background: var(--bad);
  color: white;
  border-color: var(--bad);
}

/* TEST MODE SELECTION */
.option-item.test-selected {
  background: var(--priL);
  border-color: var(--pri);
}
.option-item.test-selected .option-badge {
  background: var(--pri);
  color: white;
}

/* FEEDBACK & EXPLANATION BOXES */
.feedback-box {
  border-radius: 10px;
  padding: 16px;
  margin-top: 16px;
  animation: fadeIn 0.2s ease-out;
}
.feedback-box.correct {
  background: var(--okL);
  border: 1px solid var(--okBorder);
  color: var(--ink);
}
.feedback-box.wrong {
  background: var(--badL);
  border: 1px solid var(--badBorder);
  color: var(--ink);
}
.feedback-title {
  font-weight: 800;
  font-size: 1.05rem;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}
.explanation-card {
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 16px;
  margin-top: 14px;
}
.explanation-card h4 {
  margin: 0 0 8px 0;
  font-size: 0.95rem;
  color: var(--pri);
}
.step-solution {
  white-space: pre-line;
  font-size: 0.92rem;
  line-height: 1.6;
  margin-top: 8px;
}

/* QUESTION CONTROLS TOOLBAR */
.q-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid var(--line);
}
.q-nav-buttons {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* TEST PALETTE */
.test-layout {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 20px;
}
@media (max-width: 860px) {
  .test-layout { grid-template-columns: 1fr; }
}
.test-palette-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 16px;
  box-shadow: var(--shadow);
  height: fit-content;
}
.palette-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 6px;
  margin-top: 12px;
  max-height: 380px;
  overflow-y: auto;
  padding: 4px;
}
.palette-btn {
  aspect-ratio: 1;
  border-radius: 6px;
  border: 1px solid var(--line);
  background: var(--bg);
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s;
}
.palette-btn.current { outline: 2px solid var(--pri); }
.palette-btn.answered { background: var(--ok); color: white; border-color: var(--ok); }
.palette-btn.marked { background: var(--purple); color: white; border-color: var(--purple); }

/* FORMULA BOOK */
.formula-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 16px;
}
.formula-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 18px;
  box-shadow: var(--shadow);
}
.formula-latex {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px;
  margin: 12px 0;
  text-align: center;
  overflow-x: auto;
}

/* MODALS */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(3px);
  z-index: 500;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 16px;
}
.modal-backdrop.open { display: flex; }
.modal-dialog {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  padding: 24px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.25);
  animation: modalPop 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }
@keyframes modalPop { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }

/* RESPONSIVE HELPERS */
@media (max-width: 640px) {
  header.topbar { padding: 8px 12px; }
  .brand-title span.badge { display: none; }
  main.container { padding: 0 10px 60px 10px; }
  .q-statement { font-size: 1.05rem; }
}
"""
