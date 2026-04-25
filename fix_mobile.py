content = open("index.html", "r").read()

# Fix the hamburger JS - replace old one with clean version
old_js = """  <script>
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
  </script>"""

new_js = """  <script>
    let lastScroll = 0;
    const nav = document.querySelector("nav");
    window.addEventListener("scroll", () => {
      const current = window.scrollY;
      if (current <= 0) {
        nav.style.transform = "translateY(0)";
      } else if (current > lastScroll) {
        nav.style.transform = "translateY(-100%)";
      } else {
        nav.style.transform = "translateY(0)";
      }
      lastScroll = current;
    });

    const hamburger = document.getElementById("hamburger");
    const mobileMenu = document.getElementById("mobileMenu");

    if (hamburger && mobileMenu) {
      hamburger.addEventListener("click", function() {
        hamburger.classList.toggle("open");
        mobileMenu.classList.toggle("open");
        document.body.style.overflow = mobileMenu.classList.contains("open") ? "hidden" : "";
      });

      mobileMenu.querySelectorAll("a").forEach(function(link) {
        link.addEventListener("click", function() {
          hamburger.classList.remove("open");
          mobileMenu.classList.remove("open");
          document.body.style.overflow = "";
        });
      });
    }
  </script>"""

# Remove old scroll script
old_scroll = """  <script>
    let lastScroll = 0;
    const nav = document.querySelector(\"nav\");
    window.addEventListener(\"scroll\", () => {
      const current = window.scrollY;
      if (current <= 0) {
        nav.style.transform = \"translateY(0)\";
      } else if (current > lastScroll) {
        nav.style.transform = \"translateY(-100%)\";
      } else {
        nav.style.transform = \"translateY(0)\";
      }
      lastScroll = current;
    });
  </script>"""

content = content.replace(old_scroll, "")
content = content.replace(old_js, new_js)

open("index.html", "w").write(content)
print("✅ Mobile JS fixed!")
