def _get_matching_keys(camelot_key):
    """
    Returns a list of keys that match a given camelot_key

    @param camelot_key: the camelot key to match, e.g. '1B' or '3A'
    @return: a list of keys that match camelot_key
    """
    number = int(camelot_key[:-1]) # like 3, 4, 11
    mode = camelot_key[-1:] # A or B
    matching_numbers = [
        number - 1,
        number + 1,
        number + 3,
        number - 3,
        number + 6,
        number - 6,
    ]
    # mod 12, make unique
    matching_numbers = list(set([i % 12 for i in matching_numbers]))
    # remove zero
    matching_numbers = [i for i in matching_numbers if i != 0]
    # prepend mode to each value in matching_keys
    matching_keys = [(str(key) + mode) for key in matching_numbers]


    matching_same_number = [
        str(number) + 'A',
        str(number) + 'B',
    ]


    return matching_keys + matching_same_number


def generate_camelot_key(mode, pitch_class):
    """
    Generate a camelot key from the mode and pitch_class.

    @param mode: the mode of the key, either 1 (major) or 0 (minor)
    @param pitch_class: the pitch class of the key, 0 through 11
    @return: a camelot key like '1B' or '3A'
    """
    major_pitch_class_to_camelot_map = {
        0: '8B',
        1: '3B',
        2: '10B',
        3: '5B',
        4: '12B',
        5: '7B',
        6: '2B',
        7: '9B',
        8: '4B',
        9: '11B',
        10: '6B',
        11: '1B',
    }


    minor_pitch_class_to_camelot_map = {
        0: '5A',
        1: '12A',
        2: '7A',
        3: '2A',
        4: '9A',
        5: '4A',
        6: '11A',
        7: '6A',
        8: '1A',
        9: '8A',
        10: '3A',
        11: '10A',
    }


    if mode == 1:
        return major_pitch_class_to_camelot_map[pitch_class]
    else:
        return minor_pitch_class_to_camelot_map[pitch_class]




def filter_dataframe_by_matching_keys(df, initial_key):
    matching_camelot_keys = _get_matching_keys(initial_key)


    filtered_df = df[df['camelot_key'].isin(matching_camelot_keys)]
    filtered_df = filtered_df.sort_values(by='danceability', ascending=False)
    filtered_df = filtered_df.reset_index(drop=True)
    return filtered_df