
# create API client
import webuiapi
import os

oridir="ori"
outdir="out"
if not os.path.exists(oridir):
   os.makedirs(oridir)

if not os.path.exists(outdir):
   os.makedirs(outdir)

api = webuiapi.WebUIApi(host='127.0.0.1', port=7860)

result1 = api.txt2img(prompt="cute squirrel",
                    negative_prompt="ugly, out of frame",
#                    seed=1003,
                    styles=["anime"],
                    cfg_scale=7,
                    n_iter=3,
#                      sampler_index='DDIM',
#                      steps=30,
#                      enable_hr=True,
#                      hr_scale=2,
#                      hr_upscaler=webuiapi.HiResUpscaler.Latent,
#                      hr_second_pass_steps=20,
#                      hr_resize_x=1536,
#                      hr_resize_y=1024,
#                      denoising_strength=0.4,

                    )

for n in range(len(result1.images)) :
    img=result1.images[n]
    filename= os.path.join(outdir,"{:s}_{:04d}.png".format("img",n+1))
    img.save( filename)