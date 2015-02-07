# -*- coding: utf-8 -*-
"""
@author: Wellington Viana Lobato Junior
"""
import BeautifulSoup as bfs 
import mechanize

print "Esse script serve para baixar automaticamente as paginas de qualquer manga disponivel no site http://br.mangahost.com/"
navegador = mechanize.Browser()
navegador.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]  
nome = raw_input("Digite o nome do manga")
pgi = raw_input("Digite a URL do manga que voce quer baixar:\nExemplo -> http://br.mangahost.com/manga/naruto-pt-br/700/1\n->")
html = navegador.open(pgi)
sopa = bfs.BeautifulSoup(html)
lista_link = []
opcao_c = sopa.find('select',{'class':'viewerChapter'}).findAll('option')
url_l = raw_input("Digite a URL do manga sem os capitulos e as paginas:\nExemplo -> url original = 'http://br.mangahost.com/manga/naruto-pt-br/700/1' \n url limpa = 'http://br.mangahost.com/manga/naruto-pt-br'\n->")
for cap in opcao_c:
    capitulo = cap['value']
    url = url_l+"/"+capitulo+'/'
    print url
    html_c = navegador.open(url)
    sopa_c = bfs.BeautifulSoup(html_c)
    opcao_pa = sopa_c.find('select',{'class':'viewerPage'}).findAll('option')
    for op_pa in opcao_pa:
        pagina = op_pa['value']
        url_p = url+pagina+"/"
        print url_p
        html_p = navegador.open(url_p)
        sopa_p = bfs.BeautifulSoup(html_p)
        img = sopa_p.find('div',{'class':'image-content'}).findAll('img')
        for i in img:
            data=navegador.open(i['src']).read()
            filename = nome+"_cap_"+capitulo+"pag_"+pagina+".jpg"
            save = open(filename,'wb')
            save.write(data)
            save.close()
