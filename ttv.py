import pyttsx3

def text_to_voice(text):
    if text:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        # Pilih suara wanita dengan bahasa Indonesia
        for voice in voices:
            if "female" in voice.name.lower() and "indonesia" in voice.languages[0].lower():
                engine.setProperty('voice', voice.id)
                break
        engine.setProperty('rate', 150)  # Kecepatan pembicaraan
        engine.setProperty('volume', 1)   # Volume suara
        engine.say(text)
        engine.runAndWait()
    else:
        print("Tidak ada teks untuk diucapkan")

if __name__ == "__main__":
    print("Konversi Teks ke Suara")

    while True:
        input_text = input("\nMasukkan teks yang ingin dikonversi menjadi suara (tekan Enter untuk keluar): ")
        if input_text:
            text_to_voice(input_text)
        else:
            break
