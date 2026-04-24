content = open("index.html", "r").read()

problem_css = """
    /* ───── PROBLEM SECTION ───── */
    .problem {
      background: #ffffff;
      padding: 100px 100px;
      text-align: center;
    }

    .problem-header {
      margin-bottom: 64px;
    }

    .problem-header h2 {
      font-family: 'Geist', sans-serif;
      font-size: 40px;
      font-weight: 500;
      color: #141413;
      line-height: 1.2;
      margin-bottom: 16px;
    }

    .problem-header h2 .highlight {
      color: #007683;
    }

    .problem-header p {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      max-width: 680px;
      margin: 0 auto;
      line-height: 1.6;
    }

    .problem-cards {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }

    .problem-card {
      background: #ffffff;
      border: 1px solid rgba(0,0,0,0.08);
      border-radius: 16px;
      padding: 40px 32px;
      text-align: left;
    }

    .problem-card img {
      width: 60px;
      height: 60px;
      object-fit: contain;
      margin-bottom: 24px;
    }

    .problem-card h3 {
      font-family: 'Geist', sans-serif;
      font-size: 20px;
      font-weight: 500;
      color: #141413;
      margin-bottom: 12px;
    }

    .problem-card p {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      line-height: 1.6;
    }
"""

problem_html = """
  <!-- PROBLEM SECTION -->
  <section class="problem">
    <div class="problem-header">
      <h2>Your Tools Aren't the Problem.<br>The <span class="highlight">Fragmentation</span> Is.</h2>
      <p>Growing e-commerce brands don't fail from lack of tools. They fail because none of those tools work together.</p>
    </div>

    <div class="problem-cards">
      <div class="problem-card">
        <img src="/Public/blocks.png" alt="Too Many Tools" />
        <h3>Too Many Tools</h3>
        <p>Inventory here. Strategy there. Finances somewhere else. Most brands run on 6+ disconnected tools and still don't have a clear picture of their business.</p>
      </div>
      <div class="problem-card">
        <img src="/Public/eye-closed.png" alt="Decisions Made Blind" />
        <h3>Decisions Made Blind</h3>
        <p>Without everything in one place, you're always working from incomplete data. Missed margins. Slow decisions. Opportunities you never saw coming.</p>
      </div>
      <div class="problem-card">
        <img src="/Public/scale-3d.png" alt="Operations That Don't Scale" />
        <h3>Operations That Don't Scale</h3>
        <p>What works at $500K breaks at $5M. Growing brands need structure — not more spreadsheets.</p>
      </div>
    </div>
  </section>
"""

content = content.replace("  </style>", problem_css + "\n  </style>")
content = content.replace("</body>", problem_html + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)

print("✅ Problem section added!")
