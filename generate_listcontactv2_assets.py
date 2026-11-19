import os
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = os.path.abspath(r"D:\L3MDW\Mobile\ListContactV2\screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def get_v2_main_html():
    contacts = [
        ("Dupont Claire", "06 12 34 56 78"),
        ("Martin Thomas", "07 23 45 67 89"),
        ("Bernard Sophie", "06 98 76 54 32"),
        ("Petit Lucas", "07 11 22 33 44"),
        ("Moreau Julien", "06 55 44 33 22")
    ]
    items_html = ""
    for name, tel in contacts:
        items_html += f"""
        <div style="background: white; padding: 14px 16px; border-bottom: 1px solid #E2E8F0; display: flex; align-items: center; justify-content: space-between;">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div style="width: 44px; height: 44px; border-radius: 22px; background: #E0E7FF; display: flex; align-items: center; justify-content: center; font-size: 20px;">👤</div>
                <div>
                    <div style="font-size: 15px; font-weight: bold; color: #1E293B;">{name}</div>
                    <div style="font-size: 13px; color: #64748B; margin-top: 2px;">{tel}</div>
                </div>
            </div>
            <div style="color: #94A3B8; font-size: 16px;">›</div>
        </div>
        """
    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
        body {{ background: transparent; display: flex; justify-content: center; align-items: center; padding: 20px; }}
        .phone-frame {{ width: 340px; height: 680px; background: #F8FAFC; border-radius: 36px; border: 9px solid #1E293B; box-shadow: 0 20px 40px rgba(0,0,0,0.25); display: flex; flex-direction: column; position: relative; overflow: hidden; }}
        .status-bar {{ height: 28px; background: #311B92; display: flex; justify-content: space-between; align-items: center; padding: 0 16px; color: white; font-size: 11px; font-weight: 600; }}
        .app-bar {{ height: 56px; background: #4A148C; color: white; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; font-size: 18px; font-weight: bold; }}
        .nav-bar {{ height: 22px; background: #F8FAFC; display: flex; justify-content: center; align-items: center; }}
        .home-indicator {{ width: 90px; height: 4px; background: #94A3B8; border-radius: 2px; }}
    </style>
    </head>
    <body>
        <div class="phone-frame">
            <div class="status-bar"><span>10:24</span><span>📶 🔋 100%</span></div>
            <div class="app-bar"><span>Mes contacts</span><span style="font-size: 24px;">+</span></div>
            <div style="flex: 1; overflow-y: auto;">{items_html}</div>
            <div class="nav-bar"><div class="home-indicator"></div></div>
        </div>
    </body>
    </html>
    """

def get_v2_detail_html(nom="Dupont", prenom="Claire", tel="06 12 34 56 78", email="claire.dupont@example.com"):
    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
        body {{ background: transparent; display: flex; justify-content: center; align-items: center; padding: 20px; }}
        .phone-frame {{ width: 340px; height: 680px; background: #F8FAFC; border-radius: 36px; border: 9px solid #1E293B; box-shadow: 0 20px 40px rgba(0,0,0,0.25); display: flex; flex-direction: column; position: relative; overflow: hidden; }}
        .status-bar {{ height: 28px; background: #311B92; display: flex; justify-content: space-between; align-items: center; padding: 0 16px; color: white; font-size: 11px; font-weight: 600; }}
        .app-bar {{ height: 56px; background: #4A148C; color: white; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; font-size: 18px; font-weight: bold; }}
        .content {{ flex: 1; padding: 18px; overflow-y: auto; display: flex; flex-direction: column; }}
        .avatar-box {{ width: 84px; height: 84px; border-radius: 42px; background: #E0E7FF; display: flex; align-items: center; justify-content: center; font-size: 40px; margin: 0 auto 16px auto; position: relative; border: 2px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.15); }}
        .cam-badge {{ position: absolute; bottom: 0; right: 0; background: #4A148C; color: white; border-radius: 12px; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; font-size: 13px; }}
        .field-label {{ font-size: 11px; font-weight: 600; color: #64748B; margin-bottom: 3px; }}
        .input-box {{ height: 38px; background: white; border: 1px solid #CBD5E1; border-radius: 6px; padding: 0 10px; font-size: 13px; display: flex; align-items: center; color: #1E293B; margin-bottom: 10px; }}
        .btn-action-icon {{ width: 38px; height: 38px; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; margin-left: 8px; font-size: 16px; }}
        .btn-half {{ flex: 1; height: 36px; border: 1.5px solid #4A148C; color: #4A148C; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; background: white; }}
        .btn-save {{ height: 42px; background: #00C853; color: white; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: bold; margin-top: 14px; box-shadow: 0 2px 4px rgba(0,200,83,0.3); }}
        .btn-cancel {{ height: 40px; border: 1.5px solid #94A3B8; color: #475569; border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600; margin-top: 8px; }}
        .nav-bar {{ height: 22px; background: #F8FAFC; display: flex; justify-content: center; align-items: center; }}
        .home-indicator {{ width: 90px; height: 4px; background: #94A3B8; border-radius: 2px; }}
    </style>
    </head>
    <body>
        <div class="phone-frame">
            <div class="status-bar"><span>10:25</span><span>📶 🔋 100%</span></div>
            <div class="app-bar">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span>←</span><span>Détail du contact</span>
                </div>
                <span>🗑</span>
            </div>
            <div class="content">
                <div class="avatar-box">
                    👤<div class="cam-badge">📷</div>
                </div>

                <div class="field-label">Nom</div>
                <div class="input-box">{nom}</div>

                <div class="field-label">Prénom</div>
                <div class="input-box">{prenom}</div>

                <div class="field-label">Téléphone</div>
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div class="input-box" style="flex: 1; margin-bottom: 0;">{tel}</div>
                    <div class="btn-action-icon" style="background: #00C853;">📞</div>
                </div>

                <div class="field-label">E-mail</div>
                <div style="display: flex; align-items: center; margin-bottom: 12px;">
                    <div class="input-box" style="flex: 1; margin-bottom: 0;">{email}</div>
                    <div class="btn-action-icon" style="background: #0288D1;">✉️</div>
                </div>

                <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                    <div class="btn-half">📁 Choisir photo</div>
                    <div class="btn-half">📷 Prendre photo</div>
                </div>

                <div class="btn-save">Enregistrer</div>
                <div class="btn-cancel">Annuler</div>
            </div>
            <div class="nav-bar"><div class="home-indicator"></div></div>
        </div>
    </body>
    </html>
    """

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 420, "height": 760})

        # 1. Main list
        page.set_content(get_v2_main_html())
        p1 = os.path.join(SCREENSHOTS_DIR, "v2_01_main_list.png")
        page.locator(".phone-frame").screenshot(path=p1)
        print(f"Generated: {p1}")

        # 2. Detail screen
        page.set_content(get_v2_detail_html())
        p2 = os.path.join(SCREENSHOTS_DIR, "v2_02_detail_view.png")
        page.locator(".phone-frame").screenshot(path=p2)
        print(f"Generated: {p2}")

        # 3. Modified detail
        page.set_content(get_v2_detail_html(nom="Dupont", prenom="Claire-Marie", tel="06 99 88 77 66", email="claire.m@example.com"))
        p3 = os.path.join(SCREENSHOTS_DIR, "v2_03_modification.png")
        page.locator(".phone-frame").screenshot(path=p3)
        print(f"Generated: {p3}")

        browser.close()

if __name__ == "__main__":
    run()
