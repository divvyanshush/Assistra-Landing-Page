content = open("index.html", "r").read()

responsive_css = """
    /* ───── RESPONSIVE ───── */

    /* Tablet: 768px - 1024px */
    @media (max-width: 1024px) {
      nav {
        padding: 20px 40px;
      }

      .hero {
        padding: 140px 40px 80px 40px;
      }

      .problem {
        padding: 80px 40px;
      }

      .pillars {
        padding: 80px 40px;
      }

      .pillars-header {
        margin-bottom: 48px;
      }

      .pillar-row {
        gap: 40px;
        padding: 0 16px;
      }

      .integrations {
        padding: 80px 40px;
      }

      .social-proof {
        padding: 80px 40px;
      }

      .closing-cta {
        padding: 80px 40px;
      }

      footer {
        padding: 40px 40px;
      }

      .footer-links {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
      }

      .hero-headline {
        font-size: 48px;
      }

      .pillar-row.reverse {
        direction: ltr;
      }

      .pillar-row.reverse .pillar-image {
        order: -1;
      }
    }

    /* Mobile: max 767px */
    @media (max-width: 767px) {
      nav {
        padding: 16px 24px;
      }

      .nav-links {
        display: none;
      }

      .hero {
        padding: 120px 24px 64px 24px;
        text-align: center;
      }

      .hero-proof {
        flex-direction: column;
        gap: 12px;
        margin-bottom: 32px;
      }

      .proof-divider {
        display: none;
      }

      .hero-headline {
        font-size: 36px;
        letter-spacing: -0.03em;
      }

      .hero-sub {
        font-size: 15px;
        max-width: 100%;
      }

      .hero-ctas {
        flex-direction: column;
        width: 100%;
        align-items: center;
      }

      .hero-ctas .btn-filled,
      .hero-ctas .btn-stroke {
        width: 100%;
        justify-content: center;
      }

      .hero-badges {
        flex-direction: column;
        gap: 12px;
        align-items: center;
      }

      .problem {
        padding: 64px 24px;
      }

      .problem-header h2 {
        font-size: 32px;
      }

      .problem-cards {
        grid-template-columns: 1fr;
        gap: 16px;
      }

      .pillars {
        padding: 64px 24px;
      }

      .pillars-header h2 {
        font-size: 32px;
      }

      .pillars-list {
        gap: 48px;
      }

      .pillar-row {
        grid-template-columns: 1fr;
        gap: 32px;
        padding: 0;
      }

      .pillar-row.reverse {
        direction: ltr;
      }

      .pillar-row.reverse .pillar-image {
        order: -1;
      }

      .integrations {
        padding: 64px 24px;
      }

      .integrations-header h2 {
        font-size: 32px;
      }

      .integrations-row {
        gap: 8px;
      }

      .integration-pill {
        font-size: 14px;
        padding: 8px 16px;
      }

      .social-proof {
        padding: 64px 24px;
      }

      .social-proof-header h2 {
        font-size: 32px;
      }

      .testimonials-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }

      .closing-cta {
        padding: 64px 24px;
      }

      .closing-cta h2 {
        font-size: 32px;
      }

      .closing-cta-btns {
        flex-direction: column;
        width: 100%;
        align-items: center;
      }

      .closing-cta-btns .btn-filled,
      .closing-cta-btns .btn-stroke {
        width: 100%;
        justify-content: center;
      }

      footer {
        padding: 40px 24px;
      }

      .footer-top {
        flex-direction: column;
        gap: 32px;
      }

      .footer-email-row {
        flex-direction: column;
        width: 100%;
      }

      .footer-email-form input {
        width: 100%;
      }

      .footer-email-form .btn-filled {
        width: 100%;
        justify-content: center;
      }

      .footer-links {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 32px;
      }

      .footer-bottom {
        flex-direction: column;
        gap: 16px;
        text-align: center;
      }

      .footer-bottom-links {
        flex-wrap: wrap;
        justify-content: center;
        gap: 16px;
      }

      .nav-logo img {
        height: 28px;
      }
    }

    /* Small mobile: max 380px */
    @media (max-width: 380px) {
      .hero-headline {
        font-size: 30px;
      }

      .problem-header h2,
      .pillars-header h2,
      .integrations-header h2,
      .social-proof-header h2,
      .closing-cta h2 {
        font-size: 28px;
      }

      .footer-links {
        grid-template-columns: 1fr;
      }
    }
"""

content = content.replace("  </style>", responsive_css + "\n  </style>")

open("index.html", "w").write(content)
print("✅ Responsive CSS added!")
