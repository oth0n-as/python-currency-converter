import xmltodict

def nomes_das_moedas():

    with open("moedas.xml", "rb") as arquivo_moedas:
        dict_moedas = xmltodict.parse(arquivo_moedas)

    moedas = dict_moedas["xml"]
    return moedas

def conversoes_disponiveis():

    with open("conversoes.xml", "rb") as arquivo_conversoes:
        dict_conversoes = xmltodict.parse(arquivo_conversoes)

    conversoes =  dict_conversoes["xml"]
    dict_conversoes_disponiveis = {}

    for par_conversao in conversoes:
        moeda_origem, moeda_destino = par_conversao.split("-")

        if moeda_origem in dict_conversoes_disponiveis:
            dict_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
             dict_conversoes_disponiveis[moeda_origem] = [moeda_destino]   
    
    return dict_conversoes_disponiveis