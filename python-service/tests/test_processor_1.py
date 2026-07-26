from app.processors.processor_1 import Processor1


def test_processor_returns_expected_value():
    processor = Processor1()

    assert processor.process() == "processor completed"