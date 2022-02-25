print("Module Starts here")

def square_of_a_number(num):
    
    square = num**2# local variable
    
    return square, f"I am sqaured of {num}" 


def make_album(artist_name,album_title, num_of_tracks=""):
    
    album_dic ={'artist':artist_name, 'album':album_title}
    if num_of_tracks:
        album_dic['tracks']=num_of_tracks
    
    return album_dic
print("Module interpreted Successfully...")