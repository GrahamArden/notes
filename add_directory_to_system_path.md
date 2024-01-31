If you have a number of  modules you want to import in a directory called "modules" you can insert it in the `sys.path`:

```python
sys.path.insert(0, './modules')
from nhs_structure_sets import NHSCollectionStructures
```