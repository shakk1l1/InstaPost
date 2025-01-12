from get_metadata import Get_Metadata


def Caption_generation(image_path, specific_caption = ''):
    metadata = Get_Metadata(image_path)
    caption = specific_caption + "\n" + metadata + "\nautomated post using Python"
    return caption