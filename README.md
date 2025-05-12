<h3 align="center">Jellybeans Pro for Zed</h3><p align="center">
A modern implementation of <a href="https://github.com/nanotech/jellybeans.vim">Jellybeans color theme</a> for <a href="https://zed.dev" target="_blank">Zed</a>.

</p>


## Usage

```bash
python3 app.py
```

## Preview
![Group 2](https://github.com/user-attachments/assets/05844b69-118e-4bb2-9364-4e90ce9d68ed)
![Group 1 (1)](https://github.com/user-attachments/assets/c971eeea-9925-46a2-bae3-bd39c5dea093)


## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Create or modify theme variants in the `variants/` directory
   - Each variant should be a YAML file with a complete color scheme
   - Use `variants/base.yml` as a reference for the required color values
4. Test your changes by running `python3 app.py`
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Requirements

- Python 3.x
- PyYAML package (`pip install pyyaml`)

## Reference

### Color Scheme Structure

Each variant YAML file must define the following color groups:

1. Base Colors:
   - `gray`, `background`, `foreground`, `cursor`

2. ANSI Colors:
   - Standard: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`
   - Bright variants: `bright_black`, `bright_red`, etc.
   - Dim variants: `dim_black`, `dim_red`, etc.

3. UI Elements:
   - `selection`, `dark_background`, `hover_background`
   - `placeholder`, `light_gray`, `mid_gray`, `dark_gray`
   - `wrap_guide`, `active_wrap_guide`
   - `border`, `border_focused`, `border_disabled`
   - `drop_target`, `scrollbar_thumb`, `link_hover`

4. Semantic Colors:
   - Status indicators: `hint`, `error`, `warning`, `success`, `info`
   - Backgrounds: `hint_bg`, `error_bg`, `warning_bg`, `success_bg`, `info_bg`
   - Borders: `hint_border`, `error_border`, `warning_border`, `success_border`, `info_border`

5. Version Control:
   - `deleted_bg`, `created_bg`, `modified_bg`, `renamed_bg`

6. Syntax Highlighting:
   - `comment`, `comment_doc`
   - `string_escape`, `string_regex`, `string_special`
   - `symbol`

See `variants/base.yml` for the complete reference implementation.

## License

MIT
