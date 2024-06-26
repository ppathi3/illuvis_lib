# Illuvis Lib

A custom library for improved visualizations.

## Installation

You can install the library using the `.whl` file:

1. Download the `.whl` file from the `dist` directory.

2. Install the `.whl` file using `pip`:

    ```sh
    pip install path\to\your\whl\file\illuvis_lib-0.1.0-py3-none-any.whl
    ```

## Usage

Here’s an example of how to use the library:

```python
from illuvis_lib import create_custom_bar_chart

data = {"A": 10, "B": 20, "C": 30}
create_custom_bar_chart(data)
