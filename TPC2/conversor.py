import re

def markdown_to_html(markdown):
    expressao_headers = '^(#{1,3})\s(.+)$'
    expressao_bold = '\*{2}(.+)\*{2}'
    expressao_italico = '\*{1}(.+)\*{1}'
    expressao_listas = '(\d)\.\s(.+)\s'
    #expressao_inicio_lista = '\s\s(1\.\s(.+)\s)'
    #expressao_final_lista = '(\d)\.\s(.+)\s[^(\d)\.\s(.+)\s]'
    expressao_link = '\[(.*)\]\((http.*)\)'
    expressao_imagens = '!\[(.*)\]\((http.*)\)'


    def convert_headers(match):
        level = len(match.group(1))
        return f'<h{level}>{match.group(2)}</h{level}>'
    
    def convert_bold(match):
        return f'<b>{match.group(1)}</b>'
    
    def convert_italico(match):
        return f'<i>{match.group(1)}</i>'
    
    #def include_ol_start(match):
    #    return f'<ol>\n{match.group(1)}'
    
    #def include_ol_end(match):
    #    return f'{match.group(1)}\n</ol>'

    def convert_listas(match):
        return f'\n<il>{match.group(2)}</il>\n'
    
    def convert_links(match):
        return f'<a href="{match.group(1)}">{match.group(2)}</a>'
    
    def convert_imagens(match):
        return f'<img src="{match.group(1)}" alt="{match.group(2)}"/>'
        
    
    html = re.sub(expressao_headers, convert_headers, markdown, flags=re.MULTILINE)
    html = re.sub(expressao_bold, convert_bold, markdown)
    html = re.sub(expressao_italico, convert_italico, markdown)
    #html = re.sub(expressao_inicio_lista, include_ol_start,markdown)
    #html = re.sub(expressao_final_lista, include_ol_end,markdown)
    html = re.sub(expressao_listas, convert_listas, markdown)
    html = re.sub(expressao_link, convert_links, markdown, flags=re.MULTILINE)
    html = re.sub(expressao_imagens, convert_imagens, markdown, flags=re.MULTILINE)

    return html

# Exemplo de uso
markdown_text = """
# Título Principal

## Subtítulo

Este é um **exemplo** de texto em Markdown.
*exemplo*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
"""

html_output = markdown_to_html(markdown_text)
print(html_output)