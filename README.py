meme_dict = {
            "LOL" : "Komik bir şeye verilen cevap",
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "ROFL" : "bir şakaya karşılık cevap",
            "OMG" : "çok şaşırmak" ,
            "CREEPY" : "korkunç" ,
            "AGGRO" : "agresifleşmek/sinirlenmek"
}
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
            
            
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Bu kelime bende yok")
