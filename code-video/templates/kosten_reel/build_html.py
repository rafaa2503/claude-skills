# Erzeugt hf/index.html aus der V9-Vorlage (Kopf/CSS) + neuem Body.
src=open('../viral_reel/hf/index.html').read()
head=src.split('<body>')[0].replace('.hl{','.hl{display:none;')
body=open('body.tpl').read().replace('@@M1@@',str(100+int(2.5/4.2*880)-3)).replace('@@M2@@',str(100+int(2.5/4.2*880)-130))
open('hf/index.html','w').write(head+body)
