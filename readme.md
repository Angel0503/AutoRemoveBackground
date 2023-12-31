# AutoRemoveBackground
A python script to remove background from images using [remove.bg](https://www.remove.bg/).
You can use this script to remove background from multiple images at once.
You can also use this script to remove background and replace it with a custom background color.

# Configuration
1. Clone this repository.
2. Create a .env file in the root directory of this repository.
3. Get your API key from [remove.bg/api](https://www.remove.bg/dashboard#api-key).
4. Paste your API key in the `.env` file.
5. Delete the .gitkeep file in the `Images` and ``RemoveBgImages` folders.

# Usage

## Preparation
Place all the images you want to remove background from in the `images` folder.

## Remove background
Run the following command to remove background from all the images in the `images` folder.
```python
remove_bg("classic", get_all_images())
```

## Remove background and replace it with a custom background color
Run the following command to remove background from all the images in the `images` folder and replace it with a custom background color.
```python
remove_bg("color", get_all_images(), "red")
```
The color can be a hex color code (e.g. 81d4fa, fff) or a color name (e.g. green).

## Result
The result will be saved in the `RemoveBgImages` folder.