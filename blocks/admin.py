from django.contrib import admin
from .models import Block, Flats


@admin.register(Flats)
class FlatsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sale_date', 'status', 'area', 'flat_price')
    date_hierarchy = 'sale_date'
    search_fields = ('full_name', )
    empty_value_display = '--без хоз--'
    list_editable = ('sale_date', )

    @admin.display(description='стоимость одной квартиры')
    def flat_price(self, obj):
        return obj.block.price_per_meter * obj.area





@admin.register(Block)
class BlocksAdmin(admin.ModelAdmin):
    list_display = ('number', 'price_per_meter', 'number_of_porches',
                    'number_of_floors', 'number_of_flats_per_floor', 'full_price', 'count_flats')

    @admin.display(description='полная стоимость всех квартир')
    def full_price(self, obj):
        #  Код не будет рабоать корректно, пока во flats не будет именно столько квартир,
        #  сколько указано в блоке (Block)

        # т.е если создать блок с 1 квартирой на весь блок и добавить только одну, то все будет работать соответственно.

        a = 0
        for flat in obj.get_flats():
            a += flat.area
        return a * obj.price_per_meter

    @admin.display(description='количество квартир')
    def count_flats(self, obj):
        return len(obj.get_flats())


