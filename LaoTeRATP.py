   
import os

os.chdir('D:\InformatiqueEtProgramme')
a=open('test.txt').read()

f_out=open('LignesParis.txt','w')
f_out.write('Ligne\tStation\tCorrespondances\n')
Doc=a.split('\n')
Lignetotal=[] #Le résultat final contenant toutes les lignes de métro
Lignetempo=[]
correstempo=[]
Nomstation=''
i=0             #i est l'indice pour les strings                #j est l'autre indice pour les strings
j=0
k=3              #k va parcourir la liste doc
check=0
Nomdeligne='1'
while k<len(Doc)-1:
    #print(k)
    if Doc[k][:5]=='Ligne':
        Lignetotal.append([Nomdeligne,Lignetempo])
        Lignetempo=[]
        Nomdeligne=Doc[k].replace('\t','').replace(' (Meteor)','').replace(' ','').replace('Ligne','')
        k+=2
    else:
        i=0
        j=0
        check=1
        while Doc[k][j]!='\t':
            if Doc[k][j]=='(':
                check=0
            if check==1:
                i+=1
            j+=1
        if check==0:
            Nomstation=Doc[k][:i-1]
        else:
            Nomstation=Doc[k][:i]
        if len(Doc[k])==j+1:
            k+=1
            Lignetempo.append([Nomstation,[]])
        else:
            correstempo=[]
            j+=1
            if (j+5<len(Doc[k]) and Doc[k][j:j+5]=='Ligne') or (j+6<len(Doc[k]) and Doc[k][j:j+6]=='Lignes'):
                j=0
                ligne=Doc[k].split('\t')[1]
                metro=ligne.split('_')[0]
                metro=metro.replace('Lignes','').replace('Ligne','').replace(' ','').replace('et',',')
                stations=metro.split(',')
                for n in range(len(stations)):
                    if stations[n] not in ["7bis","10","13"]:
                        correstempo.append(stations[n])
            Lignetempo.append([Nomstation,correstempo])
            strcorres=''
            if len(correstempo)>0:
                for i in range(len(correstempo)-1):
                    strcorres+=correstempo[i]+','
                strcorres+=correstempo[len(correstempo)-1]
            f_out.write('%s\t%s\t%s\n' %(Nomdeligne,Nomstation,strcorres))
            k+=1

Lignetotal.append([Nomdeligne,Lignetempo])
f_out.close()
Lignetotal.append(['7',[['La Courneuve 8 Mai 1945',[]],["Fort d'Aubervilliers",[]],['Aubervilliers-Pantin Quatre Chemins',[]],['Porte de la Villette',[]],['Corentin Cariou',[]],['Crimée',[]],['Riquet',[]],['Stalingrad',['2','5']],['Louis Blanc',['7bis']],["Gare de l'Est",['4','5']],['Poissonière',[]],['Cadet',[]],['Le Peletier',[]],["Chaussée d'Antin-La Fayette",['9']],['Opéra',['3','8']],['Pyramides',['14']],['Palais Royal - Musée du Louvre',['1']],['Pont Neuf',[]],['Châtelet',['1','4','11','14']],['Pont Marie',[]],['Sully-Morland',[]],['Jussieu',[]],['¨Place Monge',[]],['Censier-Dauberton',[]],["Les Gobelins",[]],["Place d'Italie",['5','6']],['Tolbiac',[]],['Maison Blanche',[]]]])
#Lignetotal contient toutes les lignes et leurs stations
DicoStations=[] #Contient toutes les stations et leurs correspondances
NomStation=[]  #Contient toutes les stations    
for i in range(len(Lignetotal)):
    for j in range(len(Lignetotal[i][1])):
        if Lignetotal[i][1][j][0] not in NomStation:
            NomStation.append(Lignetotal[i][1][j][0])
            s=Lignetotal[i][0].replace(' ','').replace('Ligne','').replace('(Meteor)','').replace("(directionGared'Austerlitz)",'').replace("(directionBoulogne)",'')
            Corresp=Lignetotal[i][1][j][1]
            Corresp.append(s)
            DicoStations.append([Lignetotal[i][1][j][0],Corresp])
def Pwint(L,s):
    l=len(L[s])-4
    print(L[s])
    print("Vous commencez par prendre la ligne %s puis à la station %s vous prendrez la ligne %s  \n " %(L[s][1],L[s][0],L[s][2]))
    b=0
    while l>0:
        print("Ensuite a partir de la ligne %s vous allez à la station %s et vous prendrez la ligne %s  \n " %(L[s][3*b+5],L[s][3*b+4],L[s][3*b+6]))
        b+=1
        l=l-3
    print("En restant sur cette ligne vous arriverez a votre destination")
    print("En prenant ce chemin vous parcourerez %s stations \n" %(str(L[s][3])))
        
        
    
    
    

def Station(li_init,li_fin,station):#Fonction servant a determiner le nom des stations les plus proches permettant la         correspondance entre deux lignes
    for i in range(len(Lignetotal)):#Station renvoie une liste contenant la station de transit, la ligne initiale, la ligne d'arrivé et la distance parcourue pour arriver jusqu'a la station d'arrivé
        if li_init==Lignetotal[i][0]:
            ind=i
    print(station)
    i=ind
    s=0
    while Lignetotal[i][1][s][0]!=station and s<len(Lignetotal[i][1]):
        s+=1
    d=s
    g=s
    Stations=[]
    while g!=-1:
        if li_fin in Lignetotal[i][1][g][1]:
            Stations.append([Lignetotal[i][1][g][0],li_init,li_fin,abs(g-s)])
            break
        g-=1
    while d!=len(Lignetotal[i][1]):
        if li_fin in Lignetotal[i][1][d][1]:
            Stations.append([Lignetotal[i][1][d][0],li_init,li_fin,abs(d-s)])
            break
        d+=1
    return Stations
def CalculTrajet(Stat_init,Stat_finale,ligne):
    for i in range(len(Lignetotal)):
        if ligne==Lignetotal[i][0].replace(' ','').replace('Ligne','').replace('(Meteor)',''):
            ind=i
    i=ind
    s=0
    while s<len(Lignetotal[i][1]) and Lignetotal[i][1][s][0]!=Stat_init:
        s+=1
    g=0
    while g<len(Lignetotal[i][1]) and Lignetotal[i][1][g][0]!=Stat_finale:
        g+=1
    return abs(g-s)
def Tridist(L,s): #Algorithme de tri qui permet d'avoir les trajets les plus rapides en premier
    for i in range(1,len(L)):
        while i>=1 and L[i][s]<L[i-1][s]:
            a=L[i]
            L[i]=L[i-1]
            L[i-1]=a
            i=i-1

    

Corresp=[]
CorrespLignes=[]  #CorrespLignes permet d'avoir toutes les lignes accessibles par une ligne
for i in range(len(Lignetotal)):
    Corresp=[]
    num=Lignetotal[i][0].replace(' ','').replace('Ligne','').replace('(Meteor)','').replace("(directionGared'Austerlitz)",'').replace("(directionBoulogne)",'')
    for j in range(len(Lignetotal[i][1])):
        
        for k in range(len(Lignetotal[i][1][j][1])):
            if Lignetotal[i][1][j][1][k] not in Corresp and Lignetotal[i][1][j][1][k]!=num:
                Corresp.append(Lignetotal[i][1][j][1][k])
    CorrespLignes.append([num,Corresp])#Si il y a problème enlever la deuxième partie du if


def TheWay(Dep,Arr): # Dep et Arr sont des noms de stations
    dist=[]
    if (Dep or Arr) not in NomStation:
        print("Station d'entrée ou d'arrivé incorrecte. Veuillez vérifier l'orthographe des stations.")
        return 0
    else:
        print('1')            #Première vérification, on vérifie que les deux stations n'ont pas une ligne en commun
        for i in range(len(DicoStations)):
            if Arr in DicoStations[i]:#DicoStations[i][0]==Arr:
                print('5')
                Arr=DicoStations[i]
            if DicoStations[i][0]==Dep:
                Dep=DicoStations[i]
        Trajet=[]
        Possible=[]
        Dist=[]
        for i in range(len(Arr[1])):
            print('3')
            if Arr[1][i] in Dep[1]:
                print('4')
                Trajet.append(Arr[1][i])
        for x in Trajet:
            Dist.append(str(CalculTrajet(Dep[0],Arr[0],x)))
        if Trajet != []:
            print('Voila les différentes lignes que vous pouvez emprunter pour atteindre votre destination :')
            for i in range(len(Trajet)):
                print("Si vous prenez la ligne %s vous allez parcourir %s stations"%(Trajet[i],Dist[i]))
        else:
            for x in Dep[1]: #D'abord on verifie que pour chaque ligne de la station de départ ne soit pas connecté a une ligne de la station d'arrivée
                Corresps=[]
                for j in range(len(CorrespLignes)):
                    if x==CorrespLignes[j][0]:
                        print('2')
                        Corresps=CorrespLignes[j][1]
                        for k in Corresps:
                            if k in Arr[1]:
                                Possible.append([x,k])
                        break
            for i in range(len(Possible)): #Puis on calcule le trajet qu'il faut faire pour arriver jusqu'a la destination en partant de la ligne qui est connecté a celle de départ.
                Stat=Station(Possible[i][0],Possible[i][1],Dep[0])
                for j in range(len(Stat)):
                    Stat[j][3]+=CalculTrajet(Stat[j][0],Arr[0],Stat[j][2])
                    Trajet.append(Stat[j])
                Tridist(Trajet,3)
            s=0
            print(Trajet)
            if Trajet!=[]:
                # print("Voici le ou les trajets disponibles si vous souhaitez aller à %s en partant de %s \n" %(Arr[0],Dep[0]))
                # while s<len(Trajet) and s<3:
                #     print("Vous commencez par prendre la ligne %s puis à la station %s vous prendrez la ligne %s et en restant sur cette ligne vous arriverez a votre destination \n " %(Trajet[s][1],Trajet[s][0],Trajet[s][2]))
                #     print("En prenant ce chemin vous parcourerez %s stations\n \n" %(str(Trajet[s][3])))
                #     s+=1
                T=[]
                while s<len(Trajet) and s<3 :
                    T.append(Trajet[s])
                    s+=1
                    print(s)
                Trajet=T
            Trajet=[]
            Possible=[]
            for x in Dep[1]: 
                
                Corresps=[]
                for j in range(len(CorrespLignes)):
                    if x==CorrespLignes[j][0]:
                        Corresps=CorrespLignes[j][1]
                        for y in Corresps:
                            Corresps2=[]
                            for i in range(len(CorrespLignes)):
                                if y==CorrespLignes[i][0]:
                                    Corresps2=CorrespLignes[i][1]
                                    for k in Corresps2:
                                        if k in Arr[1]:
                                            Possible.append([x,y,k])
                                    break
                        break
            for i in range(len(Possible)):#Puis on calcule le trajet qu'il faut faire pour arriver jusqu'a la destination en partant de la ligne qui est connecté a celle de départ en sachant que cette fois-ci il y aura deux changements
                Stat=Station(Possible[i][0],Possible[i][1],Dep[0])
                for j in range(len(Stat)):
                    Stat2=Station(Possible[i][1],Possible[i][2],Stat[j][0])
                    for k in range(len(Stat2)):
                        f=CalculTrajet(Stat2[k][0],Arr[0],Possible[i][2])
                        f+=Stat[j][3]+Stat2[k][3]
                        Trajet.append([Stat[j][0],Stat[j][1],Stat[j][2],f,Stat2[k][0],Stat[j][2],Stat2[k][2]])
            if Trajet!=[]:
                s=0
                Tridist(Trajet,3)
                l=0
                if len(T)!=0 and T[0][3]<Trajet[0][3]:#On regarde le trajet avec le moins de station à parcourir
                    print("Voici le ou les trajets les plus courts si vous souhaitez aller à %s en partant de %s \n" %(Arr[0],Dep[0]))  
                    while s<len(T):
                        print("Vous commencez par prendre la ligne %s puis à la station %s vous prendrez la ligne %s et en restant sur cette ligne vous arriverez a votre destination \n " %(T[s][1],T[s][0],T[s][2]))
                        print("En prenant ce chemin vous parcourerez %s stations\n \n" %(str(T[s][3])))
                        s+=1
                else:
                    if len(T)!=0:
                        print("Voici le ou les trajets les plus courts avec un changements : \n")
                        while s<len(T) and s<3:
                            print("Vous commencez par prendre la ligne %s puis à la station %s vous prendrez la ligne %s et en restant sur cette ligne vous arriverez a votre destination \n " %(T[s][1],T[s][0],T[s][2]))
                            print("En prenant ce chemin vous parcourerez %s stations\n \n" %(str(T[s][3])))
                            s+=1
                    print("Voici le ou les trajets les plus courts avec deux changements si vous souhaitez aller à %s en partant de %s \n" %(Arr[0],Dep[0]))
                    s=0
                    while s<len(Trajet) and s<3:
                        Pwint(Trajet,s)
                        s+=1
                        
                            
                    
                        
                        
                
            
                
                        
                    
                        
            
        


