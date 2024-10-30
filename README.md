
<p align="center">
  <a href="https://ultralytics.com/">
  <img width="700" src="https://github.com/visionrd-ai/.github/assets/145563962/79a92550-c2e4-49f3-8229-bfe6545e54ea"></a>
</p>

## <div align="center">mytorchVis</div>

MyTorchvis Library to Visulaize Pytorch models. It is useful for quickly visualizing the architecture of PyTorch models and optionally saving the visualization as a PNG file for further reference.

## <div align="center">APPROACH</div>

1. The function takes several arguments:
   - **`arch`**: This is the PyTorch model (an instance of `torch.nn.Module`) whose architecture you want to visualize.
   - **`input`**: An example input tensor used to determine the input size of the model.
   - **`all_layers`**: A boolean flag indicating whether to expand nested layers in the visualization. If `True`, nested layers will be expanded. Default is `True`.
   - **`save`**: A boolean flag indicating whether to save the visualization as a PNG file. If `True`, the visualization will be saved. Default is `False`.
   - **`scale`**: A floating-point value representing the scaling factor for the graph visualization. Default is `1.5`.

2. It checks if the input tensor is a video or a single image tensor. This is determined by checking the number of dimensions of the input tensor. If the input tensor has 5 dimensions, it's considered a video model; otherwise, it's considered a single image model.

3. It sets the Jupyter format for **`graphviz`** to **PNG**.

4. It uses the **`draw_graph`** function from the `torchview` library to create a visualization of the model architecture. It provides the `arch` as the model, `input_size` to determine the input size of the model, `device='meta'` indicating that the device type is 'meta', and `expand_nested` to determine whether to expand nested layers.

5. It resizes the **graph visualization** by the specified scaling factor.

6. If `save` is `True`, it saves the visualization as a PNG file using the `render` method of the `visual_graph` attribute of the `model_graph`. The filename is determined by the type of the model (`type(arch).__name__`). It uses the `render` method with the format set to PNG. Finally, it prints **"Saved!"** to indicate that the file has been saved.

7. If `save` is `False`, it simply returns the **`visual_graph`** without saving it.

8. The function returns `None`.


## <div align="center">Installation</div>
```bash
git clone git@github.com:visionrd-ai/mytorchvis.git
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
