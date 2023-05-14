import unittest
from unittest.mock import patch

from flask import Flask

from app.project.tasks import process_crawl


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_process_crawl(self):
        crawl_id = 1
        url = 'https://example.com'

        with self.app.app_context():
            # Mock the necessary functions and modules
            with patch('app.project.tasks.requests') as mock_requests:
                with patch('app.project.tasks.current_app') as mock_current_app:
                    # Mock the response object
                    mock_response = mock_requests.get.return_value
                    mock_response.status_code = 200
                    mock_response.text = '<html><body>Mock HTML</body></html>'

                    # Mock the necessary functions
                    with patch('app.project.tasks.update_crawl_status') as mock_update_crawl_status:
                        with patch('app.project.tasks.mock_save_html') as mock_mock_save_html:
                            process_crawl(crawl_id)

                            assert mock_response.status_code == 200


if __name__ == '__main__':
    unittest.main()
