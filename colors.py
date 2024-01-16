class Color:
    END: str = '\033[0'
    START: str = '\033[1;38;2'
    MOD: str = 'm'

    def __init__(self,
                 red: int = 100,
                 green: int = 149,
                 blue: int = 237) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def _init_limits(cls, red: int, green: int, blue: int):
        return cls(min(red, 255), min(green, 255), min(blue, 255))

    def __eq__(self, other):
        if isinstance(other, Color):
            return (
                self.red == other.red
                and self.green == other.green
                and self.blue == other.blue
            )
        return NotImplemented

    def __str__(self):
        return (
            f'{self.START};{self.red};{self.green};{self.blue}'
            f'{self.MOD}●{self.END}{self.MOD}'
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Color):
            return Color._init_limits(
                self.red + other.red,
                self.green + other.green,
                self.blue + other.blue,
            )
        return NotImplemented

    def __key(self):
        return (self.red, self.green, self.blue)

    def __hash__(self):
        return hash(self.__key())

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            other = max(0, min(other, 1))
            cl = -256*(1-other)
            F = 259 * (cl+255) / (255 * (259-cl))
            return Color._init_limits(
                int((self.red - 128) * F + 128),
                int((self.green - 128) * F + 128),
                int((self.blue - 128) * F + 128),
            )
        return NotImplemented


if __name__ == '__main__':
    dot = Color()
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    blue = Color(0, 0, 255)
    pink1 = Color(255, 70, 190)
    pink2 = Color(255, 70, 190)
    color_list = [pink1, pink2, blue, red, green, blue]
    print(f'задание 1:\nточечка: {dot}\n')
    print(f'задание 2:\n'
          f'сравним red == green: {red == green}\n'
          f'red == Color(255, 0, 0): {red == Color(255, 0, 0)}\n')
    print(f'задание 3:\nred + green: {red + green}\n')
    print(f'задание 4:\nуникальные цвета: {set(color_list)}\n')
    print(f'задание 5:\nнеполноценный синий: {0.5 * blue}')
