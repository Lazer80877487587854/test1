
print("Ти звичайний чувак тобі 15 років")
q = input("пон?  ")

if q.lower() == "так":
    print("добре")
else:
    print("окей теряйся бестолоч")
    exit()

print("Ти йшов по гриби і ти загубився у лісі,ти йдеш по стежці і бачиш два тунеля, наліво і на право")
w = input("куди підеш, наліво, чи направо?:  ")

if w.lower() == "направо":
    print("Ого ти знайшов меч красава,але там був тупік, ти вийшов і залишилася тропинка на ліво"  )

else:
    print("На тебе напала діч, ти помер. Гра закінчена")
    exit()

print("Ти хочеш продовжувати путь чи хочеш іти далі?")
e = input("ну так шо, продовжуємо?  ")

if e.lower() == "так":
    print("окей")
else:
    print("окей бувай")
    exit()

print("Ти пішов далі, і там було вже 5 тунелів вибери в який тунель підеш")
r = input("Вибери тунель 1-5  ")

if r.lower() == "1":
    print("ПЕРЕМОГА, ви знайшли путь додому")

if r.lower() == "2":
    print("там була каналізація, нажаль ви потонули у говні... Гра закінчена")
    exit()

if r.lower() == "5":
    print("ПЕРЕМОГА, ви знайшли путь додому")

if r.lower() == "4":
    print("Там був гном черкаш, куди ти вдариш мечем")

    a = input("в голову, серце чи живіт? ")
    if a.lower() == "в голову":
        print("красава ти його вбив, і ти знайшов дорого додому. Гра завершена")
if a.lower() == "в серце":
    print("красава. ТИ його завалив ПЕРЕМОГА, ти знайшов дорогу додому")
else:
    print("Він тебе завалив, в нього пресс як камінь. Гра завершена")
    exit()

if r.lower() == "3":
    print("ПЕРЕМОГА, ви знайшли путь додому")

    print("Ну шо ти вижив? Сподіваюсь ти поїш ці смачні гриби що назбирав в цьому лісі.")
    print("game over")