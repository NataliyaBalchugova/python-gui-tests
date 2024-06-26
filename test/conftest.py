import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture=Application("C:\\Users\\b9l4e\\Downloads\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

