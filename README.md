# Parola Güvenlik Değerlendirme

Bu Python programı, kullanıcının girdiği bir şifrenin güvenlik seviyesini değerlendirir.

## Nasıl Çalışır?

1. `rate_password()` fonksiyonu, şifrenin güvenlik seviyesini puanlayarak değerlendirir.
2. Şifre değerlendirilirken, uzunluk, büyük ve küçük harf kullanımı, sayı kullanımı ve özel karakter kullanımı gibi kriterler göz önünde bulundurulur.
3. `evaluate_password_security()` fonksiyonu, şifrenin güvenlik seviyesine göre uygun bir değerlendirme metni döndürür.
4. Kullanıcıdan bir şifre girişi alınır ve `evaluate_password_security()` fonksiyonu kullanılarak şifrenin güvenlik seviyesi değerlendirilir.
5. Sonuç ekrana yazdırılır.

## Kullanım

Program çalıştırıldığında, kullanıcıdan bir şifre girmesi istenir. Ardından, girilen şifrenin güvenlik seviyesi değerlendirilir ve sonuç ekrana yazdırılır.

### UYARI

Bu proje, kullanıcının girdiği şifreyi işlememekte veya saklamamaktadır. Şifre sadece geçici olarak değerlendirme için kullanılır ve hiçbir şekilde kaydedilmez veya paylaşılmaz.
