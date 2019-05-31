cat perguntas/$1* |sort -R|head -n3 > tempperg
mv tempperg perguntas/$1$(date "+%Y%m%d")
