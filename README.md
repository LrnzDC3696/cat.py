# cat.py
["The ](https://bit.ly/2EqoBMo)[cat ](thecatapi.comthecatapi.com)[api  "](https://bit.ly/2EqoBMohttps://bit.ly/2EqoBMo) api wrapper in python

## Installation

```pip install -U cat.py```

## Getting Started

### Setting your Client

Set your own client by first getting an apikey at [```thecatapi```](https://thecatapi.com)

```python
from cat import Client

neko = Client("my_api_key")
```

### Examples

#### Getting cat

Getting five cats in page 1 in ascending order.

```python
cat = neko.get_cat(5, 1, "asc")
```

#### Getting cat by breed

Getting cyprus breeded cat.

```python
cat = neko.get_cat_breed("Cyprus")
```

#### Getting cat by category

Getting all cats in the category 69. Sadly there is None.

```python
cat = neko.get_cat_category(69)
```

#### Getting cat by image type

Getting cat with the gif type image.

```python
cat = neko.get_cat_image_type("gif")
```
