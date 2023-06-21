
import os
from unittest.mock import patch, MagicMock
import pytest
import mysql.connector
from module import get_connection

@pytest.fixture
def mock_os_environ():
    with patch.dict("os.environ", {
        "LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN": "1",
        "DB_HOST": "localhost",
        "DB_PORT": "3306",
        "DB_USER": "user",
        "DB_PASS": "password",
        "DB_NAME": "database",
        "DB_SECRETS_PMD": "secret"
    }):
        yield

@pytest.fixture
def mock_mysql_connector_connect():
    with patch("mysql.connector.connect") as mock:
        yield mock

def test_get_connection(mock_os_environ, mock_mysql_connector_connect):
    # Configurando o mock do método connect
    mock_connection = MagicMock(spec=mysql.connector.connection_cext.CMySQLConnection)
    mock_mysql_connector_connect.return_value = mock_connection

    conn = get_connection()

    # Asserts
    mock_mysql_connector_connect.assert_called_once_with(
        host="localhost",
        user="user",
        passwd="password",
        port="3306",
        database="database",
        ssl_ca="ca_bundle.crt"
    )
    assert conn == mock_connection

if __name__ == "__main__":
    pytest.main()






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

