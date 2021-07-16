from datetime import datetime, date
from django.conf import settings


def get_table_time_slots_available(table):
    """
    This Function is responsible to get all a time slots for specific table by check if table have
    reservation or not, if yes get all time available and exclude the time reservation else take the current time
    and the close time of restaurant
    :param table: Object of Table
    :return: list of times available
    """
    table_reservations = table.table_reservation.filter(date=datetime.now().date(),
                                                        start_time__gte=datetime.now().replace(hour=16).time()).all()
    if table_reservations:
        current_time = datetime.now().replace(hour=16).time()
        time_slot = []
        total_reservation = len(table_reservations)
        for table_reservation_index in range(total_reservation):
            if current_time < table_reservations[table_reservation_index].start_time:
                time_slot.append(
                    {'start_time': current_time.strftime('%H:%M'),
                     'end_time': table_reservations[table_reservation_index].start_time})
                current_time = table_reservations[table_reservation_index].end_time
            elif current_time == table_reservations[table_reservation_index].start_time:
                current_time = table_reservations[table_reservation_index].end_time
            else:
                time_slot.append(
                    {'start_time': current_time, 'end_time': table_reservations[table_reservation_index].end_time})
                current_time = table_reservations[table_reservation_index].end_time
        if current_time < settings.RESTAURANT_TIME_CLOSE:
            time_slot.append(
                {'start_time': current_time, 'end_time': settings.RESTAURANT_TIME_CLOSE.strftime('%H:%M')})
        return time_slot
    else:
        return {
            "start_time": datetime.now().time().strftime('%H:%M'),
            "end_time": settings.RESTAURANT_TIME_CLOSE.strftime('%H:%M')
        }
