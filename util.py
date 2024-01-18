import os

oridir="ori"
outdir="out"
trydir="try"
comdir="com"


def initdir():
    if not os.path.exists(oridir):
        os.makedirs(oridir)

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    if not os.path.exists(trydir):
        os.makedirs(trydir)
    
    if not os.path.exists(comdir):
        os.makedirs(comdir)

def cleanrep(rep):
    for filename in os.listdir(rep):
        if os.path.isfile(os.path.join(rep, filename)):
            os.remove(os.path.join(rep, filename))
def cleanout():
    cleanrep(outdir)
def cleantry():
    cleanrep(trydir)

def saveimgrep(img,rep,n):
    filename= os.path.join(rep,"{:s}_{:04d}.png".format("img",n))
    img.save( filename)

def saveallimgrep(images,rep):
    cleanrep(outdir)
    for n in range(len(images)) :
        img=images[n]
        saveimgrep(img,rep,n+1)

def saveimgout(img,n):
    saveimgrep(img,outdir,n)

def saveallimgout(images):
    saveimgrep(images,outdir)

def saveimgtry(img,seed):
    filename= os.path.join(trydir,"{:d}.png".format(seed))
    img.save( filename)

def saveimgcom(img,cfg,ds):
    filename= os.path.join(comdir,"cf{:0.2f}_ds{:0.2f}.png".format(cfg,ds))
    img.save( filename)