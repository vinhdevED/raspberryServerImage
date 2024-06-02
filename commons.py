import io

import torch
import torch.nn as nn
from torchvision import models,transforms
from PIL import Image
import torchvision
from cls.going_modular.going_modular.predictions import pred_and_plot_image

class_names = ['covid','normal', 'viral pneumonia']
def get_model():
	device = "cuda" if torch.cuda.is_available() else "cpu"
	checkpoint_path='vit_32b_10ep.pt'
	model=torchvision.models.vit_b_16(weights=torchvision.models.ViT_B_16_Weights.DEFAULT).to(device)
	# for parameter in mo.parameters():
    # 	parameter.requires_grad = False
    
# 4. Change the classifier head 
	class_names = ['covid','normal', 'viral pneumonia']


	model.heads = nn.Linear(in_features=768, out_features=len(class_names)).to(device)
	#model.classifier=nn.Linear(1024,102)
	model.load_state_dict(torch.load(checkpoint_path,map_location='cpu'),strict=False)
	model.eval()
	return model


def pred(img):
	return pred_and_plot_image(model=get_model(), 
					 	image_path=img,
						 class_names=class_names )
	


# def get_flower_name(image_bytes):
#     tensor=get_tensor(image_bytes)
#     outputs=model(tensor)
#     _,prediction=outputs.max(1)
#     category=prediction.item()
#     class_idx=idx_to_class[category]
#     flower_name=cat_to_name[class_idx]

#     return flower_name