content = open("index.html", "r").read()

integrations_css = """
    /* ───── INTEGRATIONS SECTION ───── */
    .integrations {
      background: #ffffff;
      padding: 100px 100px;
      text-align: center;
    }

    .integrations-header {
      margin-bottom: 56px;
    }

    .integrations-header h2 {
      font-family: 'Geist', sans-serif;
      font-size: 40px;
      font-weight: 500;
      color: #141413;
      line-height: 1;
      letter-spacing: -0.04em;
      margin-bottom: 16px;
    }

    .integrations-header h2 .highlight { color: #007683; }

    .integrations-header p {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      line-height: 1.6;
    }

    .integrations-grid {
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-bottom: 48px;
    }

    .integrations-row {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
    }

    .integration-pill {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: #007683;
      border: 1.5px solid rgba(0,118,131,0.25);
      border-radius: 999px;
      padding: 10px 24px;
      background: transparent;
      white-space: nowrap;
      transition: background 0.2s, color 0.2s;
    }

    .integration-pill:hover {
      background: rgba(0,118,131,0.06);
    }
"""

integrations_html = """
  <!-- INTEGRATIONS SECTION -->
  <section class="integrations">
    <div class="integrations-header">
      <h2>Connects With <span class="highlight">Everything</span> You Already Use.</h2>
      <p>Shopify, Amazon, WooCommerce, QuickBooks and more<br>Assistra plugs into your existing stack so you don't have to start from scratch.</p>
    </div>

    <div class="integrations-grid">
      <div class="integrations-row">
        <span class="integration-pill">Amazon</span>
        <span class="integration-pill">Shopify</span>
        <span class="integration-pill">EBay</span>
        <span class="integration-pill">WooCommerce</span>
        <span class="integration-pill">TikTok Shop</span>
        <span class="integration-pill">Etsy</span>
        <span class="integration-pill">QuickBooks</span>
        <span class="integration-pill">Xero</span>
        <span class="integration-pill">Shippo</span>
      </div>
      <div class="integrations-row">
        <span class="integration-pill">Loop</span>
        <span class="integration-pill">3PL</span>
        <span class="integration-pill">Central</span>
        <span class="integration-pill">ShipBob</span>
        <span class="integration-pill">FedEx</span>
        <span class="integration-pill">DHL</span>
        <span class="integration-pill">Walmart</span>
        <span class="integration-pill">Wayfair</span>
        <span class="integration-pill">Noon</span>
        <span class="integration-pill">Flipkart</span>
        <span class="integration-pill">Faire</span>
      </div>
      <div class="integrations-row">
        <span class="integration-pill">Cin7</span>
        <span class="integration-pill">Brightpearl</span>
        <span class="integration-pill">Klaviyo</span>
        <span class="integration-pill">Gorgias</span>
        <span class="integration-pill">Stripe</span>
        <span class="integration-pill">PayPal</span>
        <span class="integration-pill">Returnly</span>
        <span class="integration-pill">AfterShip</span>
        <span class="integration-pill">Royal Mail</span>
      </div>
    </div>

    <a href="#" class="btn-filled">See All Integrations <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L9 4M13 8L9 12" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
  </section>
"""

content = content.replace("  </style>", integrations_css + "\n  </style>")
content = content.replace("</body>", integrations_html + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)

print("✅ Integrations section added!")
