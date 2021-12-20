from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        # creation d'une image vide
        im_bin = Image()
 
 # affectation a l'image im_bin d'un tableau de pixels de meme taille
 # que self dont les intensites, de type uint8 (8bits non signes),
 # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
 # TODO: boucle imbriquees pour parcourir tous les pixels de l'image im_bin
 # et calculer l'image binaire
        for i in range(0,self.H):
            for k in range(0,self.W):
                if self.pixels[i,k] <= S:
                    im_bin.pixels[i,k]=0
                else :
                    im_bin.pixels[i,k]=255
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        im_bin = Image()
        
        l_min = self.H
        l_max = 0
        c_min = self.W
        c_max = 0
        for i in range(0,self.H):
            for k in range(0,self.W):
                if self.pixels[i,k] == 0:
                    if i < l_min:
                        l_min = i
                    if i > l_max:
                        l_max = i
                    if k < c_min:
                        c_min = k
                    if k > c_max:
                        c_max = k
                        
        im_bin.set_pixels(self.pixels[l_min:l_max , c_min:c_max])   
        return im_bin           

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        im_bin=Image()
        a=resize(self.pixels, (new_H,new_W), 0)
        im_bin.set_pixels(a)
        return im_bin


# np.uint8(pixels_resized*255)

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        x=0
        for k in range(0,self.H):
            for i in range(0, self.W):
                if self.pixels[k][i] == im.pixels[k][i]:
                    x = x+1
                else:
                    x = x
        return x/(self.H*self.W)   #nb d'itérations sur nb total
            

