import cv2
import numpy as np

def find_red_dot():
    # 1. Kaydedilen ekran görüntüsünü belleğe yükle
    img = cv2.imread("imgs/pygame_check.png")
    
    if img is None:
        print("Görsel yüklenemedi! Önce ekran görüntüsü aldığınızdan emin olun.")
        return None

    # 2. Görüntüyü BGR (Standart OpenCV) formatından HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 3. Kırmızı rengin HSV renk uzayındaki alt ve üst sınırları
    # (Kırmızı spektrumun hem başında hem sonundadır, bu yüzden iki aralık tanımlanır)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # 4. Maskeleme: Belirtilen kırmızı aralığındaki pikselleri beyaz, geri kalanını siyah yap
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = mask1 + mask2

    # 5. Kontur (şekil sınırları) analizi yaparak beyaz bölgeleri (kırmızı daireleri) bul
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Çok küçük gürültüleri/pikselleri elemek için alan filtresi
        if cv2.contourArea(cnt) > 50:
            
            # Şeklin merkez koordinatlarını (Moment yardımıyla) hesapla
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                
                print(f"Kırmızı Nokta Tespit Edildi! Merkez Koordinatı: X={cX}, Y={cY}")
                return (cX, cY)

    print("Kırmızı nokta bulunamadı.")
    return None

if __name__ == "__main__":
    find_red_dot()