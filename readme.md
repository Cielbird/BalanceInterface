# Messages Arduino-PC
"masse:[taredMass],tension:[tension],stable:[isStable]"
- taredMass est moyenné
- tension est la tension du capteur de postion, apres l'ampli
- isStable est soit 0 soit 1
- message envoyé à chaque 20ms

# Messages PC-Arduino
3 commandes possibles:
"t"
- tarer la balance
"e [A] [B]"
- définir l'étalonnage, les constantes A et B sont des doubles dans l'équation Ax + B
"m [nb]"
- définir le moyennage, nb est le nombre de points à utiliser pour moyenner
