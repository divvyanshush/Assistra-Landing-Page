content = open("index.html", "r").read()

hero = """
  <!-- HERO -->
  <section class="hero">

    <!-- Social Proof Row -->
    <div class="hero-proof">
      <div class="proof-g2">
        <span class="stars">★★★★★</span>
        <span class="rating">5/5</span>
        <img src="/Public/g2.png" alt="G2" class="g2-logo" />
      </div>
      <div class="proof-divider"></div>
      <div class="proof-agency">
        <img src="/Public/agency.png" alt="Trusted agencies" class="agency-faces" />
        <span class="proof-text">trusted by 20+ agencies globally</span>
      </div>
    </div>

    <!-- Headline -->
    <h1 class="hero-headline">
      Stop Switching Tools. Run Your Entire<br>
      <span class="highlight">E-Commerce</span> Business From One Place.
    </h1>

    <!-- Subheadline -->
    <p class="hero-sub">
      Assistra brings your planning, operations, finance, and execution into one platform<br>
      built for e-commerce brands that are serious about scaling.
    </p>

    <!-- CTA Buttons -->
    <div class="hero-ctas">
      <a href="#" class="btn-stroke">Book A Demo</a>
      <a href="#" class="btn-filled">Try For Free →</a>
    </div>

    <!-- Trust Badges -->
    <div class="hero-badges">
      <div class="badge">
        <img src="/Public/calendar-check.png" alt="" />
        <span>14 days free trial</span>
      </div>
      <div class="badge">
        <img src="/Public/credit-card.png" alt="" />
        <span>no cc required</span>
      </div>
      <div class="badge">
        <img src="/Public/circle-x.png" alt="" />
        <span>cancel anytime</span>
      </div>
    </div>

  </section>
"""

hero_css = """
    /* ───── HERO ───── */
    .hero {
      background: linear-gradient(180deg, #F0FFF9 0%, #ffffff 100%);
      padding: 100px 100px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    /* Social Proof */
    .hero-proof {
      display: flex;
      align-items: center;
      gap: 24px;
      margin-bottom: 40px;
    }

    .proof-g2 {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .stars {
      color: #E8441A;
      font-size: 16px;
      letter-spacing: 2px;
    }

    .rating {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 500;
      color: #141413;
    }

    .g2-logo {
      height: 24px;
      width: auto;
    }

    .proof-divider {
      width: 1px;
      height: 24px;
      background: rgba(0,0,0,0.15);
    }

    .proof-agency {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .agency-faces {
      height: 36px;
      width: auto;
    }

    .proof-text {
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: #007683;
    }

    /* Headline */
    .hero-headline {
      font-family: 'Geist', sans-serif;
      font-size: 64px;
      font-weight: 500;
      color: #141413;
      line-height: 1.1;
      letter-spacing: -1.5px;
      margin-bottom: 24px;
    }

    .hero-headline .highlight {
      color: #007683;
    }

    /* Sub */
    .hero-sub {
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      color: rgba(0,0,0,0.65);
      line-height: 1.6;
      max-width: 560px;
      margin-bottom: 40px;
    }

    /* CTAs */
    .hero-ctas {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 32px;
    }

    .btn-filled {
      background: #007683;
      color: #ffffff;
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      padding: 12px 24px;
      border: none;
      border-radius: 999px;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: opacity 0.2s, transform 0.2s;
      white-space: nowrap;
    }

    .btn-filled:hover { opacity: 0.88; transform: translateY(-1px); }

    .btn-stroke {
      background: rgba(0,118,131,0.08);
      color: #007683;
      font-family: 'Geist', sans-serif;
      font-size: 16px;
      font-weight: 400;
      padding: 12px 24px;
      border: 1.5px solid rgba(0,118,131,0.35);
      border-radius: 999px;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: opacity 0.2s, transform 0.2s;
      white-space: nowrap;
    }

    .btn-stroke:hover { opacity: 0.8; transform: translateY(-1px); }

    /* Badges */
    .hero-badges {
      display: flex;
      align-items: center;
      gap: 32px;
    }

    .badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: 'Geist', sans-serif;
      font-size: 14px;
      font-weight: 400;
      color: rgba(0,0,0,0.45);
    }

    .badge img {
      height: 18px;
      width: auto;
      opacity: 0.45;
    }
"""

# Inject CSS before </style>
content = content.replace("  </style>", hero_css + "\n  </style>")

# Inject Hero before </body>
content = content.replace("</body>", hero + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)

print("✅ Hero section added!")
