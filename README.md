# Udemy Lesson-54 Problem-1

## Perfect Number from 1 to 1000

* Print perfect numbers from 1 to 1000 on the screen. For this, write a function that returns whether a number is perfect or not.
* İlk önce sayının basamaklarını toplayıp bir değişkene atayabilmek içni bir değişken oluşturuyoruz.(total değişkeni)
* Daha sonra 1'den girilen sayıya kadar bir liste oluşturuyoruz. (Ayrı bir liste oluşturmak şart değil, 1'den sayıya kadar olan sayıları range fonksiyonuyla da gezebiliriz.)
* Bu 1'den sayıya kadar girilen listede geziniyoruz.
* Bu gezinme altında sayının çarpanlarını buluyoruz.
* bu çarpanları topluyoruz.
* Bu toplam, sayıya eşit mi değil mi bu koşullu kodumuzu yazıyoruz. Bu koşulu return olarak döndürüyoruz, 2.versiyonda döndürmeyip bunu print fonksiyonuyla da yazdırabilirdik ancak perfectN diye bir fonksiyon oluşturma amacında olduğumuz için return ile sonucu döndürmek daha mantıklı.
* Sonuç eşitse sayı mükemmeldir, değilse mükemmel değildir.
