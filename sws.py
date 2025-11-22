# ...existing code...
"""
Educational QR generator (safe)

- Generates a plain QR for any text/URL.
- Generates a "consent-protected" QR that encodes a data: URL containing
  a small HTML warning/consent page. When scanned, the phone will show
  the warning and require the user to click a link to continue.

IMPORTANT: Use only for learning and with consent. Do NOT use to trick or invade privacy.
"""

import qrcode
import urllib.parse
import html
import os

def make_plain_qr(text, filename='qr_plain.png', box_size=10, border=4):
    qr = qrcode.QRCode(box_size=box_size, border=border, error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"[+] Plain QR saved to {filename}")

def make_consent_qr(target_url, filename='qr_consent.png', site_name='Target', box_size=10, border=4):
    """
    Creates a QR that encodes a data:text/html URI. The HTML shows a clear warning
    and a link the user can click to proceed to the real target_url.
    This forces an explicit consent step for anyone who scans it.
    """
    # Safely escape values for inclusion in HTML
    escaped_site = html.escape(site_name)
    escaped_target_display = html.escape(target_url)
    escaped_target_href = html.escape(target_url, quote=True)

    # Basic, short HTML for the warning/consent page
    html_content = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width,initial-scale=1"/>
        <title>Warning — {escaped_site}</title>
        <style>body{{font-family:system-ui,Arial;margin:20px;color:#111}} .warn{{background:#fff4e5;border-left:4px solid #ffae42;padding:12px;border-radius:6px}} a.button{{display:inline-block;margin-top:12px;padding:10px 14px;border-radius:6px;text-decoration:none;border:1px solid #333}}</style>
      </head>
      <body>
        <h1>Warning: Confirm before continuing</h1>
        <div class="warn">
          <p>This link was encoded into a QR code. For your safety, always check links before opening them.</p>
          <p><strong>Target:</strong> {escaped_target_display}</p>
          <p>If you trust this source, click <a class="button" href="{escaped_target_href}">Proceed to the site</a>. Otherwise do not continue.</p>
        </div>
        <small>Educational demo — does not collect data.</small>
      </body>
    </html>
    """

    # Encode as data URI (URL-encode the HTML content)
    data_uri = "data:text/html;charset=utf-8," + urllib.parse.quote(html_content, safe='')

    qr = qrcode.QRCode(box_size=box_size, border=border, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data_uri)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"[+] Consent-protected QR saved to {filename}")
    print("    When scanned, it shows a warning page and requires the user to click 'Proceed' to visit the target URL.")

def main():
    # Example usage:
    os.makedirs('output_qr', exist_ok=True)
    # 1) Plain QR
    plain_text = input("Enter text or URL for a plain QR (e.g. https://example.com): ").strip()
    if plain_text:
        make_plain_qr(plain_text, filename=os.path.join('output_qr','qr_plain.png'))
    else:
        print("[-] Skipped plain QR (no text entered).")

    # 2) Consent-protected QR
    target = input("Enter the target URL for a consent-protected QR (e.g. https://example.com). Leave empty to skip: ").strip()
    if target:
        make_consent_qr(target, filename=os.path.join('output_qr','qr_consent.png'), site_name='Demo Site')
    else:
        print("[-] Skipped consent QR (no target entered).")

    print("\nFiles saved in ./output_qr. Scan them with a phone QR reader to see the behavior (use your own device).")

if __name__ == '__main__':
    main()
# ...existing code...