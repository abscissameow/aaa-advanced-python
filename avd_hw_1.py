import keyword
from typing import Any, Dict


class ColorizeMixin:
    """
    миксин для цветного форматирования строки представления объекта
    """

    repr_color_code: int = 33

    def __init_subclass__(cls, **kwargs) -> None:
        """
        установка в дочерних классах значения `repr_color_code` по умолчанию
        """
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "repr_color_code"):
            cls.repr_color_code = ColorizeMixin.repr_color_code

    def colored_repr(self, text: str) -> str:
        """
        цветной вывод
        """
        return f"\033[{self.repr_color_code}m{text}\033[0m"


class Advert(ColorizeMixin):
    """
    класс для динамического создания атрибутов из JSON-объекта
    """

    def __init__(self, mapping: Dict[str, Any], is_root: bool = True) -> None:
        """
        обработка входного словаря
        """
        if is_root and "title" not in mapping:
            raise ValueError("нет обязательного атрибута title")
        self._price: int = 0
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            if isinstance(value, dict):
                value = Advert(value, is_root=False)
            self.__setattr__(key, value)

    def __getattr__(self, item: str) -> Any:
        """
        получаем атрибут
        """
        return self.__dict__.get(item, 0)

    def __setattr__(self, key: str, value: Any) -> None:
        """
        устанавливаем атрибут
        """
        if key == "price":
            if value < 0:
                raise ValueError("цена должна быть неотрицательной")
            self._price = value
        else:
            super().__setattr__(key, value)

    @property
    def price(self) -> int:
        """
        представление поля `price` как атрибута объекта
        """
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        """
        установка значения для `price`
        """
        if value < 0:
            raise ValueError("цена должна быть неотрицательной")
        self._price = value

    def __str__(self) -> str:
        """
        строковое представление
        """
        return self.colored_repr(f"{self.title} | {self.price} рублей")


if __name__ == "__main__":
    print("."*33)
    print("продадим свыню")
    pig_ad = Advert(
        {
            "title": "свынюшка",
            "price": 9999999,
            "location": {
                "address": "Москва, ул. Грузинский Вал, 7",
                "metro_stations": ["Белорусская"],
            },
            "category": "свыни",
            "color": "розовый",
        }
    )
    print(pig_ad)
    print(pig_ad.price)
    print(pig_ad.location.address)
    print(pig_ad.color)
    print("."*33)
    print("можем изменить цвет свынюшки и цвет вывода")
    pig_ad.color = "очень розовый"
    pig_ad.repr_color_code = 32
    print("теперь в объявлении:")
    print(pig_ad)
    print(pig_ad.color)
    print("."*33)
    print("продадим годзиллу без цены:")
    godzilla_ad = Advert({"title": "годзилла"})
    print(godzilla_ad)
    print("."*33)
