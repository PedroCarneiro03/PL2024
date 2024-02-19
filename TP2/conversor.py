

import sys,re



# Função de substituição
def substituicaoBold(match):
    return '<b>' + match.group(1) + '</b>'
def substituicaoItalico(match):
    return '<i>' + match.group(1) + '</i>'
def substituicaoTitulo1(match):
    return '<h1>' + match.group(1) + '</h1>'
def substituicaoTitulo2(match):
    return '<h2>' + match.group(1) + '</h2>'
def substituicaoTitulo3(match):
    return '<h3>' + match.group(1) + '</h3>'
def substituicaoTitulo4(match):
    return '<h4>' + match.group(1) + '</h4>'
def substituicaoTitulo5(match):
    return '<h5>' + match.group(1) + '</h5>'
def substituicaoTitulo6(match):
    return '<h6>' + match.group(1) + '</h6>'
def substituicaoLink(match):
    return '<a href=\"' + match.group(2) + "\">" + match.group(1) +'</a>'
def substituicaoImagem(match):
    return '<img src=\"' + match.group(2) + "\" alt=\"" + match.group(1) +'\"/>'



bold = r"\*\*([^\* ]*)\*\*"
italico= r"\*([^\* ]+)\*"
titulo1=r"^# (.*)"
titulo2=r"^## (.*)"
titulo3=r"^### (.*)"
titulo4=r"^#### (.*)"
titulo5=r"^##### (.*)"
titulo6=r"^###### (.*)"
link=r"[^!]\[(.+)\]\((.+)\)"
imagem=r"\!\[(.+)\]\((.+)\)"
lista=r"\d+\. (.*)', r'<li>\1</li>"

f= open("output.html", "w")
for linha in sys.stdin:
    nova_linha=re.sub(bold, substituicaoBold, linha)
    nova_linha=re.sub(italico, substituicaoItalico, nova_linha)
    nova_linha=re.sub(titulo1, substituicaoTitulo1, nova_linha)
    nova_linha=re.sub(titulo2, substituicaoTitulo2, nova_linha)
    nova_linha=re.sub(titulo3, substituicaoTitulo3, nova_linha)
    nova_linha=re.sub(titulo4, substituicaoTitulo4, nova_linha)
    nova_linha=re.sub(titulo5, substituicaoTitulo5, nova_linha)
    nova_linha=re.sub(titulo6, substituicaoTitulo6, nova_linha)
    nova_linha=re.sub(link, substituicaoLink, nova_linha)
    nova_linha=re.sub(imagem, substituicaoImagem, nova_linha)
    
    f.write(nova_linha)
    print(nova_linha)

f.close()
