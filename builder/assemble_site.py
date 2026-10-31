# builder/assemble_site.py
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding='utf-8')

from app_css import APP_CSS
from app_js import APP_JS

print("Assembling final index.html...")

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PrepMaster Pro — Complete Placement & Competitive Exam Learning Platform</title>

  <!-- KaTeX CSS & JS for LaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>

  <style>
{APP_CSS}
  </style>
</head>
<body>

  <!-- TOPBAR -->
  <header class="topbar">
    <div class="topbar-left">
      <!-- Visible Three-Dot Navigation Menu Button -->
      <button class="three-dot-btn" id="three-dot-toggle" title="Open Syllabus Navigator (Three-dot Menu)" aria-label="Open Navigation">
        &#8942;
      </button>
      <div class="brand-title" onclick="navigateTo('catalog')">
        <span>PrepMaster <span style="color:var(--pri)">Pro</span></span>
        <span class="badge" id="global-verified-badge">32,900 Verified Qs (75/15/10 Rule)</span>
      </div>
    </div>

    <div class="topbar-right">
      <button class="btn" onclick="navigateTo('catalog')" title="All Syllabus Topics">📚 Topics</button>
      <button class="btn" onclick="navigateTo('formulas')" title="Formula Book">📐 Formulas</button>
      <button class="btn" onclick="navigateTo('study', CUR_TOPIC)" title="Study Notes">📖 Study Notes</button>
      <button class="btn" onclick="navigateTo('reports')" title="Analytics & Progress">📊 Reports</button>
      <button class="btn" onclick="navigateTo('admin')" title="Content Management">⚙️ Admin</button>
      <button class="btn" onclick="openShortcutsModal()" title="Keyboard Shortcuts Help">⌨️ Keys</button>

      <button class="user-btn" onclick="openSettingsModal()" title="User Profile & Settings">
        <div class="user-avatar" id="header-user-avatar">K</div>
        <span id="header-user-name">Kalidass S</span>
      </button>
    </div>
  </header>

  <!-- SIDEBAR DRAWER & BACKDROP -->
  <div id="sidebar-backdrop"></div>
  <aside id="sidebar" aria-label="Main Navigation">
    <div class="sidebar-header">
      <div style="display:flex;align-items:center;gap:8px">
        <b style="font-size:1.15rem">Syllabus Navigator</b>
        <span class="diff-pill easy" style="font-size:0.72rem">327 Topics</span>
      </div>
      <button class="btn btn-sm" onclick="toggleSidebar(false)">✕</button>
    </div>

    <div class="sidebar-nav">
      <button class="btn btn-sm" onclick="navigateTo('catalog')">🏠 Home Catalog</button>
      <button class="btn btn-sm" onclick="navigateTo('practice', CUR_TOPIC)">⚡ Practice Mode</button>
      <button class="btn btn-sm" onclick="navigateTo('test', CUR_TOPIC)">⏱️ Mock Exams</button>
      <button class="btn btn-sm" onclick="navigateTo('study', CUR_TOPIC)">📖 Study Guides</button>
      <button class="btn btn-sm" onclick="navigateTo('formulas')">📐 Formula Book</button>
      <button class="btn btn-sm" onclick="navigateTo('bookmarks')">★ Bookmarks</button>
      <button class="btn btn-sm" onclick="navigateTo('reports')">📊 Analytics</button>
      <button class="btn btn-sm" onclick="navigateTo('admin')">⚙️ Content Admin</button>
    </div>

    <div class="sidebar-topic-list" id="sidebar-topics-container">
      <!-- Generated dynamically from catalog -->
    </div>
  </aside>

  <!-- MAIN CONTAINER -->
  <main class="container">

    <!-- 1. CATEGORY SWITCHER TABS -->
    <div class="category-tabs">
      <button class="cat-tab-btn active" data-cat="all">All Categories (327 Topics)</button>
      <button class="cat-tab-btn" data-cat="Coding Questions">💻 Coding Questions (166 Topics)</button>
      <button class="cat-tab-btn" data-cat="Quantitative Aptitude">📐 Quantitative Aptitude (74 Topics)</button>
      <button class="cat-tab-btn" data-cat="Verbal Ability and Logical Reasoning">🧠 Verbal & Logical (87 Topics)</button>
    </div>

    <!-- VIEW 1: CATALOG VIEW -->
    <div id="catalog-view">
      <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap;">
        <div style="flex:1;min-width:280px;">
          <input type="text" id="catalog-search-input" class="search-input" placeholder="🔍 Search any topic across all 327 subjects (e.g. Binary Search, Dynamic Programming, Percentage, Syllogisms)...">
        </div>
        <div style="display:flex;gap:8px;align-items:center;">
          <span class="diff-pill easy" id="catalog-count-pill">327 Topics</span>
          <button class="btn btn-sm" onclick="navigateTo('practice', 'coding_pf_basic')">⚡ Quick Start Practice</button>
        </div>
      </div>
      <div class="topic-grid" id="catalog-grid"></div>
    </div>

    <!-- VIEW 2: PRACTICE VIEW -->
    <div id="practice-view" style="display:none;">
      <div id="practice-card-container"></div>
    </div>

    <!-- VIEW 3: TEST VIEW -->
    <div id="test-view" style="display:none;">
      <div style="display:flex;justify-content:space-between;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 18px;margin-bottom:16px;">
        <div style="font-weight:700;font-size:1.1rem;">⏱️ Mock Examination Mode</div>
        <div style="display:flex;align-items:center;gap:12px;">
          <span>Time Remaining:</span>
          <span id="test-timer-display" style="font-size:1.4rem;font-weight:900;color:var(--pri);font-family:monospace;">60:00</span>
          <button class="btn btn-primary btn-sm" onclick="confirmSubmitTest()" style="background:var(--ok);border-color:var(--ok);">Submit Test</button>
        </div>
      </div>

      <div class="test-layout">
        <div id="test-card-container"></div>
        <div id="test-palette-container"></div>
      </div>
    </div>

    <!-- VIEW 4: TEST RESULT VIEW -->
    <div id="test-result-view" style="display:none;">
      <div id="test-result-container"></div>
    </div>

    <!-- VIEW 5: STUDY MATERIAL VIEW -->
    <div id="study-view" style="display:none;">
      <div id="study-container"></div>
    </div>

    <!-- VIEW 6: FORMULA BOOK VIEW -->
    <div id="formulas-view" style="display:none;">
      <div style="margin-bottom:20px;">
        <h2>📐 Dedicated Formula Book & Mathematical Reference</h2>
        <input type="text" id="formula-search-input" class="search-input" placeholder="Search formulas by name, concept, or variable..." oninput="renderFormulaBook()">
      </div>
      <div class="formula-grid" id="formulas-container"></div>
    </div>

    <!-- VIEW 7: PERFORMANCE REPORTS VIEW -->
    <div id="reports-view" style="display:none;">
      <div id="reports-container"></div>
    </div>

    <!-- VIEW 8: ADMIN & CONTENT MANAGEMENT VIEW -->
    <div id="admin-view" style="display:none;">
      <div id="admin-container"></div>
    </div>

    <!-- VIEW 9: BOOKMARKS VIEW -->
    <div id="bookmarks-view" style="display:none;">
      <div id="bookmarks-container"></div>
    </div>

  </main>

  <!-- SETTINGS MODAL -->
  <div id="settings-modal" class="modal-backdrop">
    <div class="modal-dialog">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h3 style="margin:0;">User Profile & Personalization</h3>
        <button class="btn btn-sm" onclick="closeSettingsModal()">✕</button>
      </div>

      <div style="display:flex;flex-direction:column;gap:16px;">
        <div>
          <label style="font-weight:600;font-size:0.9rem;">Display Theme</label>
          <select id="theme-select" class="search-input" style="margin-top:6px;" onchange="handleThemeChange(this.value)">
            <option value="dark">Dark Theme (Recommended)</option>
            <option value="light">Light Theme</option>
            <option value="forest">Emerald Forest</option>
            <option value="dragon">Dragon Crimson</option>
            <option value="ocean">Deep Ocean</option>
            <option value="wizard">Arcane Wizard Purple</option>
            <option value="fairy">Fairy Blossom</option>
            <option value="royal">Royal Amber</option>
          </select>
        </div>

        <div>
          <label style="font-weight:600;font-size:0.9rem;">Base Font Size (px)</label>
          <input type="range" id="font-size-input" min="13" max="22" value="16" style="width:100%;margin-top:6px;" oninput="handleFontSizeChange(this.value)">
        </div>

        <div>
          <label style="font-weight:600;font-size:0.9rem;">Content Card Width (px)</label>
          <input type="range" id="card-width-input" min="760" max="1400" value="1000" style="width:100%;margin-top:6px;" oninput="handleCardWidthChange(this.value)">
        </div>

        <div style="border-top:1px solid var(--line);padding-top:16px;display:flex;justify-content:flex-end;">
          <button class="btn btn-primary" onclick="closeSettingsModal()">Save & Close</button>
        </div>
      </div>
    </div>
  </div>

  <!-- KEYBOARD SHORTCUTS GUIDE MODAL -->
  <div id="shortcuts-modal" class="modal-backdrop">
    <div class="modal-dialog">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h3 style="margin:0;">⌨️ Complete Keyboard Shortcuts Reference</h3>
        <button class="btn btn-sm" onclick="closeShortcutsModal()">✕</button>
      </div>

      <div style="display:flex;flex-direction:column;gap:16px;font-size:0.9rem;">
        <div>
          <h4 style="color:var(--pri);margin:0 0 6px 0;">⚡ Practice Mode Shortcuts</h4>
          <table style="width:100%;border-collapse:collapse;">
            <tr><td style="padding:4px 0;"><b>Up / Down Arrow</b></td><td>Move focus between options</td></tr>
            <tr><td style="padding:4px 0;"><b>Enter</b></td><td>Select focused option; if answered, advance to next question</td></tr>
            <tr><td style="padding:4px 0;"><b>1, 2, 3, 4 or A, B, C, D</b></td><td>Select corresponding option immediately</td></tr>
            <tr><td style="padding:4px 0;"><b>Left / Right Arrow</b></td><td>Previous / Next question</td></tr>
            <tr><td style="padding:4px 0;"><b>H</b></td><td>Show or hide hint clue</td></tr>
            <tr><td style="padding:4px 0;"><b>S</b></td><td>Show verified correct answer & solution</td></tr>
            <tr><td style="padding:4px 0;"><b>R</b></td><td>Reset current question attempt</td></tr>
            <tr><td style="padding:4px 0;"><b>M</b></td><td>Switch to Test mode for this topic</td></tr>
          </table>
        </div>

        <div style="border-top:1px solid var(--line);padding-top:10px;">
          <h4 style="color:var(--purple);margin:0 0 6px 0;">⏱️ Test Mode Shortcuts</h4>
          <table style="width:100%;border-collapse:collapse;">
            <tr><td style="padding:4px 0;"><b>1, 2, 3, 4 / A, B, C, D</b></td><td>Record answer and advance to next question</td></tr>
            <tr><td style="padding:4px 0;"><b>Left / Right Arrow</b></td><td>Previous / Next question</td></tr>
            <tr><td style="padding:4px 0;"><b>Shift + Enter</b></td><td>Submit examination (with confirmation)</td></tr>
            <tr><td style="padding:4px 0;"><b>M</b></td><td>Switch to Practice mode</td></tr>
          </table>
        </div>

        <div style="border-top:1px solid var(--line);padding-top:10px;">
          <h4 style="color:var(--ok);margin:0 0 6px 0;">🌐 Global & Study Navigation</h4>
          <table style="width:100%;border-collapse:collapse;">
            <tr><td style="padding:4px 0;"><b>[ and ]</b></td><td>Cycle main categories (Coding, Quant, Verbal)</td></tr>
            <tr><td style="padding:4px 0;"><b>Ctrl + Left / Right</b></td><td>Previous / Next category</td></tr>
            <tr><td style="padding:4px 0;"><b>/ (Forward Slash)</b></td><td>Focus study material search field</td></tr>
            <tr><td style="padding:4px 0;"><b>Escape</b></td><td>Close any open modal or navigation drawer</td></tr>
          </table>
        </div>

        <div style="border-top:1px solid var(--line);padding-top:12px;text-align:right;">
          <button class="btn btn-primary" onclick="closeShortcutsModal()">Got It</button>
        </div>
      </div>
    </div>
  </div>

  <!-- LOAD PERSISTENT QUESTION DATA CHUNKS (CORS SAFE FOR FILE:// AND HTTP) -->
  <script src="data/catalog_and_meta.js"></script>
  <script src="data/coding_part1.js"></script>
  <script src="data/coding_part2.js"></script>
  <script src="data/quant_questions.js"></script>
  <script src="data/verbal_logical_questions.js"></script>

  <!-- APPLICATION ENGINE SCRIPT -->
  <script>
{APP_JS}
  </script>
</body>
</html>
"""

out_html = "f:/placement/1round ready2/index.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"index.html generated successfully! File size: {os.path.getsize(out_html) / 1024:.2f} KB")
