from app.config.settings import settings

def test_settings_loaded():
    assert settings.APP_NAME is not None