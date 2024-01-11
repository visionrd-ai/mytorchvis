import graphviz
from torchview import draw_graph


def vis_graph(arch, input, all_layers=True, save=False, scale=1.5):
    """
    Visualizes the architecture of a PyTorch model using torchview and saves it as a PNG file.

    Args:
        arch (torch.nn.Module): The PyTorch model whose architecture you want to visualize.
        input (torch.Tensor): An example input tensor used to determine input size.
        all_layers (bool, optional): If True, expands nested layers in the visualization. Default is True.
        save (bool, optional): If True, saves the graph as a PNG file. Default is False.
        scale (float, optional): Scaling factor for the graph visualization. Default is 1.5.
    Returns:
        None
    """

    if len(input.shape) == 5: # for video model
        input = (input.shape[0], input.shape[1], input.shape[2], input.shape[3], input.shape[4])
    else: # for single image model
        input = (input.shape[0], input.shape[1], input.shape[2], input.shape[3])

    graphviz.set_jupyter_format('png')
    model_graph = draw_graph(
        arch,
        input_size=input,
        device='meta',
        expand_nested=all_layers
    )
    model_graph.resize_graph(scale=scale)

    if save:

        (model_graph.visual_graph).render(filename=str(type(arch).__name__), format='png')
        print("Saved!")
    else:
        model_graph.visual_graph

    return 

