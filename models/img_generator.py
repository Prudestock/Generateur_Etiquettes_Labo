from PIL import Image, ImageDraw, ImageFont, ImageOps
from db_handler import CONNECTION
import re
from colored_logger import log


SIZE_S = (7,4)
SIZE_L = (14,7)


def nth_repl(s, sub=" ", repl="\n", n=3):
    log.debug(f"s={s},sub={sub},repl={repl},n={n}")
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n and len(s[:find]) > 25:
        nth_repl(s, sub=" ", repl="\n", n=n - 1)
        # log.info(f)
    elif i == n:
        log.info("should be OK now")
        log.info(f"{s[:find] + repl + s[find + len(sub)::]}")
        s = s[:find] + repl + s[find + len(sub)::]
        return s
    return s


def convert_cm_to_px(cm: float):
    return cm * 37.7952755906


def convert_px_to_cm(px: float):
    return px * 0.0264583333


def create_disclaimer(size: tuple, message: str, bg_color="white"):
    """" Crée une image avec un texte"""
    FONT = ImageFont.truetype("./Assets/Fonts/arial.ttf", 200)
    W, H = size
    image = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=FONT)
    draw.multiline_text(((W - w) / 2, (H - h) / 2), message, font=FONT, fill="black")
    return image


def create_picto(picto, disclaimer: str):
    """Assemble un picto avec sa description"""
    output_name = f"{disclaimer.lower()}_merged"
    disclaimer_img = create_disclaimer((1772, 300), message=disclaimer)
    im = Image.open(picto)
    image1_size = im.size
    image2_size = disclaimer_img.size
    new_image = Image.new('RGB', (image1_size[0], image1_size[1] + image2_size[1]), (250, 250, 250))
    new_image.paste(im, (0, 0))
    new_image.paste(disclaimer_img, (0, image1_size[0]))
    new_image.save(f"./Assets/{output_name}.jpg", "JPEG")
    new_image.show()


def get_list_of_dangers(product: str) -> list:
    """returns a list of paths with dangers associated to the chemical"""
    dangers = []
    sql = f"""SELECT attention,sante,polluant,corrosif,toxique,oxydant,inflammable 
    FROM fds WHERE name = \'{product.upper()}\'"""
    c = CONNECTION.cursor()
    c.execute(sql)
    result = c.fetchone()
    attention, sante, polluant, corrosif, toxique, oxydant, inflammable = result
    if attention is not None:
        dangers.append("./Assets/Pictos/attention.jpg")
    if sante is not None:
        dangers.append("./Assets/Pictos/sante.jpg")
    if polluant is not None:
        dangers.append("./Assets/Pictos/polluant.jpg")
    if corrosif is not None:
        dangers.append("./Assets/Pictos/corrosif.jpg")
    if toxique is not None:
        dangers.append("./Assets/Pictos/toxique.jpg")
    if oxydant is not None:
        dangers.append("./Assets/Pictos/oxydant.jpg")
    if inflammable is not None:
        dangers.append("./Assets/Pictos/inflammable.jpg")
    return dangers


def assemble_pictograms(images: list) -> Image:
    """permet d'assembler les pictogrammes à partir d'une liste
    :parameter images liste d'images (paths)
    :returns génère un fichier image"""
    total_width = 0
    temp_width = 0
    height = 0
    if images == []:
        return None
    for image in images:
        im = Image.open(image)
        total_width += im.size[0] + 50 * len(images)  # Getting the total length of the generated image
        if im.size[1] >= height:
            height = im.size[1]
    new_image = Image.new(mode='RGB', size=(total_width, height), color="white")
    for image in images:
        im = Image.open(image)
        new_image.paste(im, (temp_width, 0))
        temp_width += (im.size[0] + 50)
    new_image=new_image.resize(size=(690, 300))
    # new_image.save(f'{output}.jpg', format="JPEG")
    return new_image


def create_lbl(produit: str, concentration: str, bg_color="white") -> Image:
    """" Crée une image avec le nombre d'un produit, et sa concentration"""
    size = (1050, 250)
    FONT = ImageFont.truetype("./Assets/Fonts/arial.ttf", 40)
    W, H = size
    message1 = "Nom du produit : "
    # produit_temp = nth_repl(s=produit, sub=" ", repl="\n", n=3)
    if len(produit) < 25:
        pass
    else:
        try:
            produit_t_list = re.split(" ", produit, 3)
            print(produit_t_list)
            if (len(produit[0]) + len(produit[1])) < 25:
                prod1 = " ".join(produit_t_list[0:2])
                prod2 = " ".join(produit_t_list[2:])
                produit = "\n".join([prod1, prod2])
        except:
            pass
    message2 = produit.upper()  # Affiche le nom du produit
    message3 = "Concentration : "  # Fixe
    message4 = concentration  # Affiche la concentration
    image = Image.new('RGBA', size, bg_color)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message1 + produit, font=FONT)
    draw.multiline_text((10, 50), message1, font=FONT, fill="grey")
    draw.multiline_text((320, 50), message2, font=FONT, fill="black")
    draw.multiline_text((35, 160), message3, font=FONT, fill="grey")
    draw.multiline_text((320, 160), message4, font=FONT, fill="black")
    return image


def image_resize_w_factor(path_image: str, factor: float = 0.545) -> Image:
    """:parameter path_image -> path of the image to resize
    :return a resized image
    """
    im = Image.open(path_image)
    final_w = round(im.size[0] * factor)
    final_h = round(im.size[1] * factor)
    return im.resize(size=(final_w, final_h), resample=Image.Resampling.LANCZOS)


def image_resize_w_final_size(image: Image, final_w: int = 690, final_h: int = 500) -> Image:
    """default parameters are designed to accomodate the space for danger pictos"""
    return image.resize(size=(final_w, final_h), resample=Image.Resampling.LANCZOS)


def add_url_below_qr():
    FONT = ImageFont.truetype("./Assets/Fonts/arial.ttf", 50)
    c = CONNECTION.cursor()
    sql = "SELECT name,short_url FROM 'fds' WHERE short_url IS NOT ''"""
    c.execute(sql)
    for row in c:
        prod = re.sub("\s", "_", row[0])
        output_name = f"QR+URL_{prod}"
        image_url = Image.new('RGBA', (660, 60), "white")
        draw = ImageDraw.Draw(image_url)
        _, _, w, h = draw.textbbox((0, 0), row[1], font=FONT)
        draw.multiline_text(((660 - w) / 2, (60 - h) / 2), row[1], font=FONT, fill="black")
        name = re.sub("\s", "_", row[0])
        im_qr = "../Assets/QR_Codes/QR/QR_" + name + ".png"
        image_qr = Image.open(im_qr)
        image_qr_size = image_qr.size
        image_url_size = image_url.size
        new_image = Image.new('RGB', (image_qr_size[0],
                                      image_qr_size[1] + image_url_size[1]),
                              (250, 250, 250))  # Creates an image of the correct size

        new_image.paste(image_qr, (0, 0))  # Adds the QR_Code
        new_image.paste(image_url, (0, image_qr_size[1] - 70))
        path = f"../Assets/QR_Codes/{output_name}.png"
        new_image.save(path, "PNG")
        # new_image.show()


def generate_sticker(produit: str, concentration: str):
    assert type(concentration) is str
    assert type(produit) is str
    bg = Image.new('RGBA', (1050, 750), color="white")  # Image finale
    produit = produit.upper()  # Mise en forme
    lbl = create_lbl(produit=produit, concentration=concentration)  # Création de l'en-tête

    try:
        file_name = re.sub(" ", "_", produit)
        qr = image_resize_w_factor(f'./Assets/QR_Codes/QR+URL/QR+URL_{file_name}.png')
        bg.paste(qr, (0, 250))
    except FileNotFoundError:  # Si pas de QR code
        qr = Image.new('RGB', (360, 500), "white")

    list_dangers = get_list_of_dangers(product=produit)
    log.debug(f"DANGERS POUR {produit} = {list_dangers}")
    if list_dangers != []:
        dangers = assemble_pictograms(images=list_dangers)  # Crée l'image avec les pictos
        if len(list_dangers)>1:# Récupère les dangers dans la BD
            #dangers = dangers.resize(size=(690, 300))  # Adapte la taille
            #dangers = dangers.resize(size=(290, 300), resample=Image.Resampling.LANCZOS)  # Adapte la taille
            dangers = ImageOps.expand(dangers, border=5, fill="black")  # Ajoute une bordure autour des pictos
            bg.paste(dangers, (350, 290))  # TO DO - CENTRER LES PICTOS


    bg.paste(lbl, (0, 0))
    bg = ImageOps.expand(bg,border=5,fill="black")
    return bg # Montre l'image


# add_url_below_qr()
#generate_sticker("AMIDON", "1g/L")
