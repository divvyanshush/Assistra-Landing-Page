content = open("index.html", "r").read()

pillars_css = """
    /* ───── 4 PILLARS SECTION ───── */
    .pillars {
      background: #ffffff;
      padding: 100px 100px;
      text-align: center;
    }

    .pillars-header {
      margin-bottom: 80px;
    }

    .pillars-header h2 {
      font-family: 'Geist', sans-serif;
      font-size: 40px;
      font-weight: 500;
      color: #141413;
      line-height: 1;
      letter-spacing: -0.04em;
      margin-bottom: 16px;
    }

    .pillars-header h2 .highlight { color: #007683; }

    .pillars-header p {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      line-height: 1.6;
    }

    .pillars-list {
      display: flex;
      flex-direction: column;
      gap: 64px;
      text-align: left;
    }

    .pillar-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 80px;
      align-items: center;
    }

    .pillar-row.reverse { direction: rtl; }
    .pillar-row.reverse > * { direction: ltr; }

    .pillar-text h3 {
      font-family: 'Geist', sans-serif;
      font-size: 20px;
      font-weight: 500;
      color: #141413;
      margin-bottom: 12px;
    }

    .pillar-text p {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      line-height: 1.6;
      margin-bottom: 20px;
    }

    .pillar-text ul {
      list-style: none;
      padding: 0;
      margin: 0 0 24px 0;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .pillar-text ul li {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .pillar-text ul li::before {
      content: '·';
      color: #007683;
      font-size: 20px;
      line-height: 1;
    }

    .pillar-link {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: #007683;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: gap 0.2s;
    }

    .pillar-link:hover { gap: 10px; }

    .pillar-image {
      border-radius: 16px;
      overflow: hidden;
      border: 1px solid rgba(0,118,131,0.08);
    }

    .pillar-image img {
      width: 100%;
      height: auto;
      display: block;
    }
"""

pillars_html = """
  <!-- 4 PILLARS SECTION -->
  <section class="pillars">
    <div class="pillars-header">
      <h2>Everything Your <span class="highlight">Brand</span> Runs On</h2>
      <p>One platform for strategy, operations, finance, and execution. Built for e-commerce brands that mean business.</p>
    </div>

    <div class="pillars-list">

      <!-- Pillar 1: Product Planning -->
      <div class="pillar-row">
        <div class="pillar-text">
          <h3>Product Planning</h3>
          <p>Set goals, surface opportunities, and make smarter decisions with insights that are actually connected to your business.</p>
          <ul>
            <li>Define revenue, margin, and growth targets</li>
            <li>Identify winning products and gaps</li>
            <li>Turn insights into actionable plans</li>
          </ul>
          <a href="#" class="pillar-link">Explore Product Planning <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L9 4M13 8L9 12" stroke="#007683" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </div>
        <div class="pillar-image">
          <img src="/Public/planning.png" alt="Product Planning" />
        </div>
      </div>

      <!-- Pillar 2: Product Operations -->
      <div class="pillar-row reverse">
        <div class="pillar-text">
          <h3>Product Operations</h3>
          <p>Manage your products, inventory, and warehouse in real time without jumping between platforms.</p>
          <ul>
            <li>Live inventory and stock visibility</li>
            <li>Manage SKUs, variants, and catalog at scale</li>
            <li>Sync warehouse operations seamlessly</li>
          </ul>
          <a href="#" class="pillar-link">Explore Product Operations <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L9 4M13 8L9 12" stroke="#007683" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </div>
        <div class="pillar-image">
          <img src="/Public/operations.png" alt="Product Operations" />
        </div>
      </div>

      <!-- Pillar 3: Commerce Finance -->
      <div class="pillar-row">
        <div class="pillar-text">
          <h3>Commerce Finance</h3>
          <p>Track margins and P&L across your entire business. Know your numbers before they become problems.</p>
          <ul>
            <li>Real-time margin visibility across products</li>
            <li>Track costs, fees, and profitability drivers</li>
            <li>Clear, always up-to-date P&L</li>
          </ul>
          <a href="#" class="pillar-link">Explore Commerce Finance <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L9 4M13 8L9 12" stroke="#007683" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </div>
        <div class="pillar-image">
          <img src="/Public/finance.png" alt="Commerce Finance" />
        </div>
      </div>

      <!-- Pillar 4: Execution -->
      <div class="pillar-row reverse">
        <div class="pillar-text">
          <h3>Execution</h3>
          <p>Turn strategy into action. Manage tasks and connect your existing tools so nothing slips.</p>
          <ul>
            <li>Plan, assign, and track work in one place</li>
            <li>Connect your tools and workflows seamlessly</li>
            <li>Ensure nothing slips across teams</li>
          </ul>
          <a href="#" class="pillar-link">Explore Execution <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L9 4M13 8L9 12" stroke="#007683" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </div>
        <div class="pillar-image">
          <img src="/Public/execution.png" alt="Execution" />
        </div>
      </div>

    </div>
  </section>
"""

content = content.replace("  </style>", pillars_css + "\n  </style>")
content = content.replace("</body>", pillars_html + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)

print("✅ 4 Pillars section added!")
