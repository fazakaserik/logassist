
from logassist import LogAssistant

# Create an instance of LogAssistant
logassistant = LogAssistant()

# Applying the decorator
@logassistant.log
def example_function(x):
    return x ** 2

if __name__ == "__main__":

    example_function(5)
    example_function(10)
