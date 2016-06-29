import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mpc
import numpy as np

# rozmiar macierzy mniejszej

N = 20
M = 20

# funkcja obliczajaca jasnosc komorki mniejszej macierzy, jako srednia komorek odpowiadajacych tej komorce w macierzy wiekszej

def usrednij(x1, x2, y1, y2):

    sum = 0

    for i in range( x1, x2):
        for j in range (y1, y2):
            sum += img[i][j]

    return sum / ((x2-x1)*(y2-y1))


img = mpimg.imread('input.png')  # wczytanie obrazka
mpc.rgb_to_hsv(img)             # transformuj do hsv


# znajdx rozmiar wczytanego obrazka

a = img.shape
x = a[0]
y = a[1]


# stworz macierz mniejsza

img2 = np.zeros((N,M,3))


# utworz plik do zapisu

plik = open('output.txt', 'w')


# dokonaj konwersji do mniejszej macierzy, nastepnie utworz txt na podstawie jasnosci

for i in range(N):

    string = ''
    for j in range(M):


        img2[i][j] = usrednij( i*x/N, (i+1)*x/N, j*y/M, (j+1)*y/M)
        # img2[i][j] = img[i*x/20][j*y/20]      # wersja bez usredniania



        a = 1-img2[i][j][2]

        if a < 0.3:
            string += "  "
        if 0.3 <= a and a <= 0.6:
            string += "- "
        if 0.6 < a:
            string += "||"

    plik.write( string + "\n")

plik.close()





plt.imshow(img2)
plt.show()