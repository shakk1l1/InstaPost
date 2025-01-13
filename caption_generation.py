from get_metadata import Get_Metadata


def Caption_generation(image_path, specific_caption = ''):
    """
    :param image_path: path to the image
    :param specific_caption: caption to add
    :return: caption
    """
    metadata = Get_Metadata(image_path)
    caption = specific_caption + "\n" + metadata + "\nAutomated post"
    return caption