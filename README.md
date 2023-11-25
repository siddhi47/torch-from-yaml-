# TorchFromYAML: Creating and Loading PyTorch Models from YAML

## Overview

The TorchFromYAML class is designed to facilitate the creation and loading of PyTorch models from YAML configuration files. This can be particularly useful for managing model architectures and configurations in a human-readable format.

## Usage

### Initialization

```python
model_builder = TorchFromYAML("your_model_config.yaml")
model = model_builder.build_model_from_config()

```

## Supported Model Types

The TorchFromYAML class currently supports the creation of models with the following architecture types:

    Sequential: A sequential model composed of a sequence of layers.

Adding Support for New Models

To extend support for additional model types, create a new method within the TorchFromYAML class following the pattern of the load_sequential method. Update the SUPPORTED_MODELS dictionary accordingly.

## YAML configuration format

```yaml

model:
  type: Sequential
  layers:
    - type: Linear
      in_features: 64
      out_features: 128
    - type: ReLU
    - type: Linear
      in_features: 128
      out_features: 10

```

## Dependencies

- PyTorch
- PyYAML