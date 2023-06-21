import pytest
from unittest.mock import patch, MagicMock
from module import process_notification

@pytest.fixture
def mock_envia_email():
    with patch("module.envia_email") as mock:
        yield mock

@pytest.fixture
def mock_insert_registro_email():
    with patch("module.insert_registro_email") as mock:
        yield mock

@pytest.fixture
def mock_update_registro_email():
    with patch("module.update_registro_email") as mock:
        yield mock

@pytest.fixture
def mock_logger():
    with patch("module.logger") as mock:
        yield mock

def test_process_notification_success(mock_logger, mock_update_registro_email, mock_insert_registro_email, mock_envia_email):
    # Configurando o mock do método envia_email
    mock_envia_email.return_value.status_code = 202

    dados = {
        "num_ota": "123456",
        "status": 2
    }

    process_notification(dados)

    # Asserts do teste

if __name__ == "__main__":
    pytest.main()






import unittest
from unittest.mock import patch, MagicMock
from module import process_notification

class ProcessNotificationTest(unittest.TestCase):
    @patch("module.envia_email")
    @patch("module.insert_registro_email")
    @patch("module.update_registro_email")
    @patch("module.logger")
    def test_process_notification_success(self, mock_logger, mock_update_registro_email, mock_insert_registro_email, mock_envia_email):
        dados = {
            "num_ota": "123456",
            "status": 2
        }
        mock_envia_email.return_value = MagicMock(status_code=202)

        process_notification(dados)

        mock_envia_email.assert_called_once_with(dados)
        mock_logger.info.assert_called_once_with({"sucesso": "Notificação de e-mail foi enviada com sucesso!"})
        mock_update_registro_email.assert_called_once_with("123456", 41)
        mock_insert_registro_email.assert_not_called()

    @patch("module.envia_email")
    @patch("module.insert_registro_email")
    @patch("module.update_registro_email")
    @patch("module.logger")
    def test_process_notification_failure(self, mock_logger, mock_update_registro_email, mock_insert_registro_email, mock_envia_email):
        dados = {
            "num_ota": "123456",
            "status": 1
        }
        mock_envia_email.return_value = MagicMock(status_code=500)

        process_notification(dados)

        mock_envia_email.assert_called_once_with(dados)
        mock_logger.info.assert_called_once_with({"sucesso": "Notificação de e-mail não foi enviada!"})
        mock_update_registro_email.assert_not_called()
        mock_insert_registro_email.assert_called_once_with("123456", 42)

if __name__ == "__main__":
    unittest.main()






import unittest

from unittest.mock import patch, MagicMock

from module import process_notification

class ProcessNotificationTest(unittest.TestCase):

    @patch("module.envia_email")

    @patch("module.insert_registro_email")

    @patch("module.update_registro_email")

    @patch("module.logger")

    def test_process_notification_success(self, mock_logger, mock_update_registro_email, mock_insert_registro_email, mock_envia_email):

        dados = {

            "num_ota": "123456",

            "status": 2

        }

        mock_envia_email.return_value = 202

        process_notification(dados)

        mock_envia_email.assert_called_once_with(dados)

        mock_logger.info.assert_called_once_with({"sucesso": "Notificação de e-mail foi enviada com sucesso!"})

        mock_update_registro_email.assert_called_once_with("123456", 41)

        mock_insert_registro_email.assert_not_called()

    @patch("module.envia_email")

    @patch("module.insert_registro_email")

    @patch("module.update_registro_email")

    @patch("module.logger")

    def test_process_notification_failure(self, mock_logger, mock_update_registro_email, mock_insert_registro_email, mock_envia_email):

        dados = {

            "num_ota": "123456",

            "status": 1

        }

        mock_envia_email.return_value = 500

        process_notification(dados)

        mock_envia_email.assert_called_once_with(dados)

        mock_logger.info.assert_called_once_with({"sucesso": "Notificação de e-mail não foi enviada!"})

        mock_update_registro_email.assert_not_called()

        mock_insert_registro_email.assert_called_once_with("123456", 42)

if __name__ == "__main__":

    unittest.main()

