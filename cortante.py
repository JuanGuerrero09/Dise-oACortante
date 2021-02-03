w=float(62)#carga distribuida
l=float(4.8)#longitud de viga
d=float(334.6)#d de la viga
bw=float(300)#base de la viga
fy=420#fluencia del acero
fc=21#f'c del concreto
ne=3#numero de la varilla
ast=71#area de acero de la varilla escogida
ram=2#a cuantas ramas
asf=ram*ast#area de acero de campo
dmet=d/1000
vu1=w*l/2
vu1=round(vu1,3)
vu=vu1-(dmet*w)
vu=round(vu,3)
phi=0.75
print("Su cortante máximo es {} kN, sin embargo, su cortante último es: {} kN".format(vu1,vu))
vc=0.17*fc**(1/2)*bw*d/1000
print("El cortante que da la viga es de {}".format(round(vc,2)))
vs=vu/phi-vc
if vs<=(vc*phi*0.5):
    print("La viga no necesita refuerzo a cortante")    
else: 
    print("El cortante que necesita la viga por refuerzo es: {}".format(round(vs,3)))
    vsmax=0.66*fc**(1/2)*bw*d/1000
    if vs > vsmax :
        print("La viga no puede ser diseñada, cambie la sección")
    else:
        print("El vs máximo que admite la viga es ",format(round(vsmax,2)))
        if d/2 < 600:
            s1=d/2
            s1=(round(s1/10)*10)-10
        else:
            s1=600
        print("Por norma C11.4.7.9 el espaciamiento mínimo es {}".format(s1))
        if 0.33*fc**(1/2)*bw*d/1000 < vs:
            print("Por norma C11.4.5.3 el espaciamiento se debe reducir a la mitad")
            s1=s1/2
            print("Su nuevo espaciamiento es de {}".format(s1))
        else:
            print("Por norma C11.4.5.3 el espaciamiento no se debe reducir")
            print("Vs<0.33*fc**(1/2)*bw*d, es decir {} < {}".format(round(vs,2),round(0.33*fc**(1/2)*bw*d/1000,2)))
    print("Por norma C11.4.6.3 se cálcula la separación mínima de código")
    s11=(fy*asf)/(0.062*fc**(1/2)*bw)
    s12=(fy*asf)/(0.35*bw)
    mini=min(s11,s12)
    if mini<s1:
        print("La nueva separación es {}".format(mini))
        s1=mini
    else:
        print("Aún sigue dominando la separación de {}".format(s1))
    print("Finalmente se calculará la separación por C11.4.7 a partir del Vs")
    s13=asf*fy*d/(vs*1000) #queda pendiente aproximar para decena
    print(s13)
    if s13<s1:
        print("Se usará la separación de C11.4.7, la nueva s es {}".format(s13))
        s=s13
    else:
        print("La separación previa sigue dominando, por lo que se usa un S de {}".format(s1))
        s=s1
print("El diseño a cortante de la viga es N{}({}L)@{}mmO.C.".format(ne,ram,s))



