# def test_menu_link_by_index(app):
#     expected_header = "PC"
#     app.open_home_page()
#     app.open_menu_item_by_index(i=2)
#     header = app.get_content_header_by_index(i=2)
#     assert header == expected_header


def test_menu_links_open_correct_pages(app):
    expected_headers = ['PC', 'Mac', 'Macs', 'Windows', 'Mice and Trackballs', 'Monitors', 'Printers', 'Scanners',
                        'Web Cameras', 'Tablets', 'Software', 'Phones & PDAs', 'Cameras', 'test 11', 'test 12',
                        'test 15', 'test 16', 'test 17', 'test 18', 'test 19', 'test 20', 'test 21', 'test 22',
                        'test 23', 'test 24', 'test 4', 'test 5', 'test 6', 'test 7', 'test 8', 'test 9']
    app.open_home_page()
    content_headers = app.get_content_headers()
    print("\nActual content headers:\n{}".format(content_headers))
    # expected_headers = db.get_content_headers()
    assert content_headers == expected_headers
