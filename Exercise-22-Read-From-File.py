'''
Exercise 22: Read From File

Given a .txt file that has a list of a bunch of names, count
how many of each name there are in the file, and print out
the results to the screen. I have a .txt file for you, if
you want to use it!

Extra:
Instead of using the .txt file from above (or instead of, if
you want the challenge), take this .txt file, and count how
many of each “category” of each image there are. This text
file is actually a list of files corresponding to the SUN
database scene recognition database, and lists the file
directory hierarchy for the images. Once you take a look at
the first line or two of the file, it will be clear which part
represents the scene category. To do this, you’re going to
have to remember a bit about string parsing in Python 3.
I talked a little bit about it in this post.

'''

# Solution
def read_file(filename):
    """
    Read a text file and store all lines into a list.
    
    Arguments:
    filename -- file name.
    
    Returns:
    lines -- a list contain all lines in the file.
    """
    with open(filename, 'r') as open_file:
        lines = open_file.read().splitlines()
    return lines

def count_each_element(input_list):
    """
    Counting each element in the list
    
    Arguments:
    input_list -- a list to be counted.
    
    Returns:
    Result -- a Counter result.
    """
    from collections import Counter
    return Counter(input_list)

def count_each_element_extra(input_list):
    """
    Counting each element in the list
    
    Arguments:
    input_list -- a list to be counted.
    
    Returns:
    Result -- a Counter result.
    """
    from collections import Counter
    new_list = [i.split('/')[2] for i in input_list]
    return Counter(new_list)
    
def main():
    file_name = 'nameslist.txt'
    content = read_file(file_name)
    print(count_each_element(content))
    
    file_name_extra = 'Training_01.txt'
    content_extra = read_file(file_name_extra)
    print(count_each_element_extra(content_extra))
    
if __name__ == "__main__":
    main()

# Test part
# Counter({'Lea': 54, 'Darth': 31, 'Luke': 15})
# Counter({'waterfall': 150, 'balcony': 100, 'bazaar': 100, 'bow_window': 100, 'canal': 100, 'car_interior': 100, 'cathedral': 100, 'chicken_coop': 100, 'church': 100, 'desert': 100, 'diner': 100, 'dinette': 100, 'elevator': 100, 'field': 100, 'forest': 100, 'general_store': 100, 'greenhouse': 100, 'hangar': 100, 'ice_skating_rink': 100, 'kennel': 100, 'library': 100, 'market': 100, 'mosque': 100, 'parking_garage': 100, 'podium': 100, 'poolroom': 100, 'stadium': 100, 'swimming_pool': 100, 'synagogue': 100, 'temple': 100, 'tennis_court': 100, 'theater': 100, 'volleyball_court': 100, 'wine_cellar': 100, 'abbey': 50, 'airplane_cabin': 50, 'airport_terminal': 50, 'alley': 50, 'amphitheater': 50, 'amusement_arcade': 50, 'amusement_park': 50, 'anechoic_chamber': 50, 'apartment_building': 50, 'apse': 50, 'aquarium': 50, 'aqueduct': 50, 'arch': 50, 'archive': 50, 'arrival_gate': 50, 'art_gallery': 50, 'art_school': 50, 'art_studio': 50, 'assembly_line': 50, 'athletic_field': 50, 'atrium': 50, 'attic': 50, 'auditorium': 50, 'auto_factory': 50, 'badlands': 50, 'badminton_court': 50, 'baggage_claim': 50, 'bakery': 50, 'ball_pit': 50, 'ballroom': 50, 'bamboo_forest': 50, 'banquet_hall': 50, 'bar': 50, 'barn': 50, 'barndoor': 50, 'baseball_field': 50, 'basement': 50, 'basilica': 50, 'basketball_court': 50, 'bathroom': 50, 'batters_box': 50, 'bayou': 50, 'beach': 50, 'beauty_salon': 50, 'bedroom': 50, 'berth': 50, 'biology_laboratory': 50, 'bistro': 50, 'boardwalk': 50, 'boat_deck': 50, 'boathouse': 50, 'bookstore': 50, 'booth': 50, 'botanical_garden': 50, 'bowling_alley': 50, 'boxing_ring': 50, 'brewery': 50, 'bridge': 50, 'building_facade': 50, 'bullring': 50, 'burial_chamber': 50, 'bus_interior': 50, 'butchers_shop': 50, 'butte': 50, 'cabin': 50, 'cafeteria': 50, 'campsite': 50, 'campus': 50, 'candy_store': 50, 'canyon': 50, 'carrousel': 50, 'casino': 50, 'castle': 50, 'catacomb': 50, 'cavern': 50, 'cemetery': 50, 'chalet': 50, 'cheese_factory': 50, 'chemistry_lab': 50, 'childs_room': 50, 'classroom': 50, 'clean_room': 50, 'cliff': 50, 'cloister': 50, 'closet': 50, 'clothing_store': 50, 'coast': 50, 'cockpit': 50, 'coffee_shop': 50, 'computer_room': 50, 'conference_center': 50, 'conference_room': 50, 'construction_site': 50, 'control_room': 50, 'control_tower': 50, 'corn_field': 50, 'corral': 50, 'corridor': 50, 'cottage_garden': 50, 'courthouse': 50, 'courtroom': 50, 'courtyard': 50, 'covered_bridge': 50, 'creek': 50, 'crevasse': 50, 'crosswalk': 50, 'cubicle': 50, 'dam': 50, 'delicatessen': 50, 'dentists_office': 50, 'dining_car': 50, 'dining_room': 50, 'discotheque': 50, 'dock': 50, 'doorway': 50, 'dorm_room': 50, 'driveway': 50, 'driving_range': 50, 'drugstore': 50, 'electrical_substation': 50, 'elevator_shaft': 50, 'engine_room': 50, 'escalator': 50, 'excavation': 50, 'factory': 50, 'fairway': 50, 'fastfood_restaurant': 50, 'fire_escape': 50, 'fire_station': 50, 'firing_range': 50, 'fishpond': 50, 'florist_shop': 50, 'food_court': 50, 'forest_path': 50, 'forest_road': 50, 'formal_garden': 50, 'fountain': 50, 'galley': 50, 'game_room': 50, 'garage': 50, 'garbage_dump': 50, 'gas_station': 50, 'gazebo': 50, 'gift_shop': 50, 'golf_course': 50, 'gymnasium': 50, 'harbor': 50, 'hayfield': 50, 'heliport': 50, 'herb_garden': 50, 'highway': 50, 'hill': 50, 'home_office': 50, 'hospital': 50, 'hospital_room': 50, 'hot_spring': 50, 'hot_tub': 50, 'hotel': 50, 'hotel_room': 50, 'house': 50, 'hunting_lodge': 50, 'ice_cream_parlor': 50, 'ice_floe': 50, 'ice_shelf': 50, 'iceberg': 50, 'igloo': 50, 'industrial_area': 50, 'inn': 50, 'islet': 50, 'jacuzzi': 50, 'jail': 50, 'jail_cell': 50, 'jewelry_shop': 50, 'kasbah': 50, 'kindergarden_classroom': 50, 'kitchen': 50, 'kitchenette': 50, 'labyrinth': 50, 'lake': 50, 'landfill': 50, 'landing_deck': 50, 'laundromat': 50, 'lecture_room': 50, 'lido_deck': 50, 'lift_bridge': 50, 'lighthouse': 50, 'limousine_interior': 50, 'living_room': 50, 'lobby': 50, 'lock_chamber': 50, 'locker_room': 50, 'mansion': 50, 'manufactured_home': 50, 'marsh': 50, 'martial_arts_gym': 50, 'mausoleum': 50, 'medina': 50, 'moat': 50, 'monastery': 50, 'motel': 50, 'mountain': 50, 'mountain_snowy': 50, 'movie_theater': 50, 'museum': 50, 'music_store': 50, 'music_studio': 50, 'nuclear_power_plant': 50, 'nursery': 50, 'oast_house': 50, 'observatory': 50, 'ocean': 50, 'office': 50, 'office_building': 50, 'oil_refinery': 50, 'oilrig': 50, 'operating_room': 50, 'orchard': 50, 'outhouse': 50, 'pagoda': 50, 'palace': 50, 'pantry': 50, 'park': 50, 'parking_lot': 50, 'parlor': 50, 'pasture': 50, 'patio': 50, 'pavilion': 50, 'pharmacy': 50, 'phone_booth': 50, 'physics_laboratory': 50, 'picnic_area': 50, 'pilothouse': 50, 'planetarium': 50, 'playground': 50, 'playroom': 50, 'plaza': 50, 'pond': 50, 'power_plant': 50, 'promenade_deck': 50, 'pub': 50, 'pulpit': 50, 'putting_green': 50, 'racecourse': 50, 'raceway': 50, 'raft': 50, 'railroad_track': 50, 'rainforest': 50, 'reception': 50, 'recreation_room': 50, 'residential_neighborhood': 50, 'restaurant': 50, 'restaurant_kitchen': 50, 'restaurant_patio': 50, 'rice_paddy': 50, 'riding_arena': 50, 'river': 50, 'rock_arch': 50, 'rope_bridge': 50, 'ruin': 50, 'runway': 50, 'sandbar': 50, 'sandbox': 50, 'sauna': 50, 'schoolhouse': 50, 'sea_cliff': 50, 'server_room': 50, 'shed': 50, 'shoe_shop': 50, 'shopfront': 50, 'shopping_mall': 50, 'shower': 50, 'skatepark': 50, 'ski_lodge': 50, 'ski_resort': 50, 'ski_slope': 50, 'sky': 50, 'skyscraper': 50, 'slum': 50, 'snowfield': 50, 'squash_court': 50, 'stable': 50, 'stage': 50, 'staircase': 50, 'street': 50, 'subway_interior': 50, 'subway_station': 50, 'supermarket': 50, 'sushi_bar': 50, 'swamp': 50, 'television_studio': 50, 'tent': 50, 'thriftshop': 50, 'throne_room': 50, 'ticket_booth': 50, 'toll_plaza': 50, 'topiary_garden': 50, 'tower': 50, 'toyshop': 50, 'track': 50, 'train_railway': 50, 'train_station': 50, 'tree_farm': 50, 'tree_house': 50, 'trench': 50, 'underwater': 50, 'utility_room': 50, 'valley': 50, 'van_interior': 50, 'vegetable_garden': 50, 'veranda': 50, 'veterinarians_office': 50, 'viaduct': 50, 'videostore': 50, 'village': 50, 'vineyard': 50, 'volcano': 50, 'waiting_room': 50, 'warehouse': 50, 'water_tower': 50, 'watering_hole': 50, 'wave': 50, 'wet_bar': 50, 'wheat_field': 50, 'wind_farm': 50, 'windmill': 50, 'wrestling_ring': 50, 'yard': 50, 'youth_hostel': 50})
