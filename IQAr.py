
def classificacao(indice):
    if 0<=indice<=40:
        return 1
    elif 40<indice<=80:
        return 2
    elif 80<indice<=120:
        return 3
    elif 120<indice<=200:
        return 4
    elif 200<indice<=400:
        return 5
    else: 
        return -1


def MP10(c):
    if 0<= c<= 50:
        _iqar = iqar(0, 40, 0, 50, c);
    elif 50<c<=100:
        _iqar = iqar( 41, 80, 50, 100, c);
    elif 100<c<=150:
        _iqar = iqar(81, 120, 100, 150, c);
    elif 150<c<=250:
        _iqar = iqar(121, 200, 150, 250, c);
    elif 250<=c<=600:
        _iqar = iqar(201, 400, 250, 600, c);
    
    return _iqar;


def MP25(c):

    if 0<=c<=25:
        _iqar = iqar(0, 40, 0, 25, c);
    elif 25<c<=50:
        _iqar = iqar(41, 48, 25, 50, c);
    elif 50<c<=75:
        _iqar = iqar(81, 120, 50, 75, c);
    elif 75<c<=125:
        _iqar = iqar(121, 200, 75, 125, c);
    elif 125<=c<=300:
        _iqar = iqar(201, 400, 125, 300, c);
    
    return _iqar;


def iqar(i_ini, i_fin, c_ini, c_fin, c):
    return i_ini + (((i_fin - i_ini)/(c_fin - c_ini)))*(c - c_ini)
