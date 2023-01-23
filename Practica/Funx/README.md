# Pràctica LP-FIB 2022/2023 Q1
### Mark Smithson Rivas

# Funx
Aquest llenguatge ha sigut creat amb ANTLR4 i Pyhton. L'esquelet de la gramàtica és una estructura anomenada block de manera recursiva per facilitar els visitadors, que és un conjunt de instruccions, on instruccions és el contenidor general que emmagatzema TOTES funcionalitats del codi.

# Contingut
* **funx.g4**: La gramàtica del LP
* **funx.py**: És el main de l'intèpret que també s'encarrega de la interfície gràfica del LP. Es troben les crides a l'arbre visitador.
* **TreeVisitor.py**: L'arbre visitador
* **MakeFile**: Genera el programa.

# Com executar el programa
Per executar el programa, un cop estiguem al PATH. Haurem de posar les següents dues comandes.

Per a poder realitzar una execució d'un codi basta amb escriure:
```
export FLASK_APP=funx
flask run
```

Un cop executem això accedim al localhost desde un navegador i podem començar a enviar peticions.

# Com utilitzar la interfície 
És **MOLT** important que pel funcionament correcte de la interfície es vagi posant una instrucció per cada submit que fem. En cas que no es faci així la interfície es pot comportar de maneres no desitjades. Els comentaris s'han de posar a la primera línia de cada intrucció.
## Exemple 1
En cas que es vulgui probar el fragment de codi d'abaix, després de cada instrucció s'hauria de donar a submit. En aquest cas tindriem **tres** submits.
```
DOS { 2 }
Suma2 x { DOS + x }
Suma2 3
```

## Exemple 2
En cas que es vulgui probar el seguüent fragment de codi, s'hauríen de fer **dos** submits, un per la definició de la funció **Euclides** i un altre per invocar-la.
```
# funció que rep dos enters i en torna el seu maxim comu divisor
Euclides a b
{
  while a != b
  {
    if a > b 
    {
      a <- a - b
    }
    else
    {
      b <- b - a
    }
  }
  a
}

Euclides 6 8
```

# Extensions
* **if-else:** Es pot utilitzar els if-else statements com es veu al següent exemple:
```
if 2 >= 3 { 4 }
else { -1 }
```

Ens imprimiria -1.

* **for-loops:** S'ha afegit els for-loops i tenen una sintaxi semblant a C++, amb les seves diferències, vegueu l'exemple:
```
sum <- 0
for i <- 0, i < 5, i <- i + 1 {
      sum <- sum + 1
}

sum
```
Ens imprimiria 5.

* **Llistes:** S'han implementat llistes amb varies operacions pre-definides:
    * **Crear llista:** Per crear una array s'usa l'operador **|=**, els elements han d'estar entre claudators i separats per espais.
    ```
    listNums |= [1 2 3 4 5 6 7 8 9 10]
    ```
    Això ens donaria una llista de tamany 10 amb els números del 1 al 10. És equivalent a la següent llista ja que s'avalua cada element de la llista.
    ```
    listNums2 |= [0+1 1+1 1+2 1+3 1+4 1+5 1+6 1+7 1+8 1+9]
    ```
    * **Afegir element:** Per afegir elements a una llista ja creada, s'ha d'utilitzar l'operador de **<<**.
    ```
    listNums2 << 1+10
    ```
    El codi anterior faria que ara listNums2 fos igual a [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]. Els elements s'afegeixen sempre al final de cada llista.
    * **Treure element:** Per treure un element s'utilitza el mateix operador que amb afegir però de manera diferent. Sempre és treu el últim element de la llista.
    ```
    << listNums2
    ```
    Això treuria l'últim element de la llista *listNums2*, és a dir el 11.

    * **Tamany:** Hi ha la paraula **len** reservada per saber el tamany d'una llista.
    ```
    len(listNums2)
    ```
    Ens retornaria 10.
    * **Indexació:** Per accedir a un element i d'una llista l és fa com si fos C++. És a dir amb els [].
     ```
    listNums2[0]
    ```
    Ens retornaria un 1.

# Excepcions
* Nom de funció ja declarada anteriorment.
* La funció que es vol invocar no existeix.
* La funció que es vol invocar no té el mateix número de parámetres que la funció creada anteriorment.
* Paràmetres incorrectes al crear una llista.
* Afegir element a una llista no declarada.
* Treure element a una llista no declarada.
* Treure element a una llista buida.
* Tamany de una llista que no existeix.
* Tamany de una variable que no es una llista.
* Accedim a l'índex d'una llista que no existeix.
* L'índex de la llista no té un rang correcte.
* Divisió entre 0.

# Jocs de proba
* **BinarySearch.funx:** Una funció de cerca dicotòmica de tota la vida.
* **ExistsInList.funx:** Cerca lineal per veure si un element existeix o no en una llista.
* **ListSum.funx:** Calcula la suma d'una llista.
