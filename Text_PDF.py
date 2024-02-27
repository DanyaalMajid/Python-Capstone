import fpdf

def text_to_pdf(text, filename):
    pdf = fpdf.FPDF(format='A4')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(filename)

def test():        
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut porttitor elementum sapien, at sodales neque dignissim nec. Quisque luctus quam non pharetra pulvinar. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi vehicula vestibulum odio at lobortis. Sed finibus, massa eget consequat congue, urna eros laoreet mi, a molestie elit tellus et est. Vivamus faucibus urna a eleifend rutrum. Aliquam ultrices vel arcu vitae consectetur. Etiam a facilisis nibh.

    Fusce eget facilisis erat, et mollis elit. Fusce blandit sapien sit amet odio eleifend, eget tempus metus imperdiet. Mauris sed accumsan lacus, at faucibus urna. Praesent molestie libero at ligula aliquet viverra. Curabitur interdum sodales sapien id rhoncus. Proin lobortis finibus libero, elementum tempor sapien malesuada ut. Cras a volutpat massa, eget sollicitudin nisi. Praesent faucibus felis at orci mattis consequat. Donec mattis ipsum sapien, vel auctor nisl blandit vitae. Donec ipsum lacus, ultrices eget tristique non, pretium sed quam. Duis blandit at sapien vitae posuere.

    Nunc vitae convallis enim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nulla laoreet non orci ac bibendum. Nullam eros arcu, malesuada ac gravida in, efficitur varius quam. Ut orci justo, imperdiet at eleifend ac, consequat sed est. Sed varius magna vel ligula varius, a convallis turpis fermentum. Vestibulum bibendum sollicitudin convallis. Suspendisse nec urna ut erat feugiat aliquam non commodo ipsum. Ut vitae justo eget odio congue venenatis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris condimentum ante quis ultricies tempus. Sed a mi fermentum, lobortis tortor vitae, commodo libero. Proin sit amet velit venenatis, imperdiet elit et, ultricies leo.

    Suspendisse at nisi at arcu iaculis tempor. Mauris eget vulputate neque. Vestibulum blandit, enim id pulvinar suscipit, massa dolor bibendum turpis, nec condimentum nisi mauris ac odio. Maecenas eu efficitur enim, ut placerat diam. Pellentesque diam purus, dapibus at consectetur in, vestibulum ut sem. Donec ut luctus urna. Aenean et sodales nibh, at laoreet metus.

    Pellentesque ut auctor nunc. Mauris feugiat leo quis felis molestie, non luctus dolor maximus. Cras tristique ut justo ut condimentum. Curabitur gravida malesuada condimentum. Maecenas luctus neque at libero laoreet commodo. Praesent eu consequat nisi. Vestibulum interdum arcu quis pulvinar tincidunt. Donec quis nulla a leo commodo consequat. Maecenas mattis mattis aliquam. Vestibulum rutrum iaculis ex nec imperdiet. Fusce quis neque mauris. Vestibulum dignissim arcu neque, vel vulputate enim luctus nec. Nullam vehicula nec dui euismod lacinia. Proin lectus massa, aliquet nec sem vel, finibus laoreet nisl. Cras vel lacus eget ligula laoreet dignissim."""

    text_to_pdf(text, "lorem_ipsum.pdf")

def main():
    file = input("Enter the name of the file: ")
    with open(file, "r") as f:
        text = f.read()
    text_to_pdf(text, "output.pdf")


    