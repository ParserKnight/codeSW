

import pytest
import os 
from service_functions import mflip
from service_functions import efip
from service_functions import eps
from service_functions import bytes_
from service_functions import digest_path
from event import Event
from batch import Batch
from factory import Factory
from script import run

def test_is_folder():
    """path is a folder"""
    paths = digest_path("tests")
    
    assert set([
        'tests/test_folder/test_file_1.txt',
        'tests/test_folder/test_file_2.txt',
        'tests/test_file.txt',
        'tests/test_folder/test_file.txt',
        'tests/test_folder/level2_folder/test_file_3.txt']) == set(paths)

def test_is_file():
    """path is a file"""
    paths = digest_path("tests/test_folder/test_file.txt")
    assert ["tests/test_folder/test_file.txt"] == paths

def test_event_creation_1():
    with pytest.raises(TypeError):
        event = Event("valor1","valor2")

def test_event_creation_2():
    with pytest.raises(ValueError):
        event = Event(*["1157689408str223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"])

def test_event_creation_3():
    with pytest.raises(ValueError):
        event = Event(*["1157689408.223",
        "1502str",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"])

def test_event_creation_4():
    with pytest.raises(ValueError):
        event = Event(*["1157689408.223",
        "1502",
        "10.105.21.199str", #falta validacion de ip
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"])

def test_event_creation_5():
    with pytest.raises(AttributeError):
        event = Event(*["1157689408.223",
        "1502",
        "10.105.21.199",
        34,
        "1112str",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"])

def test_event_creation_7():
    with pytest.raises(ValueError):
        event = Event(*["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112asdasd",
        "GETstr",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"])

def test_event_creation_8():
    with pytest.raises(ValueError):
        event = Event(*["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112asdasd",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        45, 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"])

def test_event_creation_9():
    with pytest.raises(ValueError):
        event = Event(*["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112asdasd",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        45, 
        "application/x-javascript"])

def test_event_creation_10():
    with pytest.raises(ValueError):
        event = Event(*["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112asdasd",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        87])

def test_mflip():
    """Most frequent IP"""

    values = [
        ["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"],
        ["1157689408.223",
        "1502",
        "10.105.21.198",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"],
        ["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"]
    ]

    events = [Event(*value) for value in values]
    batch = Batch(events)
    output = mflip(batch.list_ips)
    assert output =="10.105.21.199"


def test_efip():
    """Least frequent IP"""

    values = [
        ["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"],
        ["1157689408.223",
        "1502",
        "10.105.21.198",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"],
        ["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"]
    ]

    events = [Event(*value) for value in values]
    batch = Batch(events)
    output = efip(batch.list_ips)
    assert output =="10.105.21.198"

def test_eps():
    """events per second"""
    values = [
        ["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"],
        ["1157689408.223",
        "1502",
        "10.105.21.198",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"],
        ["1157689432.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"]
    ]

    events = [Event(*value) for value in values]
    batch = Batch(events)
    output = eps(batch.list_timestamps)
    assert round(output,2) ==round(0.12,2)

def test_bytes():
    """Total amount of bytes exchanged"""
    values = [
        ["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"],
        ["1157689408.223",
        "1502",
        "10.105.21.198",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"],
        ["1157689408.223",
        "1502",
        "10.105.21.199",
        "TCP_REFRESH_HIT/200",
        "1112",
        "GET",
        "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
        "badeyek", 
        "DIRECT/209.62.178.182", 
        "application/x-javascript"]
    ]

    events = [Event(*value) for value in values]
    batch = Batch(events)
    output = bytes_(batch.list_by_tes)
    assert round(output,2) == round(3336.0,2)


def test_batch():
    """Batch construction"""
    with pytest.raises(TypeError):
        values = [
            ["1157689408.223",
            "1502",
            "10.105.21.199",
            "TCP_REFRESH_HIT/200",
            "1112",
            "GET",
            "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
            "badeyek", 
            "DIRECT/209.62.178.182", 
            "application/x-javascript"],
            ["1157689408.223",
            "1502",
            "10.105.21.198",
            "TCP_REFRESH_HIT/200",
            "1112",
            "GET",
            "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
            "badeyek", 
            "DIRECT/209.62.178.182", 
            "application/x-javascript"],
            ["1157689408.223",
            "1502",
            "10.105.21.199",
            "TCP_REFRESH_HIT/200",
            "1112",
            "GET",
            "http://m.uk.2mdn.net/879366/flashwrite_1_2.js", 
            "badeyek", 
            "DIRECT/209.62.178.182", 
            "application/x-javascript"]
        ]

        events = [Event(*value) for value in values]
        events.append(["value1,value2"])
        batch = Batch(events)
        
def test_factory_event():
    """Factory event test"""
    path="tests/test_file.txt"
    path = digest_path(path)
    events = Factory().gather_events(path)
    assert len(events)==25


def test_factory_batch():
    """Factory batch creation test"""
    path="tests/test_file.txt"
    path = digest_path(path)
    events = Factory().gather_events(path)
    batch = Factory().create_batch(events)
    assert len(batch.batch) == 25

def test_factory_batch():
    """Invalid event going through batch creation"""
    path="tests/test_folder/test_file.txt"
    path = digest_path(path)
    events = Factory().gather_events(path)
    batch = Factory().create_batch(events)
    assert len(batch.batch) == 24

def test_run():
    """Test run with valid options"""
    path= "tests/test_folder/test_file.txt"
    argv= ["--mflip"]
    value = run(path,"text_output.txt",argv)
    assert value == {'common ip': '10.105.21.199'}

def test_run_multiple():
    """Test run with valid multiple options"""
    path= "tests/test_folder/test_file.txt"
    argv= ["--mflip","--eps", "--efip", "--bytes"]
    value = run(path,"text_output.txt",argv)
    assert len(value) == 4

def test_run_invalid():
    """Test with invalid options"""
    with pytest.raises(ValueError):
        path= "tests/test_folder/test_file.txt"
        argv= ["--mflip","--invalid"]
        value = run(path,"text_output.txt", argv)
        