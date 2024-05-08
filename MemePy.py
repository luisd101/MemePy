import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import time

def add_text(top_text, bottom_text, top_color, bottom_color, meme_file):
    # create drawing object
    drawing_object = PIL.ImageDraw.Draw(meme_file)
    size = meme_file.size[0] / 10
    font_yes_or_no = input("Would you like to use your own font?: ")
    if font_yes_or_no.lower() == 'yes':
        my_font = input("Enter the file path to your font: ")
    else:
        my_font = 'impact.ttf'
    while size > 15:
        impact_top = PIL.ImageFont.truetype(my_font, size)
        if impact_top.getlength(top_text) <= meme_file.size[0]:
            break
        else:
            size -= 1

    # set font size to 60 default
    # decreemnt values to adjust for bottom text
    size = meme_file.size[0] / 10
    while size > 15:
        impact_bot = PIL.ImageFont.truetype(my_font, size)
        if impact_bot.getlength(bottom_text) <= meme_file.size[0]:
            break
        else:
            size -= 1

    # calc text height and width
    top_text_width, top_text_height = drawing_object.textbbox((0, 0), top_text, font=impact_top)[2:]
    bottom_text_width, bottom_text_height = drawing_object.textbbox((0, 0), bottom_text, font=impact_bot)[2:]
    # calc image height and width
    image_width, image_height = meme_file.size
    x_top = (image_width - top_text_width) // 2
    y_top = 0

    x_bot = (image_width - bottom_text_width) // 2
    y_bot = image_height - (bottom_text_height * 1.2)  # 1.2 is arbitrary amount so it doesn't stick to bottom of image

    # write top text onto image
    # drawing_object.text((x_top, y_top), topText, font = impact, fill = (topTextR, topTextG, topTextB))
    drawing_object.text((x_top, y_top), top_text, font=impact_top, fill=top_color)

    # write bottom text onto image
    # drawing_object.text((x_bot, y_bot), bottomText, font = impact, fill = (bottomTextR, bottomTextG, bottomTextB))
    drawing_object.text((x_bot, y_bot), bottom_text, font=impact_bot, fill=bottom_color)
    # display the completed meme to the user
    print("Memeification successful.")


def main():
    # print intro
    print("Welcome to MemePy!")

    while True:
        # user has 3 attempts to enter a valid filename
        attempts = 1
        while attempts <= 3:
            print("You are on attempt " + str(attempts) + " of 3.")
            filename = input("Enter file to memeify (including full file path): ")
            try:
                meme_file = PIL.Image.open(filename)
            except FileNotFoundError:
                print("File name not found.")
                attempts += 1
            except:
                print("Unexpected error.")
                attempts += 1
            else:
                print("File opened successfully.")
                break
        else:
            print("All three file opening attempts failed. Program will close in 5 seconds.")
            time.sleep(5)
            exit()

        # get top and bottom text and color from user
        top_text = input("Enter top text: ")
        bottom_text = input("Enter bottom text: ")
        rgb_or_color = input("Would you like select the RGB value for text color? (yes or no): ")
        if rgb_or_color.lower() == 'yes':
            top_textR = int(input("Enter red value for top text 0-255: "))
            top_textG = int(input("Enter green value for top text 0-255: "))
            top_textB = int(input("Enter blue value for top text 0-255: "))
            bottom_textR = int(input("Enter red value for bottom text 0-255: "))
            bottom_textG = int(input("Enter green value for bottom text 0-255: "))
            bottom_textB = int(input("Enter blue value for bottom text 0-255: "))
            top_color = (top_textR, top_textG, top_textB)
            bottom_color = (bottom_textR, bottom_textG, bottom_textB)
        else:
            top_color = input("Enter color for top text: ").lower()
            bottom_color = input("Enter color for bottom text: ").lower()

        add_text(top_text, bottom_text, top_color, bottom_color, meme_file)
        meme_file.show()

        # ask user if they want to save, if they do, ask for a filename and save it
        save_yes_no = input(
            "Do you want to save your meme? Enter 'save' without quotes to save, anything else for no: ")
        if save_yes_no.lower() == "save":
            newfilename = input("Enter file name (including extension) to save as: ")
            meme_file.save(newfilename)
        try_again = input("Do you want to make another meme? (enter Y for yes or N for no)")
        if try_again.lower() == "n":
            print("Thanks for using MemePy.")
            exit()


if __name__ == "__main__":
    main()
