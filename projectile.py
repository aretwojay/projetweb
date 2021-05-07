

def shoot(self):
    mouse_pos = pygame.mouse.get_pos()
    projectiles.append(Projectile(mouse_pos[0],mouse_pos[1]))
    
    
#classe Projectile
class Projectile(pygame.sprite.Sprite):
    def __init__(self, posx_end , posy_end):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("data/img/p_feu.png")
        self.posx_end = posx_end
        self.posy_end = posy_end
        
        
        self.longx =self.posx_end - player.get.x
        self.longy =self.posy_end - player.get.y
        
    def update_proj(self):
       """Mets les positionsdu projectiles à jour sur le segment
       entre le joueur et la souris"""
       self.posx += self.velocity*math.cos(math.atan2(self.longy, self.longx))
       self.posy += self.velocity*math.sin(math.atan2(self.longy, self.longx))
       self.ttl += 1
       
    def draw (self,screen):
        """Dessine le projectile sur la surface"""
        screen.blit(self.image, self.update_proj())
        
        


#dans projetfinal.py
#creation d'une boucle principale qui parcours l'ensemble du tableau de projectiles
#pour les afficher

 For projectile in projectiles:
     projectile.update_proj
     projectile.draw
     
     
 #liberer la place une fois le projectile detruit

 For projectile in projectiles:
     if(projectile.isAlive())
        projectile.update_proj()
        projectile.draw
     else:
        projectiles.remove(projective)
     
     