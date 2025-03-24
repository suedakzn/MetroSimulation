### A* ve BFS Algoritmalarını Kullanarak Sürücüsüz Metro Simulasyonu
## 1. Proje Açıklaması
Bu proje, iki farklı arama algoritmasını kullanarak bir harita üzerinde en kısa yolu bulmayı amaçlar. BFS (Breadth-First Search) ve A (A-Star) Algoritmaları* kullanılarak bir başlangıç noktasından hedef noktaya ulaşmanın en iyi yolu hesaplanır.

## 2. Kullanılan Teknolojiler ve Kütüphaneler
Bu projede aşağıdaki teknolojiler ve kütüphaneler kullanılmıştır:

- Python: Proje dili
- heapq: A* algoritmasında öncelikli kuyruk (priority queue) yapısı için kullanıldı.
- collections.deque: BFS algoritmasında çift uçlu kuyruk veri yapısı için kullanıldı.

## 3. Algoritmaların Çalışma Mantığı
BFS (Breadth-First Search) Algoritması: BFS algoritması, başlangıç düğümünden itibaren katmanlı (level-wise) olarak ilerler ve her adımda daha yakın olan düğümleri kontrol eder. FIFO kuyruk yapısını kullanarak en kısa yolu bulmaya çalışır. Özellikle, ağırlıksız graf yapılarında doğru ve garantili sonuçlar verir.

A* (A-Star) Algoritması: A* algoritması, her adımda mevcut maliyet (g) ile hedefe olan tahmini maliyet (h) toplamını kullanarak en uygun yolculuğu bulur. Bu algoritma, daha verimli sonuçlar almak için heuristik fonksiyonlardan faydalanır. Genellikle, Manhattan mesafesi veya Öklid mesafesi gibi yöntemler kullanarak hedefe olan tahmini mesafeyi hesaplar.

### Neden Bu Algoritmalar Seçildi?
BFS: Ağırlıksız graf yapılarında garantili en kısa yol bulma özelliği sunduğu için tercih ettim.

A*: Ağırlıklı graf yapılarında daha verimli çalışarak, optimal çözümleri sunması nedeniyle bu algoritmayı kullanmaya karar verdim.

### Gereksinimler
Projeyi çalıştırmak için aşağıdaki bağımlılıkları yüklemeniz gerekmektedir. Bunun için `requirements.txt` dosyasını kullanabilirsiniz:
txt
heapq
collections
math

Bu dosya, projeyi çalıştırmadan önce yüklenmesi gereken tüm kütüphaneleri içermektedir. Bağımlılıkları yüklemek için şu komutu kullanabilirsiniz:
pip install -r requirements.txt

## 4. Örnek Kullanım ve Test Sonuçları
Örnek Kullanım:
Projeyi çalıştırmak için aşağıdaki komutları takip edebilirsiniz:
python metro_simulation.py --start 'A' --end 'F'

Bu komut, 'A' noktasından 'F' noktasına olan en kısa yolu bulacaktır.

Test Sonuçları:
Örnek metro ağı için BFS ve A* algoritmalarının sonuçları:

BFS Sonucu: Başlangıç 'A' noktasından hedef 'F' noktasına giden en kısa yol:
A -> B -> C -> D -> F
Toplam mesafe: 4

A Sonucu*: Başlangıç 'A' noktasından hedef 'F' noktasına giden en kısa yol:
A -> B -> E -> F
Toplam mesafe: 3

## 5. Projeyi Geliştirme Fikirleri
Projeyi geliştirirken aşağıdaki fikirler aklıma geldi:
- Daha büyük metro ağları ile testler yaparak algoritmaların farklı büyüklükteki ağlarda nasıl performans gösterdiğini gözlemlemek.
- Farklı metro sistemleri ve hatlar ekleyerek projeyi daha geniş çapta uygulamaya dökmek.
- Kullanıcı dostu bir arayüz geliştirerek, harita üzerinde rotaları görsel olarak sunmak.
- Kullanıcıya, farklı rota alternatiflerini sunarak seçim yapmalarını sağlamak.
