import pygame as p

class ImageLoader:
    __instance : 'ImageLoader' = None

    def __init__(self):
        self.reference_resolution : tuple[float, float] = (1600, 900)
        self.reference_rect : p.Rect = None
        self.screen : p.Surface = None

    @classmethod
    def get_instance(cls) -> 'ImageLoader':
        if cls.__instance is None:
            cls.__instance = ImageLoader()
        return cls.__instance
    
    @classmethod
    def set_reference_resolution(cls, width: float, height: float):
        instance = cls.get_instance()
        instance.reference_resolution = (width, height)
        instance.reference_rect = p.Rect(0, 0, width, height)

    @classmethod
    def set_screen(cls, screen: p.Surface):
        cls.get_instance().screen = screen

    @classmethod
    def load(cls, filename : str) -> p.Surface:
        instance = cls.get_instance()
        image = p.image.load(filename)
        return instance.resize_surface(image)
    
    @classmethod
    def scale(cls, source : p.Surface, original_size : tuple[int, int], scale : tuple[int, int]):
        scale_ratio : tuple[float, float] = (
            scale[0] / original_size[0],
            scale[1] / original_size[1]
        )

        size = (source.get_width() * scale_ratio[0], source.get_height() * scale_ratio[1])
        return p.transform.scale(source, size)
    
    @classmethod
    def resize_rect(cls, rect : p.Rect) -> p.Rect:
        instance = cls.get_instance()
        resized_size : tuple[int, int] = (instance.resize(rect.width, True), instance.resize(rect.height, False))
        resized_coordinate : tuple[int, int] = (instance.resize(rect.x, True), instance.resize(rect.y, False))
        new_rect = rect.copy()
        new_rect.width = resized_size[0]
        new_rect.height = resized_size[1]
        new_rect.x = resized_coordinate[0]
        new_rect.y = resized_coordinate[1]
        return new_rect
    
    @classmethod
    def resize_surface(cls, source : p.Surface) -> p.Surface:
        instance = cls.get_instance()
        resized_size : tuple[int, int] = (instance.resize(source.get_width(), True), instance.resize(source.get_height(), False))
        return p.transform.scale(source, resized_size)
    
    @classmethod
    def draw(cls, source : p.Surface, dest : tuple[int, int]):
        instance = cls.get_instance()
        instance.screen.blit(source, (instance.resize(dest[0], True), instance.resize(dest[1], False)))

    @classmethod
    def draw_rect(cls, color : p.Color, rect : p.Rect, width : int = 0, border : int = -1) -> p.Rect:
        instance = cls.get_instance()
        resized_rect = instance.resize_rect(rect)
        p.draw.rect(instance.screen, color, resized_rect, width, border)
        return resized_rect
    
    @classmethod
    def draw_circle(cls, color : p.Color, rect : p.Rect, radius : float, width : int = 0) -> p.Rect:
        instance = cls.get_instance()
        resized_rect = instance.resize_rect(rect)
        return p.draw.circle(instance.screen, color, resized_rect.center, instance.resize(radius, True), width)

    @classmethod
    def resize(cls, to_resize : int, is_horizontal : bool) -> int:
        if to_resize == 0:
            return 0

        instance = cls.get_instance()
        reference = instance.reference_resolution[0] if is_horizontal else instance.reference_resolution[1]
        ratio = reference / to_resize
        actual = instance.screen.get_width() if is_horizontal else instance.screen.get_height()
        return actual / ratio