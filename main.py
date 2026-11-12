import time
import sys

# Genişletilmiş Veri Tabanı
ATIK_VERITABANI = {
    # Plastikler
    "plastik şişe": {
        "kutu": "🟡 SARI KUTU (Plastik Atık)",
        "sure": "450 yıl",
        "fikir": "Alt kısmını kesip boyayarak şık bir kalemlik veya saksı yapabilirsin."
    },
    "naylon poşet": {
        "kutu": "🟡 SARI KUTU (Plastik Atık)",
        "sure": "1000 yıl",
        "fikir": "Eski poşetleri örgü yöntemiyle paspas veya çanta yapımında ip olarak kullanabilirsin."
    },
    "yoğurt kabı": {
        "kutu": "🟡 SARI KUTU (Plastik Atık)",
        "sure": "400 - 500 yıl",
        "fikir": "Üzerini kumaş veya ip ile kaplayarak mutfakta bakliyat saklama kabı yapabilirsin."
    },
    "plastik çatal": {
        "kutu": "🟡 SARI KUTU (Plastik Atık)",
        "sure": "450 yıl",
        "fikir": "Etin etrafına dizerek modern bir avize gövdesi veya ayna çerçevesi tasarlayabilirsin."
    },
    "köpük tabak": {
        "kutu": "🟡 SARI KUTU (Geri dönüştürülebilir, temizse)",
        "sure": "500+ yıl (Asla çözünmez)",
        "fikir": "Çocuklar için minyatür boyama paleti veya maket malzemesi olarak kullanabilirsin."
    },

    # Camlar
    "cam şişe": {
        "kutu": "🟢 YEŞİL KUTU (Cam Atık)",
        "sure": "4000 yıl (Neredeyse hiç yok olmaz!)",
        "fikir": "İçine led ışıklar koyarak dekoratif bir gece lambasına dönüştürebilirsin."
    },
    "cam kavanoz": {
        "kutu": "🟢 YEŞİL KUTU (Cam Atık)",
        "sure": "4000 yıl",
        "fikir": "Kapağını boyayıp baharatlık yapabilir veya içine mum koyarak şık bir şamdan elde edebilirsin."
    },

    # Kağıt & Karton
    "kağıt": {
        "kutu": "🔵 MAVİ KUTU (Kağıt/Karton Atık)",
        "sure": "2 - 6 hafta",
        "fikir": "Eski gazetelerden veya kağıtlardan origami yaparak kitap ayracı oluşturabilirsin."
    },
    "karton": {
        "kutu": "🔵 MAVİ KUTU (Kağıt/Karton Atık)",
        "sure": "2 ay",
        "fikir": "Kargodan gelen karton kutuları kesip birleştirerek çekmece içi düzenleyici yapabilirsin."
    },
    "karton bardak": {
        "kutu": "⚫ SİYAH KUTU (Evsel Atık - İçinde plastik kaplama var!)",
        "sure": "30 yıl",
        "fikir": "İçine toprak koyup tohum çimlendirme saksısı olarak kullanabilirsin."
    },
    "yumurta kolisi": {
        "kutu": "🔵 MAVİ KUTU veya 🟤 KOMPOST",
        "sure": "4 - 6 hafta",
        "fikir": "Çekmece içinde çorap düzenleyici olarak kullanabilir ya da tohum çimlendirebilirsin."
    },

    # Piller ve Elektronik
    "pil": {
        "kutu": "🔴 KIRMIZI KUTU (Atık Pil Kutusu - Sakın normal çöpe atma!)",
        "sure": "300 yıl (Toprağı ve suyu zehirler)",
        "fikir": "TAP (Taşınabilir Pil Üreticileri) kutularına atarak doğayı koruyabilirsin."
    },
    "eski telefon": {
        "kutu": "🔌 ELEKTRONİK ATIK (Belediye Atık Noktası / E-Atık Kutusu)",
        "sure": "1 milyon yıl+ (Ağır metaller içerir)",
        "fikir": "Tamir ettirip ihtiyaç sahibine verebilir ya da yetkili e-atık toplama merkezine verebilirsin."
    },
    "şarj kablosu": {
        "kutu": "🔌 ELEKTRONİK ATIK",
        "sure": "Yüzlerce yıl",
        "fikir": "Kırık kısımlarını kesip içindeki bakır telleri el sanatları projelerinde kullanabilirsin."
    },

    # Organik & Gıda
    "muz kabuğu": {
        "kutu": "🟤 KAHVERENGİ KUTU (Organik Atık / Kompost)",
        "sure": "2 - 5 hafta",
        "fikir": "Su dolu bir kavanozda 2 gün bekletip o suyu çiçeklerine doğal gübre olarak verebilirsin."
    },
    "yumurta kabuğu": {
        "kutu": "🟤 KAHVERENGİ KUTU (Organik Atık / Kompost)",
        "sure": "İ birkaç ay",
        "fikir": "İyice kurutup toz haline getirerek bitkilerin toprağına kalsiyum takviyesi olarak ekleyebilirsin."
    },
    "kahve telvesi": {
        "kutu": "🟤 KAHVERENGİ KUTU (Organik Atık / Kompost)",
        "sure": "Birkaç gün",
        "fikir": "Kurutup dolap kokusu giderici olarak kullanabilir ya da peeling maskesi yapabilirsin."
    },
    "ekmek": {
        "kutu": "🟤 KAHVERENGİ KUTU / Bayat ekmek kutusu",
        "sure": "1 - 2 hafta",
        "fikir": "Küp doğrayıp fırınlayarak çorbalar için kruton ekmek yapabilirsin."
    },

    # Metaller
    "alüminyum kutu": {
        "kutu": "⚪ GRİ KUTU (Metal Atık)",
        "sure": "200 - 500 yıl",
        "fikir": "Üstünü açıp içine toprak doldurarak mini kaktüs saksısı yapabilirsin."
    },
    "konserve kutusu": {
        "kutu": "⚪ GRİ KUTU (Metal Atık)",
        "sure": "50 - 100 yıl",
        "fikir": "Dışını ip veya kumaşla sararak masada kalemlik veya kaşıkçılık yapabilirsin."
    },

    # Tekstil ve Diğerleri
    "eski tişört": {
        "kutu": "👕 TEKSTİL KUMBARASI (Kullanılabilirse bağış)",
        "sure": "2 - 10 yıl (Kumaşına göre değişir)",
        "fikir": "Kolları ve gövdeyi kesip örerek ev için paspas (paspas ipi) yapabilirsin."
    },
    "sakız": {
        "kutu": "⚫ SİYAH KUTU (Evsel Atık - Geri dönüştürülemez)",
        "sure": "5 yıl (Sentetik kauçuk içerir)",
        "fikir": "Kuşların yem sanıp boğulmaması için mutlaka bir kağıda sarıp çöpe atmalısın."
    },
    "sigara izmariti": {
        "kutu": "⚫ SİYAH KUTU (Evsel Atık)",
        "sure": "10 - 12 yıl (Filtresi plastiktir)",
        "fikir": "İzmaritleri doğaya atmak yerine cep küllüğü kullanabilirsin."
    },
    "diş fırçası": {
        "kutu": "⚫ SİYAH KUTU (Plastik ve kıl karışımı - Geri dönüştürülemez)",
        "sure": "500 yıl",
        "fikir": "Eski diş fırçasını temizlik fırçası yaparak (klavyeler, dar köşeler) yeniden kullanabilirsin."
    }
}

def yavas_yaz(metin, hiz=0.015):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def botu_baslat():
    print("\n" + "="*55)
    print("🌱  EKO-ASİSTAN TERMINAL BOTUNA HOŞ GELDİN!  🌱")
    print("="*55)
    yavas_yaz(f"Şu an veri tabanımda tam {len(ATIK_VERITABANI)} farklı eşya kayıtlı!")
    yavas_yaz("Atığın adını yaz, nereye atılacağını ve ileri dönüşüm fikrini söyleyeyim.")
    print("-" * 55)
    print("💡 İpucu: Kayıtlı tüm eşyaları görmek için 'liste', çıkmak için 'çıkış' yaz.")
    print("-" * 55)

    while True:
        kullanici_girdisi = input("\n🗣️  Sen: ").strip().lower()

        if kullanici_girdisi in ["çıkış", "cikis", "exit", "q"]:
            yavas_yaz("\n🤖 Eko-Bot: Doğayı koruduğun için teşekkürler! Görüşmek üzere 👋\n")
            break

        elif kullanici_girdisi == "liste":
            print("\n📋 Veri Tabanındaki Tüm Eşyalar:")
            for i, esya in enumerate(ATIK_VERITABANI.keys(), 1):
                print(f"   {i}. {esya.capitalize()}")
            continue

        bulunan_esya = None
        for esya in ATIK_VERITABANI.keys():
            if esya in kullanici_girdisi:
                bulunan_esya = esya
                break

        if bulunan_esya:
            bilgi = ATIK_VERITABANI[bulunan_esya]
            print("\n🤖 Eko-Bot analiz ediyor...")
            time.sleep(0.3)
            print(f"   🗑️  Nereye Atılmalı : {bilgi['kutu']}")
            print(f"   ⏳ Doğada Yok Olma : {bilgi['sure']}")
            print(f"   🎨 İleri Dönüşüm   : {bilgi['fikir']}")
        else:
            yavas_yaz("\n🤖 Eko-Bot: Bu eşya henüz veri tabanımda yok knk 😅")
            yavas_yaz("   'liste' yazarak mevcut eşyalara göz atabilirsin.")

if __name__ == "__main__":
    botu_baslat()
