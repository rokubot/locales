from locales_test import verify_translations

def test_msgid_integrity():
    result = verify_translations()
    assert result == 0, "Translation msgid verification failed"
