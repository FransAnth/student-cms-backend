from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = "pageSize"
    page_query_param = "pageNumber"
    max_page_size = 100
