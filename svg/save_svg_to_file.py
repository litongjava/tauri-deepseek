import os

import cairosvg


def svg_string_to_png(svg_content, output_png_path, output_width=None, output_height=None):
  """
    将SVG字符串转换为PNG文件，并可选地设置输出尺寸。

    :param svg_content: SVG内容的字符串
    :param output_png_path: 输出PNG文件的路径
    :param output_width: 输出PNG的宽度（像素）
    :param output_height: 输出PNG的高度（像素）
    """
  try:
    cairosvg.svg2png(
      bytestring=svg_content.encode('utf-8'),
      write_to=output_png_path,
      output_width=output_width,
      output_height=output_height
    )
    print(f"SVG已成功转换为PNG并保存到 '{output_png_path}'")
  except Exception as e:
    print(f"转换失败: {e}")


def read_svg_file(file_path):
  """
    从指定的文件路径读取SVG内容。

    :param file_path: SVG文件的路径
    :return: SVG内容的字符串
    """
  if not os.path.isfile(file_path):
    raise FileNotFoundError(f"SVG文件未找到: '{file_path}'")

  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      svg_content = file.read()
    return svg_content
  except Exception as e:
    raise IOError(f"读取SVG文件时出错: {e}")


if __name__ == "__main__":
  # 指定SVG文件和输出PNG文件的路径
  svg_file = 'logo.svg'  # 当前目录下的SVG文件
  output_png = 'output.png'  # 输出的PNG文件路径

  # 设置输出尺寸（可选）
  output_width = 1024
  output_height = 1024

  try:
    # 从SVG文件中读取内容
    svg_content = read_svg_file(svg_file)

    # 将SVG内容转换为PNG文件
    svg_string_to_png(svg_content, output_png, output_width=output_width, output_height=output_height)
  except Exception as e:
    print(f"处理过程中出现错误: {e}")
