import streamlit as st


def map():
    st.title("Map Kecamatan Pemangkat")
    st.write("**Eksplorasi wilayah Kecamatan Pemangkat dan desa-desa di dalamnya.** Pilih desa dari menu di bawah untuk melihat peta lokasi.")

    # Function to generate iframes
    def generate_iframe(url):
        return f"""
            <iframe 
                src="{url}" 
                width="100%" 
                height="500" 
                style="border:0; margin-top: 20px;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        """

    # Desa options and their iframe embed links
    desa_maps = {
        "Pemangkat Kota": generate_iframe(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d63824.359212244344!2d108.90575180012507!3d1.1444300207400568!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31e37d80fe61fc6f%3A0xd52281ccb258c2c5!2sPemangkat%20Kota%2C%20Pemangkat%2C%20Sambas%20Regency%2C%20West%20Kalimantan!5e0!3m2!1sen!2sid!4v1731934862038!5m2!1sen!2sid"
        ),
        "Gugah Sejahtera": generate_iframe(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.9808890477125!2d108.97716577381446!3d1.173932862118459!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31e482dcb850fccd%3A0x1a8004554ae57e14!2sKantor%20Desa%20Gugah%20Sejahtera!5e0!3m2!1sen!2sid!4v1731934983954!5m2!1sen!2sid"
        ),
        "Harapan": generate_iframe(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d63823.48417629835!2d108.9499423001031!3d1.1830990095744414!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31e48329fac4dbb1%3A0x88547da6bafe7ddc!2sHarapan%2C%20Pemangkat%2C%20Sambas%20Regency%2C%20West%20Kalimantan!5e0!3m2!1sen!2sid!4v1731935029099!5m2!1sen!2sid"
        ),
        "Jelutung": generate_iframe(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31912.209830741773!2d108.97268723036991!3d1.1417103337929022!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31e37d540ab6abdd%3A0x57709b336c9e59d7!2sJelutung%2C%20Pemangkat%2C%20Sambas%20Regency%2C%20West%20Kalimantan!5e0!3m2!1sen!2sid!4v1731935076332!5m2!1sen!2sid"
        ),
        "Lonam": generate_iframe(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.978168625363!2d108.9925483738144!3d1.1758381621128684!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31e48303299dccad%3A0x746b7d36c8f6dbd5!2sKANTOR%20DESA%20%26%20BALAI%20PERTEMUAN%20DESA%20LONAM!5e0!3m2!1sen!2sid!4v1731935124286!5m2!1sen!2sid"
        ),
        "Penjajap": generate_iframe(
            "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15955.84574155992!2d108.97384167883915!3d1.1874903840667366!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31e48325dc3b5689%3A0x9d98909ee32ca45c!2sPenjajap%2C%20Pemangkat%2C%20Sambas%20Regency%2C%20West%20Kalimantan!5e0!3m2!1sen!2sid!4v1731935167926!5m2!1sen!2sid"
        ),
    }

    # Default map for Kecamatan Pemangkat
    pemangkat_iframe = generate_iframe(
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d127648.3816971748!2d108.95549352542615!3d1.1519710709512534!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31e48297b82d626d%3A0x88e7f64d4723b4d5!2sPemangkat%2C%20Sambas%20Regency%2C%20West%20Kalimantan!5e0!3m2!1sen!2sid!4v1731929739437!5m2!1sen!2sid"
    )

    # Dropdown for Desa selection
    desa_choice = st.selectbox("Pilih desa:", ["Kecamatan Pemangkat"] + list(desa_maps.keys()))

    # Show the selected map
    if desa_choice == "Kecamatan Pemangkat":
        st.components.v1.html(pemangkat_iframe, height=500)
    else:
        st.components.v1.html(desa_maps[desa_choice], height=500)
