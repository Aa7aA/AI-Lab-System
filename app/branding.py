from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"

LAB_BRANDING = {
    "logo_path": ASSETS_DIR / "lab_logo.png",
    "footer_qr_path": ASSETS_DIR / "footer_qr.png",

    "lab_name_ar": "نظام المختبر الذكي",
    "lab_name_en": "AI Lab System",

    "pdf_header_en_line1": "AI LAB",
    "pdf_header_en_line2": "Smart Medical System",

    "pdf_header_ar_line1": "نظام",
    "pdf_header_ar_line2": "المختبر الذكي",
    "pdf_header_ar_line3": "للتحليلات الطبية الذكية",
}