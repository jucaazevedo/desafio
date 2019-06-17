cat perguntas/$1* |sort -Ru|head -n3 > tempperg
mv tempperg perguntas/$1$(date "+%Y%m%d")
