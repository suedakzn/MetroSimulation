from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        # İstasyon sınıfı; her istasyonun ID'si, adı, hattı ve komşuları vardır.
        self.idx = idx  # İstasyonun benzersiz kimliği
        self.ad = ad  # İstasyonun adı (görüntülenecek)
        self.hat = hat  # İstasyonun ait olduğu metro hattı
        self.komsular: List[Tuple['Istasyon', int]] = []  # (komşu istasyon, süre) tuple listesi

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        # Bir komşu istasyonu ve ona ulaşım süresini ekler
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        # Metro ağı sınıfı; tüm istasyonları ve hatları tutar
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        # Yeni bir istasyon ekler (ID eşsiz olmalı)
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        # İki istasyon arasında çift yönlü bağlantı oluşturur
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    # === EN AZ AKTARMALI ROTA (BFS) ===
    # Bu fonksiyon, iki istasyon arasındaki en az aktarmalı güzergahı bulmak için Breadth-First Search (BFS) algoritmasını kullanır.
    # BFS, tüm yolları eşit sürede arar ve ilk bulunan geçerli çözüm, minimum aktarma garantisi verir.

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        # Breadth-First Search (BFS) algoritması ile en az aktarma içeren rotayı bulur
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None  # Geçersiz ID'ler

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # Kuyruk yapısı: (şu anki istasyon, rota listesi, aktarma sayısı, önceki hat)
        kuyruk = deque([(baslangic, [baslangic], 0, baslangic.hat)])
        ziyaret_edilen = dict()  # Aynı istasyona aynı hatta daha önce gidildiyse tekrar gitmemek için

        while kuyruk:
            mevcut, yol, aktarma, onceki_hat = kuyruk.popleft()

            if mevcut.idx == hedef.idx:
                return yol  # Hedefe ulaşıldıysa yol döndürülür

            for komsu, _ in mevcut.komsular:
                yeni_hat = komsu.hat
                yeni_aktarma = aktarma + (1 if yeni_hat != onceki_hat else 0)
                ziyaret_kaydi = (komsu.idx, yeni_hat)

                # Daha az aktarmayla gidilmişse tekrar işleme gerek yok
                if ziyaret_kaydi in ziyaret_edilen and ziyaret_edilen[ziyaret_kaydi] <= yeni_aktarma:
                    continue

                ziyaret_edilen[ziyaret_kaydi] = yeni_aktarma
                kuyruk.append((komsu, yol + [komsu], yeni_aktarma, yeni_hat))

        return None  # Ulaşım mümkün değilse
    
    # === HEURISTIC FONKSIYON ===
    # A* algoritmasında kullanılan tahmini kalan mesafeyi hesaplayan fonksiyon.
    # Burada istasyon ID’lerinin sayı kısmı kullanılarak yaklaşık fark hesaplanır.
    # Gerçek dünyada bu değer, iki istasyonun koordinatlarına göre daha doğru hesaplanabilir.

    def heuristic(self, istasyon1: Istasyon, istasyon2: Istasyon) -> int:
        # Basit bir tahmin fonksiyonu: ID'ler üzerinden mesafe
        return abs(int(istasyon1.idx[1:]) - int(istasyon2.idx[1:]))
    
    # === EN HIZLI ROTA (A* ALGORİTMASI) ===
    # Bu fonksiyon, başlangıç ve hedef istasyon arasındaki en kısa süreli rotayı bulmak için A* algoritmasını kullanır.
    # A* algoritması, her adımda toplam maliyeti (geçilen yol + hedefe kalan tahmini yol) hesaba katar.
    # Bu sayede klasik Dijkstra algoritmasından daha verimli çalışır.
    # 'heuristic()' fonksiyonu hedefe olan tahmini mesafeyi verir ve bu tahmin A*'ın öncelik sırasını belirler.

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # heap yapısına sıralanabilir 'komsu.idx' eklendi
        heap = [(self.heuristic(baslangic, hedef), 0, baslangic.idx, baslangic, [baslangic])]
        en_kisa_sure = {baslangic.idx: 0}

        while heap:
            _, toplam_sure, _, mevcut, yol = heapq.heappop(heap)

            if mevcut.idx == hedef.idx:
                return (yol, toplam_sure)

            for komsu, sure in mevcut.komsular:
                yeni_toplam_sure = toplam_sure + sure

                if komsu.idx not in en_kisa_sure or yeni_toplam_sure < en_kisa_sure[komsu.idx]:
                    en_kisa_sure[komsu.idx] = yeni_toplam_sure
                    tahmini_maliyet = yeni_toplam_sure + self.heuristic(komsu, hedef)
                    heapq.heappush(heap, (tahmini_maliyet, yeni_toplam_sure, komsu.idx, komsu, yol + [komsu]))

        return None


if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar tanımlanıyor
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # İstasyonlar arası bağlantılar tanımlanıyor
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)

    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)

    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)

    # Hatlar arası aktarma bağlantıları
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 
