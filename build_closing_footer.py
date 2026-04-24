content = open("index.html", "r").read()

closing_footer_css = """
    /* ───── CLOSING CTA ───── */
    .closing-cta {
      background: #ffffff;
      padding: 100px 100px;
      text-align: center;
    }

    .closing-cta h2 {
      font-family: 'Geist', sans-serif;
      font-size: 40px;
      font-weight: 500;
      color: #141413;
      line-height: 1;
      letter-spacing: -0.04em;
      margin-bottom: 16px;
    }

    .closing-cta h2 .highlight { color: #007683; }

    .closing-cta p {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      margin-bottom: 40px;
      line-height: 1.6;
    }

    .closing-cta-btns {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
    }

    /* ───── FOOTER ───── */
    footer {
      background: linear-gradient(180deg, #ffffff 0%, #F0FFF9 100%);
      padding: 40px 100px;
    }

    .footer-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      padding-bottom: 40px;
      border-bottom: 1px solid rgba(0,118,131,0.1);
      margin-bottom: 40px;
    }

    .footer-brand img {
      height: 32px;
      width: auto;
      margin-bottom: 12px;
    }

    .footer-brand p {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: rgba(0,0,0,0.45);
    }

    .footer-email-form {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }

    .footer-email-form label {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: #141413;
    }

    .footer-email-row {
      display: flex;
      gap: 12px;
      align-items: center;
    }

    .footer-email-form input {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: #141413;
      border: 1.5px solid #007683;
      border-radius: 999px;
      padding: 10px 24px;
      outline: none;
      width: 320px;
      background: transparent;
    }

    .footer-email-form input::placeholder {
      color: rgba(0,0,0,0.25);
    }

    .footer-links {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 40px;
      margin-bottom: 40px;
    }

    .footer-col h4 {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 500;
      color: #007683;
      margin-bottom: 16px;
    }

    .footer-col ul {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .footer-col ul li a {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: rgba(0,0,0,0.45);
      text-decoration: none;
      transition: color 0.2s;
    }

    .footer-col ul li a:hover { color: #007683; }

    .footer-bottom {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(0,118,131,0.1);
      padding-top: 24px;
    }

    .footer-bottom span {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: rgba(0,0,0,0.45);
    }

    .footer-bottom-links {
      display: flex;
      gap: 32px;
    }

    .footer-bottom-links a {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: rgba(0,0,0,0.45);
      text-decoration: none;
      transition: color 0.2s;
    }

    .footer-bottom-links a:hover { color: #007683; }
"""

closing_footer_html = """
  <!-- CLOSING CTA -->
  <section class="closing-cta">
    <h2>One Platform.<br>Every Part of Your <span class="highlight">E-Commerce</span> Business.</h2>
    <p>Join e-commerce brands already running smarter with Assistra.</p>
    <div class="closing-cta-btns">
      <a href="#" class="btn-stroke">Get A Demo</a>
      <a href="#" class="btn-filled">Try For Free <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L9 4M13 8L9 12" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
    </div>
  </section>

  <!-- FOOTER -->
  <footer>
    <div class="footer-top">
      <div class="footer-brand">
        <img src="/Public/assistra.png" alt="Assistra" />
        <p>The operating system for ecommerce founders.</p>
      </div>
      <div class="footer-email-form">
        <label>Business Email:</label>
        <div class="footer-email-row">
          <input type="email" placeholder="" />
          <a href="#" class="btn-filled">Stay Updated</a>
        </div>
      </div>
    </div>

    <div class="footer-links">
      <div class="footer-col">
        <h4>Products</h4>
        <ul>
          <li><a href="#">Strategy</a></li>
          <li><a href="#">Margin and P&L</a></li>
          <li><a href="#">Inventory</a></li>
          <li><a href="#">Review Insights</a></li>
          <li><a href="#">Opportunities</a></li>
          <li><a href="#">Goals and Strategy</a></li>
          <li><a href="#">Tasks</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Solution</h4>
        <ul>
          <li><a href="#">Amazon Sellers</a></li>
          <li><a href="#">D2C Brands</a></li>
          <li><a href="#">Multi-brand Founders</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Compare</h4>
        <ul>
          <li><a href="#">Assistra vs Helium10</a></li>
          <li><a href="#">Assistra vs Seller Central</a></li>
          <li><a href="#">Assistra vs Shopify Analytics</a></li>
          <li><a href="#">Assistra vs Jungle Scout</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Resources</h4>
        <ul>
          <li><a href="#">Case Studies</a></li>
          <li><a href="#">User Guide</a></li>
          <li><a href="#">Help and Feedback</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="#">About</a></li>
          <li><a href="#">Pricing</a></li>
          <li><a href="#">Contact us</a></li>
          <li><a href="#">Careers</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <span>© 2026 Assistra. All rights reserved.</span>
      <div class="footer-bottom-links">
        <a href="#">Terms & Conditions</a>
        <a href="#">Privacy</a>
        <a href="#">Data Deletion</a>
        <a href="#">Support</a>
      </div>
    </div>
  </footer>
"""

content = content.replace("  </style>", closing_footer_css + "\n  </style>")
content = content.replace("</body>", closing_footer_html + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)

print("✅ Closing CTA + Footer added!")
