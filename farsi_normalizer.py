# from https://gist.github.com/lingwndr/4cb2564e1bd797074420952e54b5b013
# converts all possible characters used as Persian to Persian
# converts numbers
# converts punctuations

def normalize(text):
  
  srcLine = ',?%1234567890;“”ﭘﺮﺯﻭﺻكىيﻬ٧ﺍﭙﺚﻖﯿﮎﺗﯼيﺴﻯﮥﺻﯾﺸﺿﻔﻐﻴﺞ٦ﻡےكﻩﺟﺜﻥﺰﻟﭻﻰﻣﻉﻳﺪﻤﺒ٤ﺫﺠﻲﺳﻓﺭﺨﮏﺕﻧﺵﮑ١ﮔﻗ٢ﺘﻱﻭﮯ٥ٱﻫﺩ٨ﻏﻦﻠﺺﺼﭘﺖﺏﻕﺲﺷۀﻎﻝﭽﻮﻑﺶﻨﺮﮕﮐﺣ٩٠٣ةﻍﺝﻒﭼﮓﺹﻌﯽﺛﻄڪﺬﻃﻢﻋﺑﺧﻂﺤﺥﻊﺁﻜﻞﺦﻛﺎﺯﻘﺱﻪہﺐى'
  trgLine = '،؟٪۱۲۳۴۵۶۷۸۹۰؛""پرزوصکییه۷اپثقیکتییسیهصیشضفغیج۶میکهجثنزلچیمعیدمب۴ذجیسفرخکتنشک۱گق۲تیویهاهد۸غنلصصپتبقسشهغلچوفشنرگکح۹۰۳هغجفچگصعیثطکذطمعبخطحخعآکلخکازقسههبی'

  repl = str.maketrans(srcLine, trgLine)
  repl[172] = 8204 # converting Microsoft Word ZWNJ to the unicode standard ZWNJ
  return text.translate(repl)

#usage
#normalize("1 کتاب خریدم, ديدي?")
