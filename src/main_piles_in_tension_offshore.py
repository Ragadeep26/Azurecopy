import numpy as np
#import pandas as pd
from PIL import Image
import math
image = Image.open('./common/pilesundertension.png')

def piles_under_tension(st):
    """ Helper for steel reinforced concrete"""

    st.title('Bearing capacity of offshore piles under tension loading')


    st.subheader('Input as per the sketch below')
    st.image(image, width = 750, use_column_width = False, output_format = 'auto')


    st.subheader('Pile under tension with specified rock parameters')
    cols = st.columns(1)
    d_w = cols[0].number_input('Drilling Diameter of the pile in m', value=3.0)

    st.subheader('Ground conditions')
    cols = st.columns(1)
    Topin = cols[0].write('Top level = 0.0 m')
    Top = 0.0
    Bottom = cols[0].number_input('Depth of the rock (m)', value=10.0)

    #cols[2].image(image, output_format = 'auto')
    k = Bottom-Top
    st.write('Rock level is '+ str(k) + 'm below the surface') 
    #phi = cols[0].number_input('Skin friction \u03C6 of the Rock layer', value = 40.0)
    Ucs = cols[0].number_input('Uniaxial Compressive Strength (U.C.S) of rock layer (MPa or N/mm2)', value = 40)
    RQD = cols[0].number_input('RQD (rock quality designation) of the rock in %', value = 30.0)
    j = 10**((0.0186*RQD)-1.91)
    Jlist = [0.000949649488668546,	0.0103841069715724,	0.0198257226164513,	0.0276806123568963,	0.0371150698398002,	0.0496919604296806,	0.0591168736966179,	0.0701285128679891,	0.0779881747164174,	0.087425018253313,	0.0937146565752489,	0.0968499315202504,	0.103139569842186,	0.107849640421663,	0.117286483958559,	0.126716169333479,	0.131433398074931,	0.137718264288884,	0.148732289514247,	0.158166746997151,	0.161306794050135,	0.17389084280199,	0.184904868027353,	0.19276214382179,	0.19747698650925,	0.200619419616227,	0.206906671884171,	0.219495492744009,	0.222633153743002,	0.2383691798178,	0.247810795462679,	0.250946070407681,	0.263534891267519,	0.274541758330907,	0.287128193136754,	0.299714627942601,	0.317013519381916,	0.331169977714255,	0.340604435197159,	0.353190870003006,	0.372076487346755,	0.386230559625103,	0.39566978921599,	0.411412973452763,	0.419272635301191,	0.431861456161029,	0.447599868289819,	0.460186303095666,	0.474337989320022,	0.491648811029296,	0.507384837104093,	0.519968885855949,	0.535697753768772,	0.546718937156109,	0.560880167596432,	0.578195761413689,	0.592356991854011,	0.600221425810423,	0.611237837089777,	0.625403839638083,	0.636420250917437,	0.644287070927841,	0.65058148135776,	0.663170302217598,	0.675756737023445,	0.691497535206226,	0.710385538603967,	0.726123950732757,	0.738717543700578,	0.751303978506425,	0.765467595000739,	0.78435559839848,	0.800101168689245,	0.818986786032994,	0.841024380699686,	0.853615587613516,	0.867783976215813,	0.883522388344603,	0.911863937657181,	0.930754327108914,	0.957518694733024,	0.970107515592862,	0.992142724205563,	1.0]
    Blist = [0.396986891019369,	0.406106389375378,	0.410680454877332,	0.422825469694728,	0.431944968050736,	0.445619443476766,	0.460799518971515,	0.468408645150822,	0.477523371398847,	0.485127725470171,	0.491207391040844,	0.50030780096492,	0.506387466535592,	0.515492648567651,	0.523097002638975,	0.535246789564354,	0.539806538742358,	0.5489164928824,	0.555010474777023,	0.564129973133031,	0.570200094487737,	0.579329137059713,	0.585423118954335,	0.596052989487045,	0.602127882949735,	0.606682860019756,	0.614277669875113,	0.620376423877719,	0.62796168951711,	0.635585132020367,	0.640159197522321,	0.649259607446397,	0.655358361449002,	0.665997776197679,	0.67361167448497,	0.68122557277226,	0.696429508806925,	0.707078467771568,	0.716197966127577,	0.723811864414867,	0.731444851134091,	0.743608954383419,	0.749698164170058,	0.752776173819261,	0.761890900067286,	0.767989654069892,	0.774097952288464,	0.781711850575754,	0.795391098109767,	0.803019312721008,	0.810642755224265,	0.81977179779624,	0.831940673153551,	0.833489222194119,	0.841107892589393,	0.845705818631263,	0.853324489026537,	0.859408926705193,	0.86398776431513,	0.868576146141034,	0.873154983750972,	0.877724277144943,	0.880773654146245,	0.886872408148851,	0.894486306436141,	0.899079460370029,	0.905197302804567,	0.911305601023139,	0.914374066456375,	0.921987964743666,	0.928091490854254,	0.934209333288793,	0.935772198653311,	0.943405185372534,	0.949532572023039,	0.95411618174096,	0.957189419282179,	0.963297717500751,	0.966413904013819,	0.971016602163673,	0.975643160853443,	0.981741914856049,	0.989384445791239,	0.99395373918521]
    index = len(Jlist)-1

    while j<Jlist[index] and index >=0:
        index = index-1
        print(index)

    if index > 0:
        pos = index+1
        beta = np.interp(j,[Jlist[pos-1],Jlist[pos]],[Blist[pos-1],Blist[pos]])
    else:
        beta = Blist[0]

    #st.write('The reduction coefficient \u03B2 is ' + str(round(beta,3)))
    qsk1 = 1.8*beta*((Ucs/200)**0.5)*1000
    st.write('Ultimate skin friction of rock layer qsk = '+str((math.ceil(qsk1/10))*10) +'kPa')
    
    st.subheader('Grout capacity')
    fck = st.number_input('Cylinder grout strength fck (MPa) (typically b/w 60MPa to 120 MPa)', value = 75)
    qsk2 = ((0.8/d_w)*(fck/0.9)**0.3)*((0.5)**0.6)*1000
    #k=0.3
    st.write('Ultimate shear capacity in the grout qsk = '+str((math.ceil(qsk2/10))*10)+' kPa')


    st.subheader('Loads')
    cols = st.columns(2)
    Tk = cols[0].number_input('Characteristic tension load on the pile (kN)', value = 1000)
    gamma_g = cols[1].number_input('Safety factor \u03B3g for the load', value = 1.35)
    st.write('Design load Td = '+ str(round(Tk*gamma_g))+'kN applied on the pile')


    st.subheader('Embedment depth')
    qsk = min(qsk1,qsk2)
    indexvalue = [qsk1,qsk2]
    indexnumber = indexvalue.index(min(indexvalue))
    qsklist = ['qsk due to rock','qsk due to grout']
    gamma_p = st.number_input('Safety factor \u03B3p for the pile', value=1.5)
    st.write("Minimum value of skin friction/shear capacity between grout and rock will be used for calculation. In this case "+ str(qsklist[indexnumber]) + ' = '+ str((math.ceil(qsk/10))*10)+' kPa')
    t = 1.5*d_w
    temp = t
    D = np.pi*d_w*t*qsk/gamma_p
    Tdl = Tk*gamma_g

    while D<Tdl:
        t= t+0.5
        D = np.pi*d_w*t*qsk/gamma_p
    
    if temp == t:
        st.write('Required embedment into the rock is '+str(t)+" m (min embedment), total length of the pile is "+str(t+Bottom)+' m')
    else:
        st.write('Required embedment into the rock is '+str(t)+" m, total length of the pile is "+str(t+Bottom)+' m')
    st.write('Interaction with other external loads are not included')
    st.write('Self weight of the pile is neglected')
    st.write('Bearing capacity in overburden materials is ignored')
    st.write('Cyclic degradation of the rock-pile interface is not considered')
    st.write('The grout shear capacity was estimated acc. to DNV0126 without shear keys')