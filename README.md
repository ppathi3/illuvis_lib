# Illuvis Lib

A custom library for improved visualizations.

## Steps for building the project and creating the whl file

1. Clone the repository
2. Go to the project directory
```bash
cd path/to/illuvis_lib
```
3. Ensure you have setuptools and wheel installed:
```bash
pip install setuptools wheel
```
4. Ensure you install all the required libraries from requirements.txt file
```bash
pip install -r requirements.txt
```
5. Create the distribution package
```bash
python setup.py sdist bdist_wheel
```
This command will generate the distribution files (.whl file) in the dist directory.

## Installation

You can install the library using the `.whl` file:

1. Download the `.whl` file from the `dist` directory.

2. Install the `.whl` file using `pip` in any virtual environment:

    ```sh
    pip install path\to\your\whl\file\illuvis_lib-0.1.0-py3-none-any.whl
    ```

## Usage

Here’s an example of how to use the library:

```python
from illuvis_lib import create_custom_bar_chart

data = {"A": 10, "B": 20, "C": 30}
create_custom_bar_chart(data, x_label='Keys', y_label='Values', legend_title='Legend', chart_title='Sample Bar Chart')
```
