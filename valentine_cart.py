import streamlit as st
import base64
import random
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Valentine 💘", page_icon="💘", layout="centered")

# =========================
# CONFIG
# =========================
IMG_PATH = r"C:\Users\Admin\her.jpg" 
NAME = "Oluwatosin"

# =========================
# HELPERS
# =========================
def celebration_pop_photo(image_path: str, pops: int = 24):
    img_b64 = base64.b64encode(Path(image_path).read_bytes()).decode()

    html = f"""
    <div id="stage"></div>

    <style>
      #stage {{
        position: relative;
        width: 100%;
        height: 520px;
        border-radius: 18px;
        overflow: hidden;
        background: linear-gradient(180deg, rgba(91,0,20,0.25), rgba(91,0,20,0.75));
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 18px 40px rgba(0,0,0,0.25);
      }}

      .pop {{
        position: absolute;
        width: 150px;
        height: 190px;
        border-radius: 18px;
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.22);
        backdrop-filter: blur(7px);
        box-shadow: 0 18px 40px rgba(0,0,0,0.35);
        display: grid;
        place-items: center;
        transform: translate(-50%, -50%) scale(0.35);
        opacity: 0;
        animation: popIn 1.25s ease forwards;
      }}

      .pop img {{
        width: 138px;
        height: 172px;
        object-fit: cover;
        border-radius: 14px;
      }}

      @keyframes popIn {{
        0%   {{ transform: translate(-50%, -50%) scale(0.35); opacity: 0; }}
        30%  {{ transform: translate(-50%, -50%) scale(1.05); opacity: 1; }}
        60%  {{ transform: translate(-50%, -70%) scale(1.0); opacity: 1; }}
        100% {{ transform: translate(-50%, -98%) scale(0.95); opacity: 0; }}
      }}

      .confetti {{
        position: absolute;
        width: 10px;
        height: 10px;
        border-radius: 999px;
        opacity: 0.95;
        animation: fall 1.6s linear forwards;
      }}

      @keyframes fall {{
        0% {{ transform: translateY(-20px) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(620px) rotate(360deg); opacity: 0; }}
      }}
    </style>

    <script>
      const stage = document.getElementById("stage");

      function rand(min, max) {{
        return Math.floor(Math.random() * (max - min + 1)) + min;
      }}

      function spawnPhoto() {{
        const d = document.createElement("div");
        d.className = "pop";
        d.style.left = rand(12, 88) + "%";
        d.style.top = rand(58, 88) + "%";

        const img = document.createElement("img");
        img.src = "data:image/jpeg;base64,{img_b64}";
        d.appendChild(img);

        stage.appendChild(d);
        setTimeout(() => d.remove(), 1400);
      }}

      function spawnConfettiBurst() {{
        const colors = ["#ff2b6a", "#ff6b9c", "#ffd1e1", "#ffffff"];
        for (let i=0; i<30; i++) {{
          const c = document.createElement("div");
          c.className = "confetti";
          c.style.left = rand(0, 100) + "%";
          c.style.background = colors[rand(0, colors.length-1)];
          c.style.top = "-10px";
          c.style.width = rand(6, 12) + "px";
          c.style.height = rand(6, 12) + "px";
          stage.appendChild(c);
          setTimeout(() => c.remove(), 1700);
        }}
      }}

      let count = 0;
      const pops = {pops};
      const timer = setInterval(() => {{
        spawnPhoto();
        spawnConfettiBurst();
        count++;
        if (count >= pops) clearInterval(timer);
      }}, 420);
    </script>
    """
    components.html(html, height=560)

def celebration_pop_photos(image_paths, pops: int = 60):
    valid = [p for p in image_paths if Path(p).exists()]
    if not valid:
        raise FileNotFoundError("None of the image files exist.")

    imgs_b64 = [base64.b64encode(Path(p).read_bytes()).decode() for p in valid]

    html = f"""
    <div id="stage"></div>

    <style>
      #stage {{
        position: relative;
        width: 100%;
        height: 520px;
        border-radius: 18px;
        overflow: hidden;
        background: linear-gradient(180deg, rgba(91,0,20,0.25), rgba(91,0,20,0.75));
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 18px 40px rgba(0,0,0,0.25);
      }}

      .pop {{
        position: absolute;
        width: 150px;
        height: 190px;
        border-radius: 18px;
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.22);
        backdrop-filter: blur(7px);
        box-shadow: 0 18px 40px rgba(0,0,0,0.35);
        display: grid;
        place-items: center;
        transform: translate(-50%, -50%) scale(0.35);
        opacity: 0;
        animation: popIn 1.25s ease forwards;
      }}

      .pop img {{
        width: 138px;
        height: 172px;
        object-fit: cover;
        border-radius: 14px;
      }}

      @keyframes popIn {{
        0%   {{ transform: translate(-50%, -50%) scale(0.35); opacity: 0; }}
        30%  {{ transform: translate(-50%, -50%) scale(1.05); opacity: 1; }}
        60%  {{ transform: translate(-50%, -70%) scale(1.0); opacity: 1; }}
        100% {{ transform: translate(-50%, -98%) scale(0.95); opacity: 0; }}
      }}

      .confetti {{
        position: absolute;
        width: 10px;
        height: 10px;
        border-radius: 999px;
        opacity: 0.95;
        animation: fall 1.6s linear forwards;
      }}

      @keyframes fall {{
        0% {{ transform: translateY(-20px) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(620px) rotate(360deg); opacity: 0; }}
      }}
    </style>

    <script>
      const stage = document.getElementById("stage");
      const images = {imgs_b64};

      function rand(min, max) {{
        return Math.floor(Math.random() * (max - min + 1)) + min;
      }}

      function pickImage() {{
        return images[rand(0, images.length - 1)];
      }}

      function spawnPhoto() {{
        const d = document.createElement("div");
        d.className = "pop";
        d.style.left = rand(12, 88) + "%";
        d.style.top = rand(58, 88) + "%";

        const img = document.createElement("img");
        img.src = "data:image/*;base64," + pickImage();
        d.appendChild(img);

        stage.appendChild(d);
        setTimeout(() => d.remove(), 1400);
      }}

      function spawnConfettiBurst() {{
        const colors = ["#ff2b6a", "#ff6b9c", "#ffd1e1", "#ffffff"];
        for (let i=0; i<30; i++) {{
          const c = document.createElement("div");
          c.className = "confetti";
          c.style.left = rand(0, 100) + "%";
          c.style.background = colors[rand(0, colors.length-1)];
          c.style.top = "-10px";
          c.style.width = rand(6, 12) + "px";
          c.style.height = rand(6, 12) + "px";
          stage.appendChild(c);
          setTimeout(() => c.remove(), 1700);
        }}
      }}

      let count = 0;
      const pops = {pops};
      const timer = setInterval(() => {{
        spawnPhoto();
        spawnConfettiBurst();
        count++;
        if (count >= pops) clearInterval(timer);
      }}, 420);
    </script>
    """
    components.html(html, height=560)

def play_music_autostart():
    audio_bytes = Path("music.mp3").read_bytes()
    b64 = base64.b64encode(audio_bytes).decode()

    components.html(
        f"""
        <audio id="song" autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mpeg">
        </audio>

        <script>
            var audio = document.getElementById("song");
            audio.play().catch(function(e) {{
                console.log("Autoplay blocked:", e);
            }});
        </script>
        """,
        height=0
    )


def goto(step_name: str):
    st.session_state.step = step_name
    st.rerun()

# =========================
# STATE
# =========================
if "step" not in st.session_state:
    st.session_state.step = "start"

if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

if "no_pos" not in st.session_state:
    st.session_state.no_pos = random.randint(0, 2)  # column index 0..2

# =========================
# THEME / CSS
# =========================
hearts_svg = """
<svg xmlns='http://www.w3.org/2000/svg' width='260' height='260'>
  <rect width='100%' height='100%' fill='#5b0014'/>
  <g opacity='0.18'>
    <path d='M130 95 C130 70 160 70 160 95 C160 120 130 135 130 150 C130 135 100 120 100 95 C100 70 130 70 130 95 Z' fill='#ff2b6a'/>
    <path d='M60 170 C60 150 85 150 85 170 C85 190 60 202 60 214 C60 202 35 190 35 170 C35 150 60 150 60 170 Z' fill='#ff6b9c'/>
    <path d='M205 185 C205 165 230 165 230 185 C230 205 205 217 205 229 C205 217 180 205 180 185 C180 165 205 165 205 185 Z' fill='#ff6b9c'/>
  </g>
</svg>
"""
hearts_b64 = base64.b64encode(hearts_svg.encode()).decode()

st.markdown(
    f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500;700&family=Inter:wght@400;600;800&display=swap');

      .stApp {{
        background-color: #5b0014;
        background-image: url("data:image/svg+xml;base64,{hearts_b64}");
        background-repeat: repeat;
        background-size: 260px 260px;
      }}

      .block-container {{
        max-width: 820px;
        padding-top: 44px;
        padding-bottom: 80px;
      }}

      .glass {{
        background: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 20px;
        padding: 22px 22px;
        backdrop-filter: blur(10px);
      }}

      .title {{
        font-family: Inter, system-ui;
        font-weight: 800;
        font-size: 56px;
        color: #fff;
        margin: 0 0 10px 0;
        letter-spacing: -1px;
      }}

      .subtitle {{
        font-family: Inter, system-ui;
        color: rgba(255,255,255,0.86);
        font-size: 18px;
        margin: 0 0 18px 0;
      }}

      .letter {{
        background: rgba(255,255,255,0.92);
        border-radius: 22px;
        padding: 28px 26px;
        border: 3px solid rgba(255, 43, 106, 0.35);
        box-shadow: 0 18px 40px rgba(0,0,0,0.25);
      }}
      .letter h2 {{
        font-family: "Dancing Script", cursive;
        font-size: 44px;
        margin: 0 0 8px 0;
        color: #7a0020;
      }}
      .letter p {{
        font-family: "Dancing Script", cursive;
        font-size: 28px;
        line-height: 1.35;
        color: #2a0010;
        margin: 0 0 10px 0;
      }}

      .question {{
        font-family: "Dancing Script", cursive;
        font-size: 44px;
        color: #fff;
        margin: 10px 0 10px 0;
        text-align: center;
      }}

      .sticker {{
        font-family: Inter, system-ui;
        font-weight: 900;
        text-align: center;
        color: #fff;
        margin: 6px 0 14px 0;
        text-shadow: 0 14px 30px rgba(0,0,0,0.35);
        animation: pulse 0.9s ease-in-out infinite;
      }}
      @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.02); }}
        100% {{ transform: scale(1); }}
      }}

      .card {{
        background: rgba(255,255,255,0.90);
        border-radius: 18px;
        padding: 18px 16px;
        border: 2px solid rgba(255, 43, 106, 0.25);
        box-shadow: 0 16px 34px rgba(0,0,0,0.18);
        min-height: 150px;
      }}
      .card h3 {{
        font-family: Inter, system-ui;
        margin: 0 0 8px 0;
        color: #7a0020;
        font-size: 18px;
        font-weight: 900;
      }}
      .card p {{
        font-family: Inter, system-ui;
        margin: 0;
        color: #2a0010;
        font-size: 14px;
        line-height: 1.35;
      }}

      .footerNote {{
        font-family: Inter, system-ui;
        color: rgba(255,255,255,0.75);
        text-align: center;
        margin-top: 12px;
      }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# UI
# =========================
st.markdown("<div class='glass'>", unsafe_allow_html=True)

step = st.session_state.step

if step == "start":
    st.markdown("<div class='title'>💘 Valentine</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>A little surprise made just for you.</div>", unsafe_allow_html=True)

    if st.button("💖 Let’s begin"):
        goto("letter")

    st.markdown("<div class='footerNote'>Tap “Let’s begin” to open your letter ✨</div>", unsafe_allow_html=True)

elif step == "letter":
    st.markdown(
        f"""
        <div class="letter">
          <h2>My Love,</h2>
          <p>
            Before I ask you anything today, I just want you to know something from my heart.<br/><br/> 
            Loving you has been one of the most beautiful things that has happened to me. 
            You came into my life and brought calm where there was pressure, warmth where there was distance, 
            and light in moments I didn’t even realise were dim. 
            You are strength wrapped in softness. 
            You are intelligence with grace. You are beauty with depth. I admire the way you think. 
            I admire the way you care. I admire the woman you are becoming. Being with you feels intentional not accidental. 
            It feels like something God carefully wrote. No matter how busy life gets, no matter the miles between us, my heart feels settled with you.
            And that feeling is rare. Very rare. So before I go any further… Before I say what’s really on my mind today… 
            Just know that you are deeply valued, genuinely cherished, and sincerely loved. 
            I choose you. 💗 
            <p>Now… I have one important question for you 😌</p> </div>


        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Back"):
            goto("start")
    with col2:
        if st.button("✨ Next"):
            goto("meter")

elif step == "meter":
    st.markdown("<div class='question'><i>Love Meter 💗</i></div>", unsafe_allow_html=True)
    love = st.slider("How much do you love me today? 😄", 0, 100, 85)

    if love < 30:
        st.info("Hmm… we’ll warm it up 😌")
    elif love < 70:
        st.success("Okayyy… we’re getting there 💞")
    else:
        st.warning("🔥 Valentine energy detected!")

    if st.button("Next ➜ Memory cards"):
        goto("memories")

elif step == "memories":
    st.markdown("<div class='question'><i>3 little reasons…</i></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown(
            """
            <div class="card">
              <h3>🌸 What I adore</h3>
              <p>Your softness + strength. The way you carry yourself with grace.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            """
            <div class="card">
              <h3>✨ What I’m grateful for</h3>
              <p>Your love, your heart, everything… you make life better.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            """
            <div class="card">
              <h3>🏡 What I’m building</h3>
              <p>Peace, laughter, growth… and a future with you.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("💘 Now the real question…"):
        goto("question")

elif step == "question":
    n = st.session_state.no_clicks
    size = min(28 + n * 7, 86)

    st.markdown(
        f"<div class='question'><i>Will you be my Valentine, {NAME}?</i> 💘</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='sticker' style='font-size:{size}px;'>YES 💖</div>",
        unsafe_allow_html=True
    )

    cols = st.columns(3, gap="large")

    yes_col = 1
    no_col = st.session_state.no_pos

    with cols[yes_col]:
        if st.button("YES 💖"):
            goto("yes")

    with cols[no_col]:
        if st.button("No 🙈"):
            st.session_state.no_clicks += 1
            choices = [0, 1, 2]
            choices.remove(no_col)
            st.session_state.no_pos = random.choice(choices)
            st.rerun()

    st.markdown("<div class='footerNote'>Try pressing “No”… it won’t stay still 😄</div>", unsafe_allow_html=True)

elif step == "yes":
    st.markdown("<div class='question'><i>Yessss! 🎉💘</i></div>", unsafe_allow_html=True)

    play_music_autostart()

    try:
        image_list = [
            r"her1.jpg",
            r"her2.jpg",
            r"her3.jpg",
            r"her4.jpg",
            r"her5.jpg",
        ]

        celebration_pop_photos(image_list, pops=500)

    except Exception:
        st.warning("Photo not found. Put it at C:\\Users\\Admin\\her.jpg or update IMG_PATH")


    st.markdown(
        """
        <div class="letter">
          <h2>💖 Look who is my Val 💖</h2>
          <p>😍😍😍</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔁 Restart"):
            st.session_state.no_clicks = 0
            st.session_state.no_pos = random.randint(0, 2)
            goto("start")
    with col2:
        if st.button("📸 Pop again!"):
            goto("yes")

st.markdown("</div>", unsafe_allow_html=True)
