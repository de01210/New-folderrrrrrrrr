# ...existing code...
"""
make_goodboy_qr.py

Generates a QR code (qr_goodboy.png) that encodes a small data: HTML page.
When scanned, the phone shows an animated "goodboy" message (CSS animation).

Safe and local: nothing is sent anywhere. Use only with consent.
"""
import qrcode
import urllib.parse
import os
from typing import Final

HTML: Final[str] = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>goodboy</title>
<style>
  :root{--bg:#0f1724;--text:#ffdd57;--shadow:#ffc857}
  html,body{height:100%;margin:0}
  body{
    display:flex;
    align-items:center;
    justify-content:center;
    background: radial-gradient(circle at 10% 10%, #102030 0%, var(--bg) 60%);
    font-family: system-ui,-apple-system,Segoe UI,Roboto,"Helvetica Neue",Arial;
    color:var(--text);
  }
  .card{
    text-align:center;
    padding:28px;
    border-radius:18px;
    backdrop-filter: blur(6px);
    box-shadow: 0 10px 30px rgba(2,8,23,0.6), 0 2px 6px rgba(0,0,0,0.5);
    background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
  }
  .dog{
    font-size: 4.2rem;
    transform-origin:center;
    display:inline-block;
    filter: drop-shadow(0 6px 14px rgba(0,0,0,0.5));
    animation: bounce 2.2s infinite ease-in-out;
  }
  h1{
    margin:12px 0 0;
    font-size: 3rem;
    letter-spacing:0.06em;
    text-shadow: 0 6px 18px rgba(0,0,0,0.6), 0 0 8px rgba(255,200,80,0.08);
    animation: glow 2.4s infinite;
  }
  p.small{margin:8px 0 0;color:rgba(255,255,255,0.66);font-size:0.95rem}
  @keyframes bounce{
    0%{ transform: translateY(0) rotate(-3deg) }
    25%{ transform: translateY(-10px) rotate(2deg) }
    50%{ transform: translateY(0) rotate(-1deg) }
    75%{ transform: translateY(-6px) rotate(2deg) }
    100%{ transform: translateY(0) rotate(-3deg) }
  }
  @keyframes glow{
    0%{ text-shadow: 0 6px 18px rgba(0,0,0,0.6), 0 0 6px rgba(255,200,80,0.06) }
    50%{ text-shadow: 0 10px 30px rgba(0,0,0,0.7), 0 0 18px rgba(255,210,90,0.2) }
    100%{ text-shadow: 0 6px 18px rgba(0,0,0,0.6), 0 0 6px rgba(255,200,80,0.06) }
  }

  /* responsive size tweaks */
  @media (max-width:420px){
    .dog{font-size:3.2rem}
    h1{font-size:2.2rem}
  }
</style>
</head>
<body>
  <div class="card">
    <div class="dog" aria-hidden="true">🐶</div>
    <h1>goodboy</h1>
    <p class="small">You're a good human — have a nice day!</p>
  </div>
</body>
</html>
"""
# ...existing code...