
# create API client
import webuiapi
import random
import numpy as np
import util

api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)


util.initdir()



def simpletxt2img(p,negp,n,s,stp,cfg):
    r = api.txt2img(prompt=p,
                    negative_prompt=negp,
                    steps=stp,
                    cfg_scale=cfg,
                    seed=s
                     )
    util.saveimgout(r.image,n)
    print ("TXT ► IMG:{:04d} SEED:{:d} STP:{:d} CFG:{:0.1f}".format(n,s,stp,cfg))
    return r.image

def simpleimg2img(img,p,negp,n,s,stp,cfg,ds):
    r = api.img2img(images=[img],
                    prompt=p,
                    negative_prompt=negp,
                    cfg_scale=cfg,
                    seed=s,
                    denoising_strength=ds
                     )
    util.saveimgout(r.image,n)
    print ("IMG ► IMG:{:04d} SEED:{:d} STP:{:d} CFG:{:0.1f} DS:{:0.2f}".format(n,s,stp,cfg,ds))
    return r.image

def trytxt2img(p,negp):
        s=random.randint(1, 100000000)
        r = api.txt2img(prompt=p,
                        negative_prompt=negp,
                        steps=20,
                        cfg_scale=7,
                        seed=s
                        )
        util.saveimgtry(r.image,s)
        print ("TXT ► IMG:{:04d} SEED:{:d} STP:{:d} CFG:{:0.1f}".format(n,s,20,7))


def comtxt2img(p,negp):
    s=random.randint(1, 100000000)
    r = api.txt2img(prompt=p,
                    negative_prompt=negp,
                    steps=20,
                    cfg_scale=7,
                    seed=s
                     )
    util.saveimgtry(r.image,s)
    print ("TXT ► IMG:{:04d} SEED:{:d} STP:{:d} CFG:{:0.1f}".format(n,s,20,7))
    return r.image

# for n in range(0,10,1):
#     trytxt2img("1 dog","uggly")
util.cleanout()
seed= 7071080
img=simpletxt2img("1  dog sitting","uggly",1,seed,20,7)

n=2
# for ds in np.arange(0.5,0.9,0.05):
#     simpleimg2img(img,"1 young woman","uggly",n,seed,20,7,ds)
#     n=n+1
for cfg in np.arange(5,10,0.5):
    simpleimg2img(img,"1 young woman","uggly",n,seed,20,cfg,0.6)
    n=n+1


# util.cleanout()
# seed=random.randint(1, 10000)
# n=1
# for cfg in np.arange(0.5,13,0.5):
#    simpletxt2img("1 dog","uggly",n,10,cfg,seed)
#    print ("img {:04d} CFG:{:0.1f}".format(n,cfg))
#    n=n+1
# for s in range(1000,1020,1):
#    simpletxt2img("1 dog","uggly",n,1,7,s)
#    print ("img {:04d} SEED:{:0.1f}".format(n,s))
#    n=n+1
# img=Image.open("./out/img_0001.png")
# img= simpletxt2img("1 dog","uggly",1,7,45)

# simpleimg2img(img,"a very big dog","uggly",2,45,0.2)
# simpleimg2img(img,"very big dog","uggly",3,45,0.5)
# simpleimg2img(img,"very big dog","uggly",4,45,0.6)
# simpleimg2img(img,"very big dog","uggly",5,45,0.7)
# simpleimg2img(img,"very big dog","uggly",6,45,0.8)
# simpleimg2img(img,"very big dog","uggly",7,45,0.9)
#simpleimg2img(img,"very big dog","uggly",8,45,1)
#simpletxt2img("3 dogs","uggly",3,45)
# simpletxt2img("1 dog","uggly",1,1016,20,7)
# img=simpletxt2img("1 dog","uggly",2,1016,1,7)
# #simpleimg2img(img,"1 dog","uggly",3,1016,19,7,0.5)
# n=4
# for sd in np.arange(0,1,0.1):
#     simpleimg2img(img,"1 dog","uggly",n,1030,20,7,sd)
#     n=n+1