# hf/index.html = Kopf/CSS der V9-Vorlage + body.tpl
src=open('../viral_reel/hf/index.html').read()
open('hf/index.html','w').write(src.split('<body>')[0]+open('body.tpl').read())
