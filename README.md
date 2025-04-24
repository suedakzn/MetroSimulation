# 🚇 Sürücüsüz Metro Simülasyonu – A* ve BFS Algoritmalarıyla

## 📌 Proje Açıklaması  
Bu proje, Python dili kullanılarak geliştirilen bir sürücüsüz metro simülasyonudur. Amaç; bir metro ağı içerisinde, kullanıcı tarafından belirlenen iki istasyon arasında:

- ✅ **En az aktarma** ile ulaşım sağlayan rotayı bulmak (BFS ile),
- ✅ **En kısa sürede** hedefe ulaştıran rotayı bulmak (A* algoritması ile).

Proje, ulaşım sistemlerinde optimizasyon problemlerini çözme üzerine algoritmaların nasıl uygulanabileceğini göstermektedir.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

| Teknoloji | Açıklama |
|----------|----------|
| **Python 3** | Projenin geliştirme dili |
| `collections.deque` | BFS algoritması için verimli kuyruk yapısı |
| `heapq` | A* algoritmasında öncelikli kuyruk (min-heap) kullanımı |
| `typing` | Tip açıklamaları ile okunabilirlik ve hata azaltımı |

---

## 📚 Algoritmaların Açıklaması

### 🔁 BFS (Breadth-First Search)
- Başlangıç noktasından hedef istasyona **en az aktarma** ile ulaşmayı amaçlar.
- Katman katman ilerleyen yapısı sayesinde garantili çözüm sunar.
- FIFO mantığıyla çalışan `deque` veri yapısı ile uygulanır.

### ⭐ A* (A-Star) Algoritması
- Başlangıç ve hedef istasyon arasında **en kısa sürede** varış yolunu bulur.
- Her adımda:
toplam_maliyet = g (geçilen süre) + h (tahmini kalan süre)

- Bu projede basit bir heuristic olarak istasyon ID’lerinin sayısal farkı kullanılmıştır.

---

## 🎯 Neden Bu Algoritmalar Seçildi?

- **BFS** → Ağırlıksız graf yapılarında garantili en kısa aktarma sayısını verdiği için,
- **A\*** → Süre bazlı hesaplamalarda daha verimli ve optimal çözüm sunduğu için.

---


🧪 Test Senaryoları
Projeyi çalıştırdığınızda şu örnek senaryolar otomatik test edilir:

AŞTİ → OSB

Batıkent → Keçiören

Keçiören → AŞTİ

Örnek çıktı:

![Ekran görüntüsü 2025-04-24 155830](https://github.com/user-attachments/assets/aaa81280-1a7e-45f5-8302-fd222bdd9b3e)

💡 Geliştirme Fikirleri
Gerçek koordinatlarla daha doğru heuristic() hesaplamaları,

Harita üzerinde görsel metro ağı çizimi ve animasyonlu rota izleme,

Kullanıcı arayüzü (GUI) ile daha etkileşimli deneyim,

Gerçek şehir verileriyle entegre edilebilir bir navigasyon aracı.

👩‍💻 Geliştirici
Sueda Kazan
GitHub: github.com/suedakzn

Bu proje, algoritmaların gerçek dünya problemlerine nasıl uygulanabileceğini gösteren yalın ama etkili bir simülasyondur.
Keyifli incelemeler ve katkılar dilerim! 🚇💻✨

