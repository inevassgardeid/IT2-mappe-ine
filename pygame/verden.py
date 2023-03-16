import pygame as pg
from spiller import Spiller
from hinder import Hinder
import time

spiller1 = Spiller()
hindere = []

for i in range(3):
    nytt_hinder = Hinder()
    hindere.append(nytt_hinder)

pg.init()
VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((255,255,255)) # farger bakgrunnen hvit

    for hinder in hindere:
        hinder.flytt_venstre()
        hinder.tegn(vindu)

    spiller1.tegn(vindu)
    pg.display.flip() # Oppdaterer pygame-vinduet - Denne MÅ være med!
    time.sleep(1/60)

pg.quit() # avslutter pygame
print("Ferdig")


    # pg.draw.circle(vindu, (rød,grønn,blå), (x,y), radius)
    # pg.draw.rect(vindu, (rød,grønn,blå), (x,y,bredde,høyde))
    # vindu.fill((rød,grønn,blå)) # andel rgb mellom 0-255