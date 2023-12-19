from rest_framework.pagination import PageNumberPagination


# Настроена через config.settings.py
class HabitPaginator(PageNumberPagination):
    page_size = 5
    page_query_param = "page_size"
    max_page_size = 50
