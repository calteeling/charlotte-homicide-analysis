def filter_data(df, year='All', month_label='All', weekday_label='All', weapon='All'):
    month_labels = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    weekday_labels = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
                      4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    df_filtered = df.copy()
    if year != "All":
        df_filtered = df_filtered[df_filtered["Year"] == year]
    if month_label != "All":
        month_number = [num for num, label in month_labels.items() if label == month_label][0]
        df_filtered = df_filtered[df_filtered["Month"] == month_number]
    if weekday_label != "All":
        weekday_number = [num for num, label in weekday_labels.items() if label == weekday_label][0]
        df_filtered = df_filtered[df_filtered["Weekday"] == weekday_number]
    if weapon != "All":
        df_filtered = df_filtered[df_filtered["Weapon"] == weapon]
    return df_filtered


def simplify_weapon(weapon):
    if not isinstance(weapon, str):
        return 'Other'
    weapon = weapon.lower()
    weapon_list = [w.strip() for w in weapon.split(',')]
    for w in weapon_list:
        if any(term in w for term in ['gun', 'firearm', 'rifle', 'shotgun']):
            return 'Gun'
        elif any(term in w for term in ['knife', 'cutting instrument', 'sharp', 'razor', 'screwdriver']):
            return 'Blade'
    return 'Other'

def predict_weapon(df_input, model):
    return model.predict(df_input)

def get_month_name(n):
    labels = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return labels[n]

def get_weekday_name(n):
    labels = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
              4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    return labels[n]
