content = open("index.html", "r").read()

social_css = """
    /* ───── SOCIAL PROOF SECTION ───── */
    .social-proof {
      background: #ffffff;
      padding: 100px 100px;
      text-align: center;
    }

    .social-proof-header {
      margin-bottom: 56px;
    }

    .social-proof-header h2 {
      font-family: 'Geist', sans-serif;
      font-size: 40px;
      font-weight: 500;
      color: #141413;
      line-height: 1;
      letter-spacing: -0.04em;
      margin-bottom: 16px;
    }

    .social-proof-header h2 .highlight { color: #007683; }

    .social-proof-header p {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      line-height: 1.6;
    }

    .testimonials-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    .testimonial-card {
      background: linear-gradient(135deg, #F0FFF9 0%, #ffffff 100%);
      border-radius: 12px;
      padding: 40px 24px;
      text-align: left;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 40px;
    }

    .testimonial-quote {
      font-family: 'Geist', sans-serif;
      font-size: 20px;
      font-weight: 500;
      color: #141413;
      line-height: 1.4;
    }

    .testimonial-author {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .testimonial-author img {
      width: 56px;
      height: 56px;
      border-radius: 999px;
      object-fit: cover;
    }

    .author-info {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .author-name {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 500;
      color: #141413;
    }

    .author-title {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: rgba(0,0,0,0.45);
    }
"""

social_html = """
  <!-- SOCIAL PROOF SECTION -->
  <section class="social-proof">
    <div class="social-proof-header">
      <h2>What E-Commerce <span class="highlight">Teams</span> Are Saying</h2>
      <p>From agencies managing 20+ clients to brands scaling past $5M. Here's what they think.</p>
    </div>

    <div class="testimonials-grid">
      <div class="testimonial-card">
        <p class="testimonial-quote">"Our team can now walk into every client meeting with a full picture of their business. Assistra made us look a lot smarter."</p>
        <div class="testimonial-author">
          <img src="/Public/Rectangle 26-1.png" alt="Ethan Cole" />
          <div class="author-info">
            <span class="author-name">Ethan Cole</span>
            <span class="author-title">President, PMA. LA</span>
          </div>
        </div>
      </div>

      <div class="testimonial-card">
        <p class="testimonial-quote">"Finally a platform that actually understands how e-commerce works. We stopped jumping between tools the day we switched to Assistra."</p>
        <div class="testimonial-author">
          <img src="/Public/Rectangle 26.png" alt="Kamal Sabnani" />
          <div class="author-info">
            <span class="author-name">Kamal Sabnani,</span>
            <span class="author-title">Principal Product Manager</span>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

content = content.replace("  </style>", social_css + "\n  </style>")
content = content.replace("</body>", social_html + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)

print("✅ Social proof section added!")
