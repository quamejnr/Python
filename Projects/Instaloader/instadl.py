import instaloader


def dl_pp():

    """
    Function that downloads profile picture of instagram users
    """

    loader = instaloader.Instaloader()
    user = input("Username: ")
    print('downloading picture...')
    loader.download_profile(user, profile_pic_only=True)
    print('picture downloaded')
