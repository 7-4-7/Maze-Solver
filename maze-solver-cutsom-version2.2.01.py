import pygame
pygame.init()
screen=pygame.display.set_mode((1800,800))
screen.fill((20,20,20))
pygame.display.update()

def create_Grid():
    x,y=0,100
    for _ in range(6):
        for _ in range(18):
            pygame.draw.rect(screen,(40, 40, 60),(x,y,100,100))
            pygame.draw.rect(screen,(0,0,0),(x,y,100,100),4)
            x+=100
        x=0
        y+=100
def pos_in_range(coord):
    return coord[1]>99 and coord[1]<701
def update_get_pos(coord):
    return (coord[0]//100)*100,(coord[1]//100)*100
l=[]
def perform_select(pos,button):
    temp1,temp2=[],[]
    if button==1:
        up_pos=update_get_pos(pos)
        if not [up_pos] in l:
            pygame.draw.rect(screen,(0,0,0),(up_pos[0],up_pos[1],100,100))
            pygame.draw.rect(screen,(0,0,0),(up_pos[0],up_pos[1],100,100),4)
    elif button==2 and not hasattr(perform_select,"has_run1"):
        up_pos=update_get_pos(pos)
        if not [up_pos] in l:
            temp2.append(up_pos)
            temp1.append(up_pos)
            l.append(temp1)
            pygame.draw.rect(screen,(169, 10, 13),(up_pos[0],up_pos[1],100,100))
            pygame.draw.rect(screen,(0,0,0),(up_pos[0],up_pos[1],100,100),4)
            perform_select.has_run1=True
    elif button==3 and not hasattr(perform_select,"has_run2"):
        up_pos=update_get_pos(pos)
        if not [up_pos] in l:
            temp2.append(up_pos)
            l.append(temp2)
            pygame.draw.rect(screen,(31, 198, 0),(up_pos[0],up_pos[1],100,100))
            pygame.draw.rect(screen,(0,0,0),(up_pos[0],up_pos[1],100,100),4)
            perform_select.has_run2=True



status = True
create_Grid()
pygame.display.update()
while status:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            status=False      
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if pos_in_range(pygame.mouse.get_pos()):
                #count=[1,1,1]
                perform_select(pygame.mouse.get_pos(),event.button)
                       
    pygame.display.update()             

pygame.quit()