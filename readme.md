# Messages Arduino-PC
`v_amp:[taredMass],v_pos:[tension],mass:[mass],stable:[isStable]`
- `v_amp` est la tension de l'ampi qui indique le courrant
- `v_amp` est moyenné par l'arduino
- `taredMass` est simplement `A*v_amp + B - tare` avec les constantes d'étalonnage `A` et `B` 
    et la tare `tare`. 
    Il est nécessaire de calculer l'étalonnage et la tare sur l'arduino dans le cas où 
    les constantes changent sans que l'interface PC le sache.
- `v_pos` est la tension du capteur de postion, apres l'ampli
- `isStable` est soit `0` soit `1`
- message envoyé à chaque 20ms

# Messages PC-Arduino
3 commandes possibles:
`t`
- tarer la balance
`e [A] [B]`
- définir l'étalonnage, les constantes `A` et `B` sont des doubles dans l'équation `Ax + B`
`m [nb]`
- définir le moyennage, nb est le nombre de points à utiliser pour moyenner
