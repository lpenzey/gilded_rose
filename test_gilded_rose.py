import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_quality_decreases_by_1(self):
        items = [Item("foo", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)

    def test_sell_by_decreases_by_1(self):
        items = [Item("foo", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality)    

    def test_quality_degrades_2x_after_sell_by_date_passes(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)

    def test_quality_is_never_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
    
    def test_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)              

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_sulfurus_quality_remains_at_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_backstagepass_increases_in_quality_by_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)      

    def test_backstagepass_increases_by_2_when_between_5_and_10_days_left(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(12, items[0].quality)

    def test_backstagepass_increases_by_3_when_less_than_6_days_left(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(13, items[0].quality)

    def test_backstagepass_is_worthless_after_sell_by_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_conjured_items_quality_decrease_by_2(self):
        items = [Item("Conjured", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)                                                        

if __name__ == '__main__':
    unittest.main()