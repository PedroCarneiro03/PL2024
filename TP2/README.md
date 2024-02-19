# PL2024 TPC1

**Titulo** Conversor em python que transforma ficheiros MD em ficheiros HTML através de expressões regulares

**Autor** Pedro Carneiro, a100652

Foi criada um expressão regular para cada uma destas formatações de ficheiros MD:
    **1**- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
    **2**- Bold: pedaços de texto entre "**"
    **3**- Itálico: pedaços de texto entre "*"
    **4**- Lista numerada
    **5**- Link: [texto](endereço URL)
    **6**- Imagem: ![texto alternativo](path para a imagem)

Depois foi lida linha a linha do ficheiro original, dado match a cada uma das regex desenvolvidas e escritas no ficheiro final "output.html".

**Regex Desenvolvidas:**
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