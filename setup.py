from setuptools import setup, find_packages

setup(
    name='illuvis_lib',
    version='0.1.0',
    description='A custom library for improved visualizations',
    author='Pooja Pathi',
    # author_email='your.email@example.com',
    # url='https://github.com/yourusername/my_viz_lib',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        # Add other dependencies here
    ],
)
