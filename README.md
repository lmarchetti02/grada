### Colori matplotlib per grafici

---

<img width="704" alt="colors" src="https://github.com/lmarchetti02/graphs-for-data-analysis/assets/90146345/17c94f95-7054-47dc-9e9f-8ade52ed6390">

---

# GRADA: Graphs for Data Analysis

> A library for rendering beautiful plots of analyzed data: scatter plot with error bars and fit curves.

## Installation

Follow the steps below to install _grada_:

1. Clone the repository in a directory:

   ```bash
    git clone https://github.com/lmarchetti02/grada
   ```

2. Install `wheel`, `setuptools`, `twine`

   ```bash
    pip3 install wheel
   ```

   ```bash
    pip3 install setuptools
   ```

   ```bash
    pip3 install twine
   ```

3. Build the library by running:

   ```bash
    python3 setup.py bdist_wheel
   ```

   This will create a folder named 'dist' in the working directory, which contains a file
   with '.whl' extension

4. Install the library by running:

   ```bash
   pip install /path/to/wheelfile.whl
   ```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
