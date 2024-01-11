MyTorchvis Library to Visulaize Pytorch models 

## <div align="center">Installation</div>
```bash
sudo apt-get graphviz
python setup.py install
```

## <div align="center">Usage</div>
```bash
from torchvision.models import resnet50, ResNet50_Weights
from mytorchvis.visualize import vis_graph

model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
model.cuda()
model_input = torch.rand((1,3,250,250))
out = model(model_input.cuda())


vis_graph(model, model_input, all_layers=True, save=True, scale=2)
```
