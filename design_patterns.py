"""
Python Design Patterns Reference
--------------------------------
This file contains implementations of common design patterns in Python for
Low-Level Design (LLD) interview preparation. All examples are runnable.
"""

import abc
import copy
import threading
from typing import List, Dict, Any, Callable
import time
import random


# ============================================================================
# CREATIONAL PATTERNS
# ============================================================================

print("\n===== CREATIONAL PATTERNS =====\n")

# ----------------------------------------------------------------------------
# 1. Singleton Pattern
# ----------------------------------------------------------------------------
print("1. Singleton Pattern")

class Singleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Singleton, cls).__new__(cls)
                cls._instance.value = 0
        return cls._instance
    
    def increment(self):
        self.value += 1
        return self.value


# Testing Singleton
singleton1 = Singleton()
singleton2 = Singleton()
print(f"Singleton instances are the same: {singleton1 is singleton2}")
singleton1.increment()
print(f"singleton1 value: {singleton1.value}, singleton2 value: {singleton2.value}")


# ----------------------------------------------------------------------------
# 2. Factory Method Pattern
# ----------------------------------------------------------------------------
print("\n2. Factory Method Pattern")

class Animal(abc.ABC):
    @abc.abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


# Testing Factory Method
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
print(f"Dog says: {dog.speak()}")
print(f"Cat says: {cat.speak()}")


# ----------------------------------------------------------------------------
# 3. Abstract Factory Pattern
# ----------------------------------------------------------------------------
print("\n3. Abstract Factory Pattern")

# Abstract product classes
class Button(abc.ABC):
    @abc.abstractmethod
    def render(self) -> str:
        pass

class Checkbox(abc.ABC):
    @abc.abstractmethod
    def render(self) -> str:
        pass

# Concrete products for Windows
class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering a Windows button"

class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering a Windows checkbox"

# Concrete products for MacOS
class MacOSButton(Button):
    def render(self) -> str:
        return "Rendering a MacOS button"

class MacOSCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendering a MacOS checkbox"

# Abstract factory
class GUIFactory(abc.ABC):
    @abc.abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abc.abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Client code
def create_ui(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


# Testing Abstract Factory
print("Windows UI:")
create_ui(WindowsFactory())
print("\nMacOS UI:")
create_ui(MacOSFactory())


# ----------------------------------------------------------------------------
# 4. Builder Pattern
# ----------------------------------------------------------------------------
print("\n4. Builder Pattern")

class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
        self.gpu = None
    
    def __str__(self):
        return f"Computer(cpu={self.cpu}, memory={self.memory}GB, storage={self.storage}GB, gpu={self.gpu})"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu: str) -> 'ComputerBuilder':
        self.computer.cpu = cpu
        return self
    
    def set_memory(self, memory: int) -> 'ComputerBuilder':
        self.computer.memory = memory
        return self
    
    def set_storage(self, storage: int) -> 'ComputerBuilder':
        self.computer.storage = storage
        return self
    
    def set_gpu(self, gpu: str) -> 'ComputerBuilder':
        self.computer.gpu = gpu
        return self
    
    def build(self) -> Computer:
        return self.computer

class ComputerDirector:
    @staticmethod
    def build_gaming_computer(builder: ComputerBuilder) -> Computer:
        return builder.set_cpu("Intel i9").set_memory(32).set_storage(1000).set_gpu("RTX 3080").build()
    
    @staticmethod
    def build_office_computer(builder: ComputerBuilder) -> Computer:
        return builder.set_cpu("Intel i5").set_memory(16).set_storage(512).set_gpu("Integrated").build()


# Testing Builder
builder = ComputerBuilder()
director = ComputerDirector()

gaming_pc = director.build_gaming_computer(builder)
print(f"Gaming PC: {gaming_pc}")

# Reset builder and create a new computer
builder = ComputerBuilder()
office_pc = director.build_office_computer(builder)
print(f"Office PC: {office_pc}")

# Use builder without director
custom_pc = ComputerBuilder().set_cpu("AMD Ryzen 7").set_memory(64).set_storage(2000).set_gpu("RTX 3070").build()
print(f"Custom PC: {custom_pc}")


# ----------------------------------------------------------------------------
# 5. Prototype Pattern
# ----------------------------------------------------------------------------
print("\n5. Prototype Pattern")

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Document(Prototype):
    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content
        self.attachments = []
    
    def add_attachment(self, attachment: str):
        self.attachments.append(attachment)
    
    def __str__(self):
        return f"Document(name='{self.name}', content='{self.content}', attachments={self.attachments})"


# Testing Prototype
original_doc = Document("Template", "This is a template document")
original_doc.add_attachment("logo.png")

# Clone the document
cloned_doc = original_doc.clone()
cloned_doc.name = "Document 1"
cloned_doc.content = "Content for Document 1"
cloned_doc.add_attachment("signature.png")

print(f"Original: {original_doc}")
print(f"Clone: {cloned_doc}")


# ============================================================================
# STRUCTURAL PATTERNS
# ============================================================================

print("\n\n===== STRUCTURAL PATTERNS =====\n")

# ----------------------------------------------------------------------------
# 6. Adapter Pattern
# ----------------------------------------------------------------------------
print("6. Adapter Pattern")

# Target interface
class UsbC:
    def connect_usb_c(self):
        return "Connected to USB-C port"

# Adaptee (incompatible interface)
class UsbA:
    def plug_usb_a(self):
        return "Plugged into USB-A port"

# Adapter
class UsbAToUsbCAdapter(UsbC):
    def __init__(self, usb_a: UsbA):
        self.usb_a = usb_a
    
    def connect_usb_c(self):
        return f"Adapter: {self.usb_a.plug_usb_a()} (converted to USB-C)"


# Testing Adapter
# Client code that expects UsbC
def connect_to_computer(device: UsbC):
    print(device.connect_usb_c())

# Using the adapter
usb_c_device = UsbC()
usb_a_device = UsbA()
adapter = UsbAToUsbCAdapter(usb_a_device)

connect_to_computer(usb_c_device)  # Works naturally
connect_to_computer(adapter)  # USB-A device works through adapter


# ----------------------------------------------------------------------------
# 7. Bridge Pattern
# ----------------------------------------------------------------------------
print("\n7. Bridge Pattern")

# Implementor
class DrawingAPI(abc.ABC):
    @abc.abstractmethod
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        pass

# Concrete Implementors
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f"API1.circle at ({x}, {y}) with radius {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x: int, y: int, radius: int) -> None:
        print(f"API2.circle at ({x}, {y}) with radius {radius}")

# Abstraction
class Shape(abc.ABC):
    def __init__(self, drawing_api: DrawingAPI):
        self.drawing_api = drawing_api
    
    @abc.abstractmethod
    def draw(self) -> None:
        pass

# Refined Abstraction
class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self) -> None:
        self.drawing_api.draw_circle(self.x, self.y, self.radius)


# Testing Bridge
api1 = DrawingAPI1()
api2 = DrawingAPI2()

circle1 = Circle(1, 2, 3, api1)
circle2 = Circle(5, 7, 11, api2)

circle1.draw()
circle2.draw()


# ----------------------------------------------------------------------------
# 8. Composite Pattern
# ----------------------------------------------------------------------------
print("\n8. Composite Pattern")

class FileSystemComponent(abc.ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abc.abstractmethod
    def display(self, indent: str = "") -> None:
        pass
    
    @abc.abstractmethod
    def get_size(self) -> int:
        pass

class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def display(self, indent: str = "") -> None:
        print(f"{indent}File: {self.name} ({self.size} KB)")
    
    def get_size(self) -> int:
        return self.size

class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.children = []
    
    def add(self, component: FileSystemComponent) -> None:
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        self.children.remove(component)
    
    def display(self, indent: str = "") -> None:
        print(f"{indent}Directory: {self.name} ({self.get_size()} KB)")
        for child in self.children:
            child.display(indent + "  ")
    
    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)


# Testing Composite
root = Directory("root")
home = Directory("home")
file1 = File("file1.txt", 5)
file2 = File("file2.txt", 10)

docs = Directory("docs")
file3 = File("file3.doc", 20)

root.add(home)
root.add(file1)
home.add(file2)
home.add(docs)
docs.add(file3)

root.display()


# ----------------------------------------------------------------------------
# 9. Decorator Pattern
# ----------------------------------------------------------------------------
print("\n9. Decorator Pattern")

class TextComponent(abc.ABC):
    @abc.abstractmethod
    def render(self) -> str:
        pass

class SimpleText(TextComponent):
    def __init__(self, text: str):
        self.text = text
    
    def render(self) -> str:
        return self.text

class TextDecorator(TextComponent, abc.ABC):
    def __init__(self, component: TextComponent):
        self.component = component

class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"<b>{self.component.render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"<i>{self.component.render()}</i>"

class UnderlineDecorator(TextDecorator):
    def render(self) -> str:
        return f"<u>{self.component.render()}</u>"


# Testing Decorator
text = SimpleText("Hello World")
print(f"Simple: {text.render()}")

bold_text = BoldDecorator(text)
print(f"Bold: {bold_text.render()}")

italic_bold_text = ItalicDecorator(bold_text)
print(f"Italic+Bold: {italic_bold_text.render()}")

underlined_italic_bold_text = UnderlineDecorator(italic_bold_text)
print(f"Underline+Italic+Bold: {underlined_italic_bold_text.render()}")


# ----------------------------------------------------------------------------
# 10. Facade Pattern
# ----------------------------------------------------------------------------
print("\n10. Facade Pattern")

# Complex subsystem components
class CPU:
    def freeze(self) -> None:
        print("CPU: Freezing processor...")
    
    def jump(self, address: str) -> None:
        print(f"CPU: Jumping to {address}")
    
    def execute(self) -> None:
        print("CPU: Executing instructions...")

class Memory:
    def load(self, address: str, data: str) -> None:
        print(f"Memory: Loading {data} at {address}")

class HardDrive:
    def read(self, sector: str, size: int) -> str:
        print(f"HardDrive: Reading {size}KB from sector {sector}")
        return "Boot data"

# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start(self) -> None:
        print("\nComputer start sequence:")
        self.cpu.freeze()
        self.memory.load("0x00", self.hard_drive.read("Master Boot Record", 512))
        self.cpu.jump("0x00")
        self.cpu.execute()
        print("Computer started successfully!")


# Testing Facade
computer = ComputerFacade()
computer.start()


# ----------------------------------------------------------------------------
# 11. Flyweight Pattern
# ----------------------------------------------------------------------------
print("\n11. Flyweight Pattern")

class Character:
    def __init__(self, symbol: str, font: str, size: int):
        self.symbol = symbol
        self.font = font
        self.size = size
        # Simulate memory consumption
        print(f"Creating character: {symbol} with font {font} and size {size}")
    
    def render(self, position_x: int, position_y: int) -> None:
        # Extrinsic state passed as method parameters
        print(f"Rendering '{self.symbol}' at ({position_x}, {position_y}) using {self.font} font, size {self.size}")

class CharacterFactory:
    _characters: Dict[str, Character] = {}
    
    @classmethod
    def get_character(cls, symbol: str, font: str, size: int) -> Character:
        key = f"{symbol}_{font}_{size}"
        if key not in cls._characters:
            cls._characters[key] = Character(symbol, font, size)
        return cls._characters[key]


# Testing Flyweight
factory = CharacterFactory()

# These will create new Character instances
char1 = factory.get_character("A", "Arial", 12)
char2 = factory.get_character("B", "Arial", 12)

# This will reuse the existing "A" Character instance
char3 = factory.get_character("A", "Arial", 12)

# Render characters at different positions (extrinsic state)
char1.render(10, 10)
char2.render(20, 10)
char3.render(30, 10)

print(f"char1 is char3: {char1 is char3}")
print(f"Total characters created: {len(CharacterFactory._characters)}")


# ----------------------------------------------------------------------------
# 12. Proxy Pattern
# ----------------------------------------------------------------------------
print("\n12. Proxy Pattern")

class Image(abc.ABC):
    @abc.abstractmethod
    def display(self) -> None:
        pass

class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_from_disk()
    
    def _load_from_disk(self) -> None:
        print(f"Loading image from disk: {self.filename}")
        # Simulate heavy loading operation
        time.sleep(0.1)
    
    def display(self) -> None:
        print(f"Displaying image: {self.filename}")

class ImageProxy(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None
    
    def display(self) -> None:
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


# Testing Proxy
# Without proxy - loads immediately when created
print("Creating real image:")
real_image = RealImage("nature.jpg")

# With proxy - loads only when display() is called
print("\nCreating proxy image:")
proxy_image = ImageProxy("city.jpg")

print("\nDisplaying images:")
real_image.display()  # Already loaded
proxy_image.display()  # Loads and then displays

print("\nDisplaying proxy image again:")
proxy_image.display()  # Already loaded, no loading necessary


# ============================================================================
# BEHAVIORAL PATTERNS
# ============================================================================

print("\n\n===== BEHAVIORAL PATTERNS =====\n")

# ----------------------------------------------------------------------------
# 13. Chain of Responsibility Pattern
# ----------------------------------------------------------------------------
print("13. Chain of Responsibility Pattern")

class Handler(abc.ABC):
    def __init__(self):
        self.next_handler = None
    
    def set_next(self, handler: 'Handler') -> 'Handler':
        self.next_handler = handler
        return handler
    
    @abc.abstractmethod
    def handle(self, request: int) -> str:
        pass

class AbstractHandler(Handler):
    def handle(self, request: int) -> str:
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class Level1Support(AbstractHandler):
    def handle(self, request: int) -> str:
        if request <= 10:
            return f"Level 1 Support: Handled request {request}"
        return super().handle(request)

class Level2Support(AbstractHandler):
    def handle(self, request: int) -> str:
        if 10 < request <= 20:
            return f"Level 2 Support: Handled request {request}"
        return super().handle(request)

class Level3Support(AbstractHandler):
    def handle(self, request: int) -> str:
        if 20 < request <= 30:
            return f"Level 3 Support: Handled request {request}"
        return super().handle(request)


# Testing Chain of Responsibility
level1 = Level1Support()
level2 = Level2Support()
level3 = Level3Support()

# Set up the chain
level1.set_next(level2).set_next(level3)

# Process some requests
print(level1.handle(5))
print(level1.handle(15))
print(level1.handle(25))
print(level1.handle(35) or "Request not handled")


# ----------------------------------------------------------------------------
# 14. Command Pattern
# ----------------------------------------------------------------------------
print("\n14. Command Pattern")

class Light:
    def __init__(self, name: str):
        self.name = name
    
    def turn_on(self) -> None:
        print(f"{self.name} light is ON")
    
    def turn_off(self) -> None:
        print(f"{self.name} light is OFF")

class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> None:
        pass
    
    @abc.abstractmethod
    def undo(self) -> None:
        pass

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self) -> None:
        self.light.turn_on()
    
    def undo(self) -> None:
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self) -> None:
        self.light.turn_off()
    
    def undo(self) -> None:
        self.light.turn_on()

class RemoteControl:
    def __init__(self):
        self.command = None
        self.history: List[Command] = []
    
    def set_command(self, command: Command) -> None:
        self.command = command
    
    def press_button(self) -> None:
        if self.command:
            self.command.execute()
            self.history.append(self.command)
    
    def undo_last(self) -> None:
        if self.history:
            last_command = self.history.pop()
            last_command.undo()


# Testing Command
living_room_light = Light("Living Room")
kitchen_light = Light("Kitchen")

living_room_on = LightOnCommand(living_room_light)
living_room_off = LightOffCommand(living_room_light)
kitchen_on = LightOnCommand(kitchen_light)
kitchen_off = LightOffCommand(kitchen_light)

remote = RemoteControl()

# Turn on living room light
remote.set_command(living_room_on)
remote.press_button()

# Turn on kitchen light
remote.set_command(kitchen_on)
remote.press_button()

# Turn off kitchen light
remote.set_command(kitchen_off)
remote.press_button()

# Undo last command (turn kitchen light back on)
remote.undo_last()


# ----------------------------------------------------------------------------
# 15. Interpreter Pattern
# ----------------------------------------------------------------------------
print("\n15. Interpreter Pattern")

class Expression(abc.ABC):
    @abc.abstractmethod
    def interpret(self, context: Dict[str, bool]) -> bool:
        pass

class TerminalExpression(Expression):
    def __init__(self, variable: str):
        self.variable = variable
    
    def interpret(self, context: Dict[str, bool]) -> bool:
        return context.get(self.variable, False)

class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def interpret(self, context: Dict[str, bool]) -> bool:
        return self.expr1.interpret(context) or self.expr2.interpret(context)

class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2
    
    def interpret(self, context: Dict[str, bool]) -> bool:
        return self.expr1.interpret(context) and self.expr2.interpret(context)

class NotExpression(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr
    
    def interpret(self, context: Dict[str, bool]) -> bool:
        return not self.expr.interpret(context)


# Testing Interpreter
# Build the expression: (A AND B) OR (C AND NOT D)
a = TerminalExpression("A")
b = TerminalExpression("B")
c = TerminalExpression("C")
d = TerminalExpression("D")

a_and_b = AndExpression(a, b)
not_d = NotExpression(d)
c_and_not_d = AndExpression(c, not_d)
expression = OrExpression(a_and_b, c_and_not_d)

# Define a context
context = {"A": True, "B": False, "C": True, "D": False}

# Interpret the expression
result = expression.interpret(context)
print(f"Expression (A AND B) OR (C AND NOT D) with context {context} = {result}")

# Change context and interpret again
context = {"A": False, "B": False, "C": True, "D": True}
result = expression.interpret(context)
print(f"Expression (A AND B) OR (C AND NOT D) with context {context} = {result}")


# ----------------------------------------------------------------------------
# 16. Iterator Pattern
# ----------------------------------------------------------------------------
print("\n16. Iterator Pattern")

class Iterator(abc.ABC):
    @abc.abstractmethod
    def has_next(self) -> bool:
        pass
    
    @abc.abstractmethod
    def next(self) -> Any:
        pass

class Collection(abc.ABC):
    @abc.abstractmethod
    def create_iterator(self) -> Iterator:
        pass

class ConcreteIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self.collection = collection
        self.position = 0
    
    def has_next(self) -> bool:
        return self.position < len(self.collection)
    
    def next(self) -> Any:
        if not self.has_next():
            raise StopIteration()
        item = self.collection[self.position]
        self.position += 1
        return item

class ConcreteCollection(Collection):
    def __init__(self):
        self.items: List[Any] = []
    
    def add_item(self, item: Any) -> None:
        self.items.append(item)
    
    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self.items)


# Testing Iterator
collection = ConcreteCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")
collection.add_item("Item 4")

iterator = collection.create_iterator()
print("Iterating through collection:")
while iterator.has_next():
    print(iterator.next())


# ----------------------------------------------------------------------------
# 17. Mediator Pattern
# ----------------------------------------------------------------------------
print("\n17. Mediator Pattern")

class ChatMediator(abc.ABC):
    @abc.abstractmethod
    def send_message(self, message: str, user: 'User') -> None:
        pass
    
    @abc.abstractmethod
    def add_user(self, user: 'User') -> None:
        pass

class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []
    
    def add_user(self, user: 'User') -> None:
        self.users.append(user)
        print(f"ChatRoom: {user.name} joined the chat")
    
    def send_message(self, message: str, sender: 'User') -> None:
        for user in self.users:
            # Don't send message back to sender
            if user != sender:
                user.receive(message, sender.name)

class User(abc.ABC):
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
    
    @abc.abstractmethod
    def send(self, message: str) -> None:
        pass
    
    @abc.abstractmethod
    def receive(self, message: str, sender_name: str) -> None:
        pass

class ChatUser(User):
    def send(self, message: str) -> None:
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)
    
    def receive(self, message: str, sender_name: str) -> None:
        print(f"{self.name} receives from {sender_name}: {message}")


# Testing Mediator
chat_room = ChatRoom()

alice = ChatUser("Alice", chat_room)
bob = ChatUser("Bob", chat_room)
charlie = ChatUser("Charlie", chat_room)

chat_room.add_user(alice)
chat_room.add_user(bob)
chat_room.add_user(charlie)

alice.send("Hi everyone!")
bob.send("Hey Alice, how are you?")
charlie.send("Hello everyone!")


# ----------------------------------------------------------------------------
# 18. Memento Pattern
# ----------------------------------------------------------------------------
print("\n18. Memento Pattern")

class EditorMemento:
    def __init__(self, content: str):
        self._content = content
    
    def get_content(self) -> str:
        return self._content

class Editor:
    def __init__(self):
        self.content = ""
    
    def type(self, words: str) -> None:
        self.content += words
    
    def get_content(self) -> str:
        return self.content
    
    def save(self) -> EditorMemento:
        return EditorMemento(self.content)
    
    def restore(self, memento: EditorMemento) -> None:
        self.content = memento.get_content()

class History:
    def __init__(self):
        self.states: List[EditorMemento] = []
    
    def push(self, state: EditorMemento) -> None:
        self.states.append(state)
    
    def pop(self) -> EditorMemento:
        if not self.states:
            return None
        last_state = self.states[-1]
        self.states.pop()
        return last_state


# Testing Memento
editor = Editor()
history = History()

# Initial state
editor.type("First line of text. ")
print(f"Current content: '{editor.get_content()}'")

# Save state
history.push(editor.save())

# Add more content
editor.type("Second line of text. ")
print(f"Current content: '{editor.get_content()}'")

# Save state
history.push(editor.save())

# Add more content
editor.type("Third line that we'll undo. ")
print(f"Current content: '{editor.get_content()}'")

# Restore to last saved state
editor.restore(history.pop())
print(f"After undo: '{editor.get_content()}'")

# Restore to first saved state
editor.restore(history.pop())
print(f"After another undo: '{editor.get_content()}'")


# ----------------------------------------------------------------------------
# 19. Observer Pattern
# ----------------------------------------------------------------------------
print("\n19. Observer Pattern")

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass

class Subject(abc.ABC):
    @abc.abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass
    
    @abc.abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass
    
    @abc.