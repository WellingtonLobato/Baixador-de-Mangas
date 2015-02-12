# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 2014

@author: Wellington Viana Lobato Junior
"""

#Deve ser instalado primeiro os modulos BeautifulSoup e mechanize do python

import BeautifulSoup as bfs 
import mechanize
import osgit staticmethod

navegador = mechanize.Browser()
navegador.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]  

#Esse programinha so funciona com o site: http://www.mangahere.co

# pgi = raw_input("Entre com o link: \nDeve ser a primeira pagina do manga\n "
#                 "Exemplo: http://www.mangahere.co/manga/golden_boy/v01/c001"
#                 "/\n ->")
#Deve ser a primeira pagina do manga
#Exemplo: "Entre com o link: http://www.mangahere.co/manga/golden_boy/v01/c001/"

pgi = "http://www.mangahere.co/manga/minami_ke/v08/c163/"

html = navegador.open(pgi)
sopa = bfs.BeautifulSoup(html)

opcao_paginas = sopa.findAll('select', {"class": "wid60"})
opcao_paginas = str(opcao_paginas)

nome_diretorio = pgi.split('/')[4]

os.mkdir(nome_diretorio)

opcao_paginas = opcao_paginas.replace("<option value=", "")
opcao_paginas = opcao_paginas.replace("</option>", "")
opcao_paginas = opcao_paginas.replace('<option selected="selected">', "")
opcao_paginas = opcao_paginas.replace("</select>", "")
opcao_paginas = opcao_paginas.replace(
    '<select class="wid60" onchange="change_page(this)">', "")
opcao_paginas = opcao_paginas.replace('[', "")
opcao_paginas = opcao_paginas.replace(']', "")
opcao_paginas = opcao_paginas.replace('selected="selected"', '')
opcao_paginas = opcao_paginas.replace('"', "")

opcao_paginas = opcao_paginas.split("\n") #Transforma a string em lista
opcao_paginas.remove('')
opcao_paginas.remove('')


nome_do_arquivo = 0
for op in opcao_paginas:
    num = op.find(">")
    new_pgi = op[0:num]
    try:
        html2 = navegador.open(new_pgi)
        sopa2 = bfs.BeautifulSoup(html2)
        new_opcao = sopa2.findAll('img', {"id": "image"})
        for img in new_opcao:
            
            filename = str(nome_do_arquivo)+".jpg"
            nome_do_arquivo += 1
            data = navegador.open(img['src']).read()
            save = open(nome_diretorio + '/' + filename, 'wb')
            save.write(data)
            save.close()
      
    except:
        print "Processo finalizado!"
        break  
    
#So funciona no Linux!!! Tenho outra versao para Windows... 
