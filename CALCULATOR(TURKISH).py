try:
  İlkSayi=int (input('Lütfen bir sayı giriniz:   '))
  İkinciSayi=int (input('Lütfen bir sayı daha giriniz:   '))
  Operator= input('Lütfen operatör giriniz(+, -, *, /):  ')
  if Operator == '+' :
     print(str(İlkSayi+İkinciSayi))
  elif Operator== '-' :
     print(str(İlkSayi-İkinciSayi))   
  elif Operator== '*' :
     print(str(İlkSayi*İkinciSayi))    
  elif Operator== '/' :
     print(str(İlkSayi/İkinciSayi))
  else :print('Lütfen girdiğiniz operatörü kontrol ediniz')  

except ValueError:
     print('Lütfen geçerli bir sayı giriniz!')
except ZeroDivisionError:
     print('Sıfıra bölme hatası!')
