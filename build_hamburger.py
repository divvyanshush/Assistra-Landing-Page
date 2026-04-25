content = open("index.html", "r").read()

hamburger_css = """
    /* ───── HAMBURGER MENU ───── */
    .hamburger {
      display: none;
      flex-direction: column;
      gap: 5px;
      cursor: pointer;
      padding: 4px;
      background: none;
      border: none;
      z-index: 1001;
    }

    .hamburger span {
      display: block;
      width: 24px;
      height: 2px;
      background: #141413;
      border-radius: 2px;
      transition: all 0.3s ease;
    }

    .hamburger.open span:nth-child(1) {
      transform: translateY(7px) rotate(45deg);
    }

    .hamburger.open span:nth-child(2) {
      opacity: 0;
    }

    .hamburger.open span:nth-child(3) {
      transform: translateY(-7px) rotate(-45deg);
    }

    .mobile-menu {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: #F0FFF9;
      z-index: 999;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 32px;
    }

    .mobile-menu.open {
      display: flex;
    }

    .mobile-menu a {
      font-family: 'Geist', sans-serif;
      font-size: 24px;
      font-weight: 400;
      color: #141413;
      text-decoration: none;
      transition: color 0.2s;
    }

    .mobile-menu a:hover {
      color: #007683;
    }

    .mobile-menu .mobile-cta {
      margin-top: 16px;
    }

    @media (max-width: 767px) {
      .hamburger {
        display: flex;
      }

      .nav-links {
        display: none;
      }

      .nav-cta {
        display: none;
      }
    }
"""

hamburger_html = """
      <button class="hamburger" id="hamburger" aria-label="Menu">
        <span></span>
        <span></span>
        <span></span>
      </button>

      <!-- Mobile Menu -->
      <div class="mobile-menu" id="mobileMenu">
        <a href="#">Product</a>
        <a href="#">Solutions</a>
        <a href="#">Resources</a>
        <a href="#">Pricing</a>
        <a href="#" class="btn-filled mobile-cta">Try For Free <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8H13M13 8L9 4M13 8L9 12" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      </div>
"""

hamburger_js = """
  <script>
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobileMenu');

    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      mobileMenu.classList.toggle('open');
      document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('open');
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  </script>
"""

# Add class to CTA button in nav
content = content.replace(
    '<a href="#" class="btn-filled">Try For Free',
    '<a href="#" class="btn-filled nav-cta">Try For Free'
)

# Inject hamburger CSS
content = content.replace("  </style>", hamburger_css + "\n  </style>")

# Inject hamburger button + mobile menu before </nav>
content = content.replace("  </nav>", hamburger_html + "\n  </nav>")

# Inject JS before closing </body>
content = content.replace("</body>", hamburger_js + "\n</body>")

open("index.html", "w").write(content)
print("✅ Hamburger menu added!")
