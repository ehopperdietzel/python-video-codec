conf = None

###########################################
## MODIFICAR ESTE VALOR
bandwidth = 500
###########################################

if bandwidth == 500:
    conf = {
    'filtroSeno':'FFT',             # Método utilizado para eliminar ruido sinusoidal (IIR FIR FFT)
    'interFrameThreshold':290,      # Umbral de MSE entre frames, mientras mayor sea, menos cuandrados se envian.
    'interFrameNeighbors': 3,       # Radio de cuadrados que también son enviados
    'interFrameSendAll': 25,        # Cada cuantos frames se envia el frame "completo"
    'interFrameBlur':0.5,           # Cuanto afecta los cuadrados nuevos a los vecinos anteriores en el lado del receptor
    'interFrameBlurRadius':0,       # A cuantos pixeles vecinos aplica blur ( Lo omitimos para mejorar rendimiento )
    'skipFrameAfter':4,             # Cada cuantos frames se omite uno (3 = 20fps, 4 = 24 fps, ...)
    'postQuantization':'Truncate',  # Método para reducir redundancia de las DCT ( RunLength o Truncate )
    'dynamicDendrogram':False,      # Si es True Genera un dendrograma por cada frame y lo envía
    'allQ':30,                      # Calidad de compresión para los keyframe
    'maxQ':25,                      # Calidad de compresión máxima
    'minQ':18,                                         # Calidad de compresión mínima
    'dendrograma':'dendrogramas/Dendrograma500.txt',   # Dendrograma estático
    'bandwidth':bandwidth           # Ancho de banda
    }
elif bandwidth == 1000:
    conf = {
    'filtroSeno':'FFT',
    'interFrameThreshold':145,
    'interFrameNeighbors':2,
    'interFrameSendAll': 20,
    'interFrameBlur':0.5,
    'interFrameBlurRadius':0,
    'skipFrameAfter':4,
    'postQuantization':'Truncate',
    'dynamicDendrogram':False,
    'allQ':40,
    'maxQ':30,
    'minQ':20,
    'dendrograma':'dendrogramas/Dendrograma1000.txt',
    'bandwidth':bandwidth
    }
elif bandwidth == 5000:
    conf = {
    'filtroSeno':'FFT',
    'interFrameThreshold':30,
    'interFrameNeighbors':3,
    'interFrameSendAll': 20,
    'interFrameBlur':0.5,
    'interFrameBlurRadius':0,
    'skipFrameAfter':4,
    'postQuantization':'Truncate',
    'dynamicDendrogram':False,
    'allQ':50,
    'maxQ':45,
    'minQ':30,
    'dendrograma':'dendrogramas/Dendrograma5000.txt',
    'bandwidth':bandwidth
    }
