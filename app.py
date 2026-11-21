from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'kunci_rahasia_bouquet_cantik'  # Diperlukan untuk notifikasi pesan

# Data Company Profile & Katalog
COMPANY_INFO = {
    "name": "Bloom & Bite Craft",
    "tagline": "Merangkai Momen Spesial Lewat Bunga, Snack & Karya Kreatif",
    "about": (
        "Bloom & Bite Craft adalah studio kreatif yang berdedikasi menciptakan berbagai jenis "
        "bouquet custom untuk segala momen berharga Anda. Mulai dari bunga segar, rangkaian snack "
        "favorit, hingga bouquet uang dan boneka yang dirangkai secara handmade dengan penuh ketelitian."
    ),
    "whatsapp": "6289602883653",  # Ganti dengan nomor WhatsApp Anda (awali dengan 62)
    "instagram": "@bloomandbite.id",
    "address": "Jl. Melati Indah No. 45, Tangerang, Banten"
}

CATALOG = [
    {
        "id": 1,
        "category": "Bunga Segar & Artificial",
        "title": "Eternal Rose Bouquet",
        "price": "Rp 185.000",
        "description": "Rangkaian mawar merah & baby breath dengan wrapping kertas cellophane premium.",
        "image": "https://images.unsplash.com/photo-1561181286-d3fee7d55364?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2,
        "category": "Bouquet Makanan",
        "title": "Sweet Choco & Snack Tower",
        "price": "Rp 120.000",
        "description": "Kombinasi cokelat SilverQueen, Pocky, dan wafer favorit yang cocok untuk hadiah ulang tahun.",
        "image": "https://images.unsplash.com/photo-1549465220-1a8b9238cd48?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 3,
        "category": "Bouquet Custom Lainnya",
        "title": "Graduation Bear & Money Bouquet",
        "price": "Rp 150.000",
        "description": "Jasa rangkai uang (nominal bebas) lengkap dengan boneka wisuda dan kartu ucapan gratis.",
        "image": "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=600&q=80"
    }
]

SERVICES = [
    {"icon": "💐", "title": "Flower Bouquet", "desc": "Bunga segar lokal & impor, bunga kering (dried flower), serta artificial."},
    {"icon": "🍫", "title": "Snack & Food Bouquet", "desc": "Rangkaian cokelat, makanan ringan, hingga bouquet kopi atau buah."},
    {"icon": "💸", "title": "Money & Gift Bouquet", "desc": "Bouquet lembaran uang, boneka wisuda, skincare, hingga polaroid."}
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nama = request.form.get("nama")
        jenis = request.form.get("jenis")
        catatan = request.form.get("catatan")
        
        # Di sini Anda bisa menambahkan logic simpan ke database atau kirim email
        flash(f"Terima kasih {nama}! Permintaan konsultasi untuk {jenis} telah kami terima.", "success")
        return redirect(url_for("home") + "#kontak")

    return render_template(
        "index.html",
        company=COMPANY_INFO,
        catalog=CATALOG,
        services=SERVICES
    )

if __name__ == "__main__":
    app.run(debug=True)