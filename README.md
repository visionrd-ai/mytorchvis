
<p align="center">
  <a href="https://ultralytics.com/">
  <img width="700" src="https://github.com/visionrd-ai/.github/assets/145563962/79a92550-c2e4-49f3-8229-bfe6545e54ea"></a>
</p>

## <div align="center">mytorchVis</div>

MyTorchvis Library to Visulaize Pytorch models. It is useful for quickly visualizing the architecture of PyTorch models and optionally saving the visualization as a PNG file for further reference.


## <div align="center">Installation</div>
```bash
sudo apt-get graphviz
python setup.py install
```

## <div align="center">Usage and Visuals</div>
```bash
from torchvision.models import resnet50, ResNet50_Weights
from mytorchvis.visualize import vis_graph

model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
model.cuda()
model_input = torch.rand((1,3,250,250))
out = model(model_input.cuda())

vis_graph(model, model_input, all_layers=True, save=True, scale=2)
```
<div align="center">
  <p>
      <img width="50%" src="ResNet.png"></a>
  </p>
