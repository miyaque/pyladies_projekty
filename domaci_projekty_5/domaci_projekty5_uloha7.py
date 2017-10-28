
pisnicka = '''Princi můj maličký spi, ptáčkové sladce již sní, 
dřímají nivy i háj, utichl celičký kraj.
Měsíček stříbrný sám, okénkem dívá se k nám. 
Jak by se usnouti bál, dřímej můj princi, spi dál. 
Hajej a spi. Hajej a spi. 

Dávno již zmlk´denní vír, v zámku se rozhostil mír.
Nehne se myška ´ni již, prázdná je kuchyň i spíž. 
Jenom přes komorné práh, zaznělo žíznivé ach. 
Kdo si tu něčeho přál? Dřímej můj princi, spi dál. 

Hajej a spi. Hajej a spi. '''

def pocet_k_v_textu(retezec):
    n = 0
    for i in retezec:
        if i == 'k':
            n += 1
    return n

print(pocet_k_v_textu(pisnicka))
